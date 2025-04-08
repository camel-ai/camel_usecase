import os
import gradio as gr
import tempfile
import logging
from pathlib import Path

# 设置日志
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 支持的文件类型
SUPPORTED_EXTENSIONS = ['.md', '.txt', '.json']

def get_file_extension(file_path):
    """获取文件扩展名"""
    return os.path.splitext(file_path)[1].lower()

def collect_files_from_folder(folder_path):
    """从文件夹中收集所有支持的文件"""
    collected_files = []
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            ext = get_file_extension(file_path)
            if ext in SUPPORTED_EXTENSIONS:
                collected_files.append(file_path)
                
    return collected_files

def process_files(files):
    """
    处理上传的文件并合并相同类型的文件
    
    Args:
        files: 上传的文件列表
        
    Returns:
        合并后的文件列表
    """
    if not files:
        return None
        
    logger.info(f"接收到 {len(files)} 个文件/文件夹")
    
    # 处理所有文件和文件夹
    all_files = []
    
    for file in files:
        try:
            file_path = file.name if hasattr(file, 'name') else str(file)
            logger.info(f"处理: {file_path}")
            
            if os.path.isdir(file_path):
                # 如果是文件夹，收集所有支持的文件
                folder_files = collect_files_from_folder(file_path)
                logger.info(f"从文件夹 {file_path} 收集了 {len(folder_files)} 个文件")
                all_files.extend(folder_files)
            else:
                # 单个文件
                ext = get_file_extension(file_path)
                if ext in SUPPORTED_EXTENSIONS:
                    all_files.append(file_path)
                    
        except Exception as e:
            logger.error(f"处理时出错: {str(e)}")
    
    # 按扩展名分组文件
    files_by_extension = {}
    
    for file_path in all_files:
        try:
            ext = get_file_extension(file_path)
            if ext not in SUPPORTED_EXTENSIONS:
                continue
                
            if ext not in files_by_extension:
                files_by_extension[ext] = []
            files_by_extension[ext].append(file_path)
        except Exception as e:
            logger.error(f"处理文件 {file_path} 时出错: {str(e)}")
    
    # 合并文件
    merged_files = []
    
    for ext, file_list in files_by_extension.items():
        if len(file_list) < 2:  # 只有一个文件不需要合并
            logger.info(f"类型 {ext} 只有一个文件，不合并")
            continue
            
        logger.info(f"合并 {len(file_list)} 个 {ext} 类型的文件")
        
        # 创建临时文件
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
        output_path = output_file.name
        output_file.close()
        
        try:
            with open(output_path, mode='w', encoding='utf-8') as outfile:
                for file_path in file_list:
                    try:
                        with open(file_path, mode='r', encoding='utf-8') as infile:
                            # 添加分隔符
                            if outfile.tell() > 0:
                                outfile.write(f"\n\n--- 来自: {os.path.basename(file_path)} ---\n\n")
                            
                            outfile.write(infile.read())
                    except Exception as e:
                        logger.error(f"读取文件 {file_path} 时出错: {str(e)}")
                        
            merged_files.append((f"merged{ext}", output_path))
        except Exception as e:
            logger.error(f"创建合并文件时出错: {str(e)}")
    
    # 返回合并后的文件
    if not merged_files:
        return "没有可合并的文件"
    
    return [file[1] for file in merged_files]

# 创建简化的Gradio界面
with gr.Blocks() as demo:
    gr.Markdown("# 文件合并工具")
    gr.Markdown("上传多个文件或文件夹，将自动合并所有 `.md`、`.txt` 和 `.json` 文件")
    
    with gr.Row():
        upload_btn = gr.UploadButton("上传文件或文件夹", file_count="multiple", file_types=["file", "directory"])
    
    with gr.Row():
        output = gr.Files(label="合并后的文件")
    
    upload_btn.upload(
        fn=process_files,
        inputs=upload_btn,
        outputs=output
    )

if __name__ == "__main__":
    logger.info("启动文件合并工具")
    demo.launch() 