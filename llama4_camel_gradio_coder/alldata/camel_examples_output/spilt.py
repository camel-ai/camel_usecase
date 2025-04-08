import os

def split_text_file(input_file, max_chars, output_dir):
    """
    将文本文件按照最大字符数拆分成多个文件
    
    Args:
        input_file (str): 输入文件路径
        max_chars (int): 每个文件的最大字符数
        output_dir (str): 输出目录路径
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 计算需要拆分的文件数
    total_chars = len(content)
    num_files = (total_chars + max_chars - 1) // max_chars
    
    # 拆分并写入文件
    for i in range(num_files):
        start = i * max_chars
        end = min((i + 1) * max_chars, total_chars)
        
        # 生成输出文件名
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}_part{i+1}.txt")
        
        # 写入拆分的内容
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content[start:end])
            
    return num_files

def main():
    # 示例使用
    input_file = "merged01.txt"  # 输入文件路径
    max_chars = 450000  # 每个文件最大字符数
    output_dir = "split_output"  # 输出目录
    
    num_files = split_text_file(input_file, max_chars, output_dir)
    print(f"文件已被拆分为 {num_files} 个部分")

if __name__ == "__main__":
    main()
