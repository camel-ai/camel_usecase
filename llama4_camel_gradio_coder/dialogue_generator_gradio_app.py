# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========

import os
import json
import tempfile
import gradio as gr
from datetime import datetime
import time
import traceback

# 导入主题生成和对话生成模块
from topic_generator import generate_topics, save_topics
from roleplay_dialogue_generator import generate_dialogue, save_dialogue, load_topics_from_file

# 导入CAMEL相关模块
from camel.configs import OpenRouterConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType


def create_model(temperature=0.7, api_key=None):
    """创建CAMEL模型"""
    try:
        # 如果提供了API密钥，则使用它
        if api_key:
            os.environ["OPENROUTER_API_KEY"] = api_key
        
        # 检查API密钥是否已设置
        if "OPENROUTER_API_KEY" not in os.environ:
            raise ValueError("OpenRouter API密钥未设置。请在环境变量中设置OPENROUTER_API_KEY或在界面中输入API密钥。")
        
        return ModelFactory.create(
            model_platform=ModelPlatformType.OPENROUTER,
            model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
            model_config_dict=OpenRouterConfig(temperature=temperature).as_dict(),
        )
    except Exception as e:
        print(f"创建模型时出错: {str(e)}")
        raise


def generate_dialogues_from_input(
    input_text,
    num_topics,
    num_dialogues,
    topic_type,
    assistant_role,
    user_role,
    chat_turn_limit,
    temperature,
    api_key,
    progress=gr.Progress()
):
    """从输入文本生成主题和对话"""
    try:
        # 检查输入文本是否为空
        if not input_text.strip():
            return "错误: 输入文本不能为空", []
        
        # 创建临时目录
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建临时文件
            input_file = os.path.join(temp_dir, "input.txt")
            topics_file = os.path.join(temp_dir, "topics.txt")
            output_dir = os.path.join(temp_dir, "dialogues")
            os.makedirs(output_dir, exist_ok=True)
            
            # 保存输入文本到临时文件
            with open(input_file, "w", encoding="utf-8") as f:
                f.write(input_text)
            
            # 创建模型
            try:
                model = create_model(temperature, api_key)
                print("模型创建成功")
            except Exception as e:
                error_msg = f"创建模型时出错: {str(e)}\n{traceback.format_exc()}"
                print(error_msg)
                return f"错误: {error_msg}", []
            
            # 步骤1：生成主题
            progress(0, desc="生成主题中...")
            try:
                topics = generate_topics(
                    model=model,
                    input_content=input_text,
                    num_topics=num_topics,
                    topic_type=topic_type
                )
                print(f"成功生成 {len(topics)} 个主题")
            except Exception as e:
                error_msg = f"生成主题时出错: {str(e)}\n{traceback.format_exc()}"
                print(error_msg)
                return f"错误: {error_msg}", []
            
            # 保存主题
            save_topics(topics, topics_file)
            
            # 步骤2：生成对话
            dialogue_files = []
            total_steps = len(topics) * num_dialogues
            current_step = 0
            dialogue_contents = []
            
            for topic_idx, topic in enumerate(topics):
                for i in range(num_dialogues):
                    current_step += 1
                    progress(current_step / total_steps, desc=f"生成对话中... ({current_step}/{total_steps})")
                    
                    try:
                        print(f"开始为主题 '{topic}' 生成对话 {i+1}/{num_dialogues}")
                        # 使用原始输入文本作为上下文生成对话
                        dialogue = generate_dialogue(
                            model=model,
                            topic=topic,
                            assistant_role=assistant_role,
                            user_role=user_role,
                            chat_turn_limit=chat_turn_limit,
                            context=input_text  # 添加原始输入文本作为上下文
                        )
                        
                        # 保存对话
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"{topic.replace(' ', '_')}_{i+1}_{timestamp}.json"
                        filepath = os.path.join(output_dir, filename)
                        
                        with open(filepath, "w", encoding="utf-8") as f:
                            json.dump(dialogue, f, ensure_ascii=False, indent=2)
                        
                        dialogue_files.append(filepath)
                        dialogue_contents.append(dialogue)
                        print(f"主题 '{topic}' 的对话 {i+1}/{num_dialogues} 生成完成")
                    except Exception as e:
                        error_msg = f"生成对话 '{topic}' 时出错: {str(e)}"
                        print(error_msg)
                        # 创建一个基本的对话结构
                        basic_dialogue = {
                            "topic": topic,
                            "assistant_role": assistant_role,
                            "user_role": user_role,
                            "messages": [
                                {
                                    "role": "system",
                                    "content": f"生成对话时出错: {str(e)}"
                                }
                            ]
                        }
                        dialogue_contents.append(basic_dialogue)
                        continue
            
            # 返回生成的主题和对话
            if not dialogue_contents:
                print("警告：没有生成任何对话")
                return "\n".join(topics), []
            
            print(f"生成了 {len(dialogue_contents)} 个对话")
            return "\n".join(topics), dialogue_contents
    
    except Exception as e:
        error_msg = f"处理过程中出错: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return f"错误: {error_msg}", []


def format_dialogue(dialogue):
    """格式化对话内容为HTML"""
    html = f"<h3>主题: {dialogue['topic']}</h3>"
    html += f"<p><strong>助手角色:</strong> {dialogue['assistant_role']}</p>"
    html += f"<p><strong>用户角色:</strong> {dialogue['user_role']}</p>"
    html += "<h4>对话内容:</h4>"
    
    for msg in dialogue["messages"]:
        role = msg["role"]
        content = msg["content"]
        

        if role == "assistant":
            html += f"<div style='background-color: #e6f7ff; padding: 10px; margin: 5px 0; border-left: 5px solid #1890ff;'><strong>助手:</strong> {content}</div>"
        elif role == "user":
            html += f"<div style='background-color: #f6ffed; padding: 10px; margin: 5px 0; border-left: 5px solid #52c41a;'><strong>用户:</strong> {content}</div>"
    
    return html


def create_gradio_app():
    """创建Gradio应用程序"""
    with gr.Blocks(title="CAMEL对话数据生成器", theme=gr.themes.Soft()) as app:
        gr.Markdown("# CAMEL对话数据生成器")
        gr.Markdown("基于CAMEL框架的RolePlaying功能，从输入文本生成主题和对话数据")
        
        # 创建一个状态变量来存储生成的对话数据
        all_dialogues = gr.State([])
        topics_text = gr.State("")
        original_input_text = gr.State("")
        
        with gr.Row():
            with gr.Column(scale=1):
                with gr.Tab("文本输入"):
                    input_text = gr.Textbox(
                        label="输入文本",
                        placeholder="请输入用于生成主题的文本内容...",
                        lines=10
                    )
                
                with gr.Tab("文件上传"):
                    file_input = gr.File(
                        label="上传文本文件",
                        file_types=[".txt"],
                        type="file"
                    )
                
                api_key = gr.Textbox(
                    label="OpenRouter API密钥",
                    placeholder="请输入您的OpenRouter API密钥",
                    type="password"
                )
                
                with gr.Row():
                    num_topics = gr.Slider(
                        minimum=1,
                        maximum=200,
                        value=5,
                        step=1,
                        label="生成主题数量"
                    )
                    num_dialogues = gr.Slider(
                        minimum=1,
                        maximum=1000,
                        value=1,
                        step=1,
                        label="每个主题生成的对话数量"
                    )
                
                topic_type = gr.Textbox(
                    label="主题类型",
                    value="编程项目",
                    placeholder="例如：编程项目、商业计划、教育课程等"
                )
                
                with gr.Row():
                    assistant_role = gr.Textbox(
                        label="助手角色",
                        value="Python程序员",
                        placeholder="例如：Python程序员、数据分析师等"
                    )
                    user_role = gr.Textbox(
                        label="用户角色",
                        value="股票交易员",
                        placeholder="例如：股票交易员、项目经理等"
                    )
                
                chat_turn_limit = gr.Slider(
                    minimum=2,
                    maximum=100,
                    value=50,
                    step=1,
                    label="对话轮次限制"
                )
                
                temperature = gr.Slider(
                    minimum=0.1,
                    maximum=1.0,
                    value=0.7,
                    step=0.1,
                    label="模型温度（越高越随机）"
                )
                
                generate_topics_btn = gr.Button("生成主题", variant="primary")
                generate_dialogues_btn = gr.Button("生成对话", variant="primary")
            
            with gr.Column(scale=1):
                with gr.Tabs():
                    with gr.TabItem("主题编辑"):
                        generated_topics = gr.Textbox(
                            label="主题列表（每行一个主题，可以编辑）",
                            lines=10,
                            interactive=True
                        )
                        download_topics_btn = gr.Button("下载主题列表", variant="secondary")
                    
                    with gr.TabItem("生成的对话"):
                        dialogue_dropdown = gr.Dropdown(
                            label="选择对话",
                            choices=[],
                            interactive=True,
                            allow_custom_value=True
                        )
                        dialogue_content = gr.HTML(label="对话内容")
                        download_dialogue_btn = gr.Button("下载当前对话", variant="secondary")
                        download_all_btn = gr.Button("下载所有对话", variant="secondary")
        
        # 设置事件处理
        def update_dialogue_dropdown(dialogues):
            """更新对话下拉框选项并返回对话状态"""
            if not dialogues:
                # 确保返回空的选项列表和空的状态
                return gr.Dropdown.update(choices=[], value=None), []
            
            choices = []
            for i, d in enumerate(dialogues):
                topic = str(d.get('topic', '未知主题'))
                assistant = str(d.get('assistant_role', '未知助手'))
                user = str(d.get('user_role', '未知用户'))
                # 确保生成的标题是字符串
                title = f"{i+1}. {topic} ({assistant} 与 {user}的对话)"
                choices.append(title)
            
            # 更新下拉框选项，并将第一个选项设为默认值
            # 同时返回更新后的对话状态
            return gr.Dropdown.update(choices=choices, value=choices[0] if choices else None), dialogues
        
        def display_dialogue(dialogues, choice):
            """根据选择的标题显示对话内容"""
            if not choice or not dialogues:
                return ""
            
            try:
                # 确保 choice 是字符串
                if not isinstance(choice, str):
                    print(f"警告: display_dialogue 收到非字符串选择: {type(choice)}")
                    return "<p>错误：选择的对话格式不正确</p>"
                    
                # 从选项标题中提取索引
                index = int(choice.split('.')[0]) - 1
                if 0 <= index < len(dialogues):
                    return format_dialogue(dialogues[index])
                else:
                    return f"<p>错误：无法找到对话 {choice}</p>"
            except Exception as e:
                return f"<p>显示对话时出错：{str(e)}</p>"
        
        def read_file_content(file):
            if file is None:
                return ""
            with open(file.name, "r", encoding="utf-8") as f:
                return f.read()
        
        def save_topics_to_file(topics_text):
            """将主题保存到文件并返回下载链接"""
            if not topics_text:
                return None
            
            # 创建临时文件
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
                f.write(topics_text)
                return f.name
        
        def save_dialogue_to_file(dialogues, choice):
            """将选中的对话保存到文件并返回下载链接"""
            if not choice or not dialogues:
                return None
            
            try:
                # 从选项标题中提取索引
                index = int(choice.split('.')[0]) - 1
                if 0 <= index < len(dialogues):
                    dialogue = dialogues[index]
                    
                    # 创建临时文件
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8") as f:
                        json.dump(dialogue, f, ensure_ascii=False, indent=2)
                        return f.name
                else:
                    print(f"错误：无法找到对话 {choice}")
                    return None
            except Exception as e:
                print(f"保存对话时出错：{str(e)}")
                return None
        
        def save_all_dialogues_to_file(dialogues):
            """将所有对话保存到zip文件并返回下载链接"""
            if not dialogues:
                return None
            
            try:
                # 创建临时目录
                temp_dir = tempfile.mkdtemp()
                output_dir = os.path.join(temp_dir, "dialogues")
                os.makedirs(output_dir, exist_ok=True)
                
                # 保存所有对话到临时目录
                for i, dialogue in enumerate(dialogues):
                    filename = f"{dialogue['topic'].replace(' ', '_')}_{i+1}.json"
                    filepath = os.path.join(output_dir, filename)
                    with open(filepath, "w", encoding="utf-8") as f:
                        json.dump(dialogue, f, ensure_ascii=False, indent=2)
                
                # 创建zip文件
                zip_filename = os.path.join(temp_dir, "all_dialogues.zip")
                import shutil
                shutil.make_archive(os.path.splitext(zip_filename)[0], 'zip', output_dir)
                
                return zip_filename
            except Exception as e:
                print(f"保存所有对话时出错：{str(e)}")
                return None
        
        def generate_topics_only(input_text, num_topics, topic_type, temperature, api_key, progress=gr.Progress()):
            """仅生成主题，不生成对话"""
            try:
                if not input_text.strip():
                    return "错误: 输入文本不能为空", input_text
                
                # 创建模型
                try:
                    model = create_model(temperature, api_key)
                    print("模型创建成功")
                except Exception as e:
                    error_msg = f"创建模型时出错: {str(e)}\n{traceback.format_exc()}"
                    print(error_msg)
                    return f"错误: {error_msg}", input_text
                
                # 生成主题
                progress(0, desc="生成主题中...")
                try:
                    topics = generate_topics(
                        model=model,
                        input_content=input_text,
                        num_topics=num_topics,
                        topic_type=topic_type
                    )
                    print(f"成功生成 {len(topics)} 个主题")
                except Exception as e:
                    error_msg = f"生成主题时出错: {str(e)}\n{traceback.format_exc()}"
                    print(error_msg)
                    return f"错误: {error_msg}", input_text
                
                # 返回主题列表
                return "\n".join(topics), input_text
            
            except Exception as e:
                error_msg = f"处理过程中出错: {str(e)}\n{traceback.format_exc()}"
                print(error_msg)
                return f"错误: {error_msg}", input_text
        
        def generate_dialogues_from_topics(
            topics_text, 
            original_text,
            num_dialogues, 
            assistant_role, 
            user_role, 
            chat_turn_limit, 
            temperature, 
            api_key, 
            progress=gr.Progress()
        ):
            """从编辑过的主题生成对话"""
            try:
                # 检查主题文本是否为空
                if not topics_text.strip():
                    return "错误: 主题列表不能为空", []
                
                # 将主题文本拆分为主题列表
                topics = [line.strip() for line in topics_text.splitlines() if line.strip()]
                if not topics:
                    return "错误: 主题列表为空或格式不正确", []
                
                # 创建模型
                try:
                    model = create_model(temperature, api_key)
                    print("模型创建成功")
                except Exception as e:
                    error_msg = f"创建模型时出错: {str(e)}\n{traceback.format_exc()}"
                    print(error_msg)
                    return topics_text, []
                
                # 生成对话
                dialogue_contents = []
                total_steps = len(topics) * num_dialogues
                current_step = 0
                
                for topic_idx, topic in enumerate(topics):
                    for i in range(num_dialogues):
                        current_step += 1
                        progress(current_step / total_steps, desc=f"生成对话中... ({current_step}/{total_steps})")
                        
                        try:
                            print(f"开始为主题 '{topic}' 生成对话 {i+1}/{num_dialogues}")
                            # 使用原始输入文本作为上下文生成对话
                            dialogue = generate_dialogue(
                                model=model,
                                topic=topic,
                                assistant_role=assistant_role,
                                user_role=user_role,
                                chat_turn_limit=chat_turn_limit,
                                context=original_text  # 使用原始输入文本作为上下文
                            )
                            
                            # 确保对话包含所有必要的字段
                            if not isinstance(dialogue, dict):
                                raise ValueError("生成的对话格式不正确")
                            
                            # 添加或更新对话的基本信息
                            dialogue.update({
                                "topic": topic,
                                "assistant_role": assistant_role,
                                "user_role": user_role,
                                "dialogue_index": i + 1,
                                "total_dialogues": num_dialogues,
                                "context": original_text[:500] + "..." if len(original_text) > 500 else original_text
                            })
                            
                            # 确保messages字段存在且为列表
                            if "messages" not in dialogue or not isinstance(dialogue["messages"], list):
                                dialogue["messages"] = []
                            
                            dialogue_contents.append(dialogue)
                            print(f"主题 '{topic}' 的对话 {i+1}/{num_dialogues} 生成完成")
                        except Exception as e:
                            error_msg = f"生成对话 '{topic}' 时出错: {str(e)}"
                            print(error_msg)
                            # 创建一个基本的对话结构
                            basic_dialogue = {
                                "topic": topic,
                                "assistant_role": assistant_role,
                                "user_role": user_role,
                                "dialogue_index": i + 1,
                                "total_dialogues": num_dialogues,
                                "context": original_text[:500] + "..." if len(original_text) > 500 else original_text,
                                "messages": [
                                    {
                                        "role": "system",
                                        "content": f"生成对话时出错: {str(e)}"
                                    }
                                ]
                            }
                            dialogue_contents.append(basic_dialogue)
                            continue
                
                # 返回结果
                if not dialogue_contents:
                    print("警告：没有生成任何对话")
                    return topics_text, []
                
                print(f"生成了 {len(dialogue_contents)} 个对话")
                return topics_text, dialogue_contents
            
            except Exception as e:
                error_msg = f"处理过程中出错: {str(e)}\n{traceback.format_exc()}"
                print(error_msg)
                return topics_text, []
                
        # 文件上传时更新文本输入
        file_input.change(
            fn=read_file_content,
            inputs=[file_input],
            outputs=[input_text]
        )
        
        # 生成主题按钮
        generate_topics_btn.click(
            fn=generate_topics_only,
            inputs=[
                input_text,
                num_topics,
                topic_type,
                temperature,
                api_key
            ],
            outputs=[generated_topics, original_input_text]
        )
        
        # 生成对话按钮
        generate_dialogues_btn.click(
            fn=generate_dialogues_from_topics,
            inputs=[
                generated_topics,
                original_input_text,
                num_dialogues,
                assistant_role,
                user_role,
                chat_turn_limit,
                temperature,
                api_key
            ],
            # 直接更新 all_dialogues 状态
            outputs=[generated_topics, all_dialogues]
        ).then(
            # 根据新的 all_dialogues 状态更新下拉框
            fn=update_dialogue_dropdown,
            inputs=[all_dialogues],
            # 输出更新后的下拉框组件和状态
            outputs=[dialogue_dropdown, all_dialogues]
        ).then(
            # 清空对话显示区域
            fn=lambda: "", 
            inputs=None, 
            outputs=[dialogue_content]
        )
        
        # 显示选中的对话
        # 当 dialogue_dropdown 的值改变时触发
        dialogue_dropdown.change(
            fn=display_dialogue,
            # 输入包括 all_dialogues 状态和 dialogue_dropdown 的当前值
            inputs=[all_dialogues, dialogue_dropdown],
            outputs=dialogue_content
        )
        
        # 下载按钮事件
        download_topics_btn.click(
            fn=save_topics_to_file,
            inputs=[generated_topics],
            outputs=[gr.File(label="下载主题", visible=False)]
        )
        
        # 下载当前对话按钮
        # 输入应为 all_dialogues 状态和 dialogue_dropdown 的值 (choice)
        download_dialogue_btn.click(
            fn=save_dialogue_to_file,
            inputs=[all_dialogues, dialogue_dropdown], 
            outputs=[gr.File(label="下载对话", visible=False)]
        )
        
        # 下载所有对话按钮
        download_all_btn.click(
            fn=save_all_dialogues_to_file,
            inputs=[all_dialogues],
            outputs=[gr.File(label="下载所有对话", visible=False)]
        )
    
    return app


if __name__ == "__main__":
    app = create_gradio_app()
    # 启用队列功能并设置并发数
    app.queue(concurrency_count=1).launch() 