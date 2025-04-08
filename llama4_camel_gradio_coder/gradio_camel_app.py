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

import gradio as gr
import os
import tempfile
from camel.agents import ChatAgent
from camel.configs import OpenRouterConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.messages import BaseMessage

# 创建模型
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENROUTER,
    model_type=ModelType.OPENROUTER_LLAMA_4_MAVERICK,
    model_config_dict=OpenRouterConfig(temperature=0.2).as_dict(),
)

# 定义系统消息
sys_msg = "你是一个擅长结合camel框架和gradio框架而制作可视化gradio应用的专家，请你参考你的历史记忆，来回答用户的问题"

# 设置agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

# 存储上传的文件内容
uploaded_files_content = []

def upload_knowledge_base(file):
    """上传知识库文件并添加到agent的memory中"""
    if file is None:
        return "请选择要上传的文件", []
    
    try:
        # 读取上传的文件内容
        with open(file.name, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 创建用户消息
        knowledge_msg = BaseMessage.make_user_message(
            role_name="Knowledge Base",
            content=content,
        )
        
        # 更新agent的记忆
        camel_agent.record_message(knowledge_msg)
        
        # 存储上传的文件内容
        uploaded_files_content.append({
            "filename": os.path.basename(file.name),
            "content": content[:100] + "..." if len(content) > 100 else content
        })
        
        return f"成功上传知识库: {os.path.basename(file.name)}", uploaded_files_content
    except Exception as e:
        return f"上传失败: {str(e)}", uploaded_files_content

def chat_with_agent(message, history):
    """与agent进行对话"""
    if not message:
        return "", history
    
    # 创建用户消息
    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=message,
    )
    
    # 记录用户消息
    camel_agent.record_message(user_msg)
    
    # 获取响应
    response = camel_agent.step(message)
    
    # 获取响应内容
    response_content = response.msgs[0].content
    
    # 创建助手消息
    assistant_msg = BaseMessage.make_assistant_message(
        role_name="Assistant",
        content=response_content,
    )
    
    # 记录助手消息
    camel_agent.record_message(assistant_msg)
    
    # 更新历史记录
    history.append((message, response_content))
    
    return "", history

def clear_history():
    """清除对话历史"""
    # 使用camel_agent.reset()清空历史对话
    camel_agent.reset()
    return [], []

def get_context():
    """获取当前上下文"""
    context = camel_agent.memory.get_context()
    return context

# 创建Gradio界面
with gr.Blocks(theme=gr.themes.Soft(), title="CAMEL Agent 知识库对话系统") as demo:
    gr.Markdown("# 🐪 CAMEL Agent 知识库对话系统")
    gr.Markdown("上传知识库文件，然后与CAMEL Agent进行对话")
    
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="上传知识库文件", file_types=[".txt"])
            upload_button = gr.Button("上传知识库", variant="primary")
            upload_output = gr.Textbox(label="上传状态", interactive=False)
            uploaded_files = gr.Dataframe(
                headers=["文件名", "内容预览"],
                datatype=["str", "str"],
                label="已上传的知识库",
                interactive=False
            )
            context_button = gr.Button("查看当前上下文")
            context_output = gr.Textbox(label="当前上下文", lines=10, interactive=False)
        
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(
                label="对话历史",
                height=500,
                show_copy_button=True,
                avatar_images=(None, "https://api.dicebear.com/7.x/bottts/svg?seed=CAMEL")
            )
            with gr.Row():
                msg_input = gr.Textbox(
                    label="输入消息",
                    placeholder="输入您的问题...",
                    lines=3
                )
                submit_button = gr.Button("发送", variant="primary")
            
            clear_button = gr.Button("清除对话历史")
    
    # 设置事件处理
    upload_button.click(
        upload_knowledge_base,
        inputs=[file_input],
        outputs=[upload_output, uploaded_files]
    )
    
    submit_button.click(
        chat_with_agent,
        inputs=[msg_input, chatbot],
        outputs=[msg_input, chatbot]
    )
    
    msg_input.submit(
        chat_with_agent,
        inputs=[msg_input, chatbot],
        outputs=[msg_input, chatbot]
    )
    
    clear_button.click(
        clear_history,
        inputs=[],
        outputs=[chatbot]
    )
    
    context_button.click(
        get_context,
        inputs=[],
        outputs=[context_output]
    )

# 启动应用
if __name__ == "__main__":
    demo.launch(share=True) 