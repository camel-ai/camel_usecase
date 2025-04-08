# CAMEL Agent 知识库对话系统

这是一个基于CAMEL框架和Gradio的可视化应用，允许用户上传知识库文件并将其添加到CAMEL Agent的记忆中，然后进行对话。

## 功能特点

- 上传知识库文件（支持.txt格式）
- 将知识库内容添加到CAMEL Agent的记忆中
- 与CAMEL Agent进行对话
- 查看当前上下文
- 清除对话历史

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行应用

```bash
python gradio_camel_app.py
```

## 使用说明

1. 启动应用后，在左侧面板上传知识库文件（.txt格式）
2. 点击"上传知识库"按钮，将知识库内容添加到CAMEL Agent的记忆中
3. 在右侧面板的输入框中输入问题，点击"发送"按钮或按回车键发送消息
4. 查看CAMEL Agent的回复
5. 可以点击"查看当前上下文"按钮查看当前上下文
6. 可以点击"清除对话历史"按钮清除对话历史

## 技术栈

- CAMEL框架：用于创建和管理对话Agent
- Gradio：用于创建Web界面
- OpenRouter API：用于访问LLaMA 4模型

## 注意事项

- 上传的知识库文件必须是UTF-8编码的文本文件
- 知识库文件大小不应过大，以避免内存问题
- 需要有效的OpenRouter API密钥才能使用LLaMA 4模型