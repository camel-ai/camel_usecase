import os
import tempfile
import json
import gradio as gr
from datetime import datetime
import traceback

from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import OpenRouterConfig

# Import functional modules
from topic_generator import generate_topics, save_topics
from roleplay_dialogue_generator import generate_dialogue, save_dialogue

# CSS styling
css = """
body {
    font-family: 'Roboto', 'Arial', sans-serif;
    background-color: #f8f9fa;
    color: #202124;
}
.container {
    max-width: 1200px;
    margin: 0 auto;
}
.header {
    background-color: #4285f4;
    color: white;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    text-align: center;
    box-shadow: 0 2px 5px 0 rgba(0,0,0,0.16), 0 2px 10px 0 rgba(0,0,0,0.12);
}
.header h1 {
    font-size: 2.5rem;
    font-weight: 400;
    margin-bottom: 10px;
}
.card {
    background-color: white;
    border-radius: 8px;
    padding: 24px;
    box-shadow: 0 1px 2px 0 rgba(60,64,67,0.3), 0 1px 3px 1px rgba(60,64,67,0.15);
    margin-bottom: 20px;
    transition: box-shadow 0.2s;
}
.card:hover {
    box-shadow: 0 1px 3px 0 rgba(60,64,67,0.3), 0 4px 8px 3px rgba(60,64,67,0.15);
}
button {
    background-color: #4285f4 !important;
    border: none !important;
    border-radius: 4px !important;
    color: white !important;
    padding: 10px 24px !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.25px !important;
    transition: background-color 0.2s !important;
    box-shadow: 0 1px 2px 0 rgba(60,64,67,0.3), 0 1px 3px 1px rgba(60,64,67,0.15) !important;
}
button:hover {
    background-color: #1a73e8 !important;
    box-shadow: 0 1px 3px 0 rgba(60,64,67,0.3), 0 4px 8px 3px rgba(60,64,67,0.15) !important;
}
.gr-box {
    border-radius: 8px !important;
    border: 1px solid #dadce0 !important;
}
.gr-padded {
    padding: 16px !important;
}
.gr-form {
    border: none !important;
    box-shadow: none !important;
}
.footer {
    text-align: center;
    margin-top: 24px;
    padding: 16px;
    color: #5f6368;
    font-size: 0.9rem;
}
.upload-btn {
    background-color: #f8f9fa !important;
    border: 1px solid #dadce0 !important;
    border-radius: 4px !important;
    padding: 16px !important;
    transition: background-color 0.2s !important;
}
.upload-btn:hover {
    background-color: #f1f3f4 !important;
    border-color: #4285f4 !important;
}
.gr-button-secondary {
    background-color: #f1f3f4 !important;
    color: #1a73e8 !important;
    border: 1px solid #dadce0 !important;
}
.gr-button-secondary:hover {
    background-color: #e8eaed !important;
}
.gr-input, .gr-textarea {
    border-radius: 4px !important;
    border: 1px solid #dadce0 !important;
    padding: 12px !important;
    transition: border 0.2s !important;
}
.gr-input:focus, .gr-textarea:focus {
    border-color: #4285f4 !important;
    box-shadow: 0 0 0 2px rgba(66, 133, 244, 0.2) !important;
}
.tab-nav {
    margin-bottom: 16px !important;
}
.tab-nav button {
    font-size: 1rem !important;
    padding: 12px 24px !important;
    text-transform: none !important;
    font-weight: 500 !important;
    background-color: transparent !important;
    color: #5f6368 !important;
    box-shadow: none !important;
    border-bottom: 2px solid transparent !important;
    border-radius: 0 !important;
}
.tab-nav button.selected {
    color: #1a73e8 !important;
    border-bottom: 2px solid #1a73e8 !important;
}
.panel-header {
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid #dadce0;
    color: #1a73e8;
}
.info-icon {
    color: #4285f4;
    margin-left: 5px;
    cursor: help;
}
.gr-button-lg {
    padding: 12px 24px !important;
}
"""

def create_model():
    """Create an OpenRouter Llama 4 model instance"""
    return ModelFactory.create(
        model_platform=ModelPlatformType.OPENROUTER,
        model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT,
        model_config_dict=OpenRouterConfig(temperature=0.7).as_dict(),
    )

def process_uploaded_file(file_obj):
    """Process uploaded file and return its content"""
    if file_obj is None:
        return None
    
    try:
        content = file_obj.decode('utf-8')
        return content
    except UnicodeDecodeError:
        try:
            content = file_obj.decode('gbk')
            return content
        except:
            return "Unsupported file encoding. Please upload UTF-8 or GBK encoded text files."

def generate_topics_interface(input_text, upload_file, num_topics):
    """Gradio interface: Generate topics"""
    try:
        # If file is uploaded, prioritize file content
        if upload_file is not None:
            file_content = process_uploaded_file(upload_file)
            if file_content is not None and not file_content.startswith("Unsupported"):
                input_text = file_content
            elif file_content.startswith("Unsupported"):
                return file_content, None
        
        if not input_text.strip():
            return "Please enter text or upload a file", None
            
        # Create temp file to store input text
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as temp:
            temp.write(input_text)
            temp_path = temp.name

        # Create model
        model = create_model()
        
        # Generate topics
        topics = generate_topics(
            model=model,
            input_content=input_text,
            num_topics=num_topics
        )
        
        # Create output temp file
        output_path = f"generated_topics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        save_topics(topics, output_path)
        
        # Format output
        result = "\n".join([f"{i+1}. {topic}" for i, topic in enumerate(topics)])
        
        return result, output_path
    except Exception as e:
        error_trace = traceback.format_exc()
        return f"Error generating topics: {str(e)}\n{error_trace}", None

def generate_dialogue_interface(selected_topics, assistant_role, user_role, chat_turns, context_text, context_file):
    """Gradio interface: Generate dialogue"""
    try:
        # Parse selected topics
        topics = [topic.strip() for topic in selected_topics.split("\n") if topic.strip()]
        if not topics:
            return "Please select at least one topic", None
        
        # If context file is uploaded, prioritize file content
        if context_file is not None:
            file_content = process_uploaded_file(context_file)
            if file_content is not None and not file_content.startswith("Unsupported"):
                context_text = file_content
            elif file_content.startswith("Unsupported"):
                return file_content, None
                
        # Create output directory
        output_dir = f"generated_dialogues_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(output_dir, exist_ok=True)
        
        # Create model
        model = create_model()
        
        # Generate dialogue for each topic
        results = []
        dialogue_files = []
        
        for i, topic in enumerate(topics):
            topic = topic.split(". ", 1)[-1]  # Remove numbering if present
            
            result = f"--- Topic {i+1}: {topic} ---\n"
            dialogue = generate_dialogue(
                model=model,
                topic=topic,
                assistant_role=assistant_role,
                user_role=user_role,
                chat_turn_limit=chat_turns,
                context=context_text
            )
            
            # Save dialogue
            filename = f"{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(dialogue, f, ensure_ascii=False, indent=2)
            
            # Format dialogue content
            messages = []
            for msg in dialogue["messages"]:
                role = msg["role"]
                content = msg["content"]
                
                if role == "assistant":
                    messages.append(f"🤖 **{assistant_role}**: {content}")
                elif role == "user":
                    messages.append(f"👤 **{user_role}**: {content}")
                else:
                    messages.append(f"🔄 **System**: {content}")
            
            result += "\n\n" + "\n\n".join(messages)
            results.append(result)
            dialogue_files.append(filepath)
        
        return "\n\n" + "\n\n".join(results), output_dir
    except Exception as e:
        error_trace = traceback.format_exc()
        return f"Error generating dialogue: {str(e)}\n{error_trace}", None

# Create Gradio interface
with gr.Blocks(css=css, theme="soft", title="CAMEL 角色扮演对话数据合成s") as app:
    gr.HTML("""
    <div class="header">
        <h1>CAMEL角色扮演对话数据生成器</h1>
        <p>由 Llama 4 model提供超长上下文的支持 可基于超长上下文进行角色扮演对话数据生成 无rag机制更高质量生成数据</p>
    </div>
    """)
    
    with gr.Tabs() as tabs:
        with gr.Tab("📚 话题生成", elem_classes="tab-nav"):
            with gr.Box(elem_classes=["card"]):
                gr.HTML("<div class='panel-header'><h3>🔍 话题提取</h3></div>")
                
                with gr.Row():
                    with gr.Column(scale=3):
                        input_text = gr.Textbox(
                            label="输入文本", 
                            placeholder="输入文本内容以生成话题或上传TXT文件...",
                            lines=10,
                            elem_classes=["gr-textarea"]
                        )
                        
                        with gr.Row():
                            upload_file = gr.File(
                                label="上传TXT文件（文件内容优先）",
                                file_types=[".txt"],
                                type="binary",
                                elem_classes=["upload-btn"]
                            )
                        
                        with gr.Row():
                            num_topics = gr.Slider(
                                minimum=1, 
                                maximum=20, 
                                value=5, 
                                step=1, 
                                label="话题数量"
                            )
                            
                        generate_btn = gr.Button("✨ 生成话题", variant="primary", elem_classes=["gr-button-lg"])
                    
                    with gr.Column(scale=2):
                        topics_output = gr.Textbox(
                            label="生成的话题", 
                            lines=10,
                            elem_classes=["gr-textarea"],
                  
                        )
                        topics_file = gr.Textbox(
                            label="保存路径", 
                            visible=True, 
                            elem_classes=["gr-input"],
                       
                        )
                
                generate_btn.click(
                    generate_topics_interface,
                    inputs=[input_text, upload_file, num_topics],
                    outputs=[topics_output, topics_file]
                )
        
        with gr.Tab("💬 对话生成", elem_classes="tab-nav"):
            with gr.Box(elem_classes=["card"]):
                gr.HTML("<div class='panel-header'><h3>🎭 角色扮演对话创建</h3></div>")
                
                with gr.Row():
                    with gr.Column(scale=3):
                        selected_topics = gr.Textbox(
                            label="选定话题", 
                            placeholder="输入或粘贴来自话题生成器的话题（每行一个）...",
                            lines=5,
                            elem_classes=["gr-textarea"]
                        )
                        
                        gr.HTML("<div style='margin-top: 10px;'><b>对话上下文：</b></div>")
                        with gr.Row():
                            context_text = gr.Textbox(
                                label="上下文内容", 
                                placeholder="输入对话上下文或上传TXT文件...",
                                lines=5,
                                elem_classes=["gr-textarea"]
                            )
                        
                        with gr.Row():
                            context_file = gr.File(
                                label="上传上下文文件（文件内容优先）",
                                file_types=[".txt"],
                                type="binary",
                                elem_classes=["upload-btn"]
                            )
                        
                        gr.HTML("<div style='margin-top: 15px;'><b>角色设置：</b></div>")
                        with gr.Row():
                            with gr.Column(scale=1):
                                assistant_role = gr.Textbox(
                                    label="助手角色", 
                                    value="Python程序员", 
                                    placeholder="例如：数据科学家，厨师",
                                    elem_classes=["gr-input"]
                                )
                            with gr.Column(scale=1):
                                user_role = gr.Textbox(
                                    label="用户角色", 
                                    value="股票交易员", 
                                    placeholder="例如：客户，学生",
                                    elem_classes=["gr-input"]
                                )
                        
                        with gr.Row():
                            chat_turns = gr.Slider(
                                minimum=2, 
                                maximum=20, 
                                value=6, 
                                step=1, 
                                label="对话轮数"
                            )
                        
                        dialogue_btn = gr.Button("🔮 生成对话", variant="primary", elem_classes=["gr-button-lg"])
                
                with gr.Box(elem_classes=["card"]):
                    gr.HTML("<div class='panel-header'><h3>💎 生成结果</h3></div>")
                    
                    dialogue_output = gr.Textbox(
                        label="生成的对话", 
                        lines=20,
                        elem_classes=["gr-textarea"],
                   
                    )
                    
                    dialogue_dir = gr.Textbox(
                        label="保存目录", 
                        visible=True,
                        elem_classes=["gr-input"],
                   
                    )
                
                dialogue_btn.click(
                    generate_dialogue_interface,
                    inputs=[selected_topics, assistant_role, user_role, chat_turns, context_text, context_file],
                    outputs=[dialogue_output, dialogue_dir]
                )
    
    with gr.Box(elem_classes=["card"]):
        gr.HTML("<div class='panel-header'><h3>📝 使用说明</h3></div>")
        
        gr.HTML("""
        <div style="padding: 10px;">
            <ol>
                <li><b>话题生成</b>: 在"话题生成"标签页中，输入文本或上传TXT文件，设置话题数量，然后点击"生成话题"</li>
                <li><b>话题选择</b>: 将生成的话题复制到"对话生成"标签页的"选定话题"输入框中</li>
                <li><b>上下文内容</b>: 输入或上传对话上下文以提供对话背景</li>
                <li><b>角色设置</b>: 自定义助手和用户角色（例如"Python程序员"和"股票交易员"）</li>
                <li><b>对话生成</b>: 设置对话轮数，然后点击"生成对话"</li>
                <li><b>结果保存</b>: 生成的对话将显示并保存为JSON文件在指定目录中</li>
            </ol>
        </div>
        """)
    
    gr.HTML("""
    <div class="footer">
        <p>© 2025 CAMEL-AI.org. 保留所有权利</p>
        <p>由 Llama 4 和 CAMEL-AI 框架提供支持</p>
    </div>
    """)

if __name__ == "__main__":
    app.launch(share=True)
