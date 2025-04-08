# 基于CAMEL框架的对话数据生成器

这个项目使用CAMEL框架的RolePlaying功能，基于指定的主题生成对话数据。它可以从文本文件中读取主题列表，并为每个主题生成指定数量的对话。

## 功能特点

- 从文本文件中读取主题列表
- 为每个主题生成指定数量的对话
- 自定义助手和用户角色
- 将生成的对话保存为JSON格式
- 支持设置对话轮次限制
- 支持基于输入文件自动生成主题
- 提供Gradio Web界面，方便用户操作

## 安装依赖

确保已安装所需的依赖项：

```bash
pip install camel-ai
pip install colorama
pip install "gradio>=4.44.1"  # 使用最新版本的Gradio
```

## 使用方法

### 方法1：使用Gradio Web界面（推荐）

启动Gradio应用程序：

```bash
python dialogue_generator_gradio_app.py
```

这将启动一个Web界面，您可以在其中：
- 输入文本内容
- 设置生成参数（主题数量、对话数量、角色等）
- 查看生成的主题和对话
- 浏览和查看生成的对话内容

### 方法2：使用集成脚本

集成脚本可以基于输入文件生成主题，然后基于这些主题生成对话数据：

```bash
python generate_dialogues_pipeline.py --input_file input_content.txt --num_topics 10 --num_dialogues 3 --output_dir generated_dialogues
```

#### 命令行参数

- `--input_file`：输入文件路径（必需）
- `--output_dir`：输出对话的目录（默认：`generated_dialogues`）
- `--num_topics`：生成的主题数量（默认：10）
- `--num_dialogues`：每个主题生成的对话数量（默认：1）
- `--topic_type`：主题类型（默认：`编程项目`）
- `--assistant_role`：助手角色名称（默认：`Python程序员`）
- `--user_role`：用户角色名称（默认：`股票交易员`）
- `--chat_turn_limit`：对话轮次限制（默认：50）
- `--skip_topic_generation`：跳过主题生成步骤，使用现有主题文件
- `--topics_file`：主题文件路径（如果跳过主题生成，默认：`generated_topics.txt`）

### 方法3：分步使用

#### 步骤1：生成主题

```bash
python topic_generator.py --input_file input_content.txt --num_topics 10 --output_file generated_topics.txt --topic_type "编程项目"
```

#### 步骤2：生成对话

```bash
python roleplay_dialogue_generator.py --topics_file generated_topics.txt --num_dialogues 3 --output_dir generated_dialogues
```

## 输出格式

生成的对话将保存为JSON文件，格式如下：

```json
{
  "topic": "开发一个股票市场交易机器人",
  "assistant_role": "Python程序员",
  "user_role": "股票交易员",
  "messages": [
    {
      "role": "system",
      "content": "最终任务提示..."
    },
    {
      "role": "assistant",
      "content": "助手回复内容..."
    },
    {
      "role": "user",
      "content": "用户回复内容..."
    },
    ...
  ]
}
```

## 注意事项

- 生成对话需要连接到OpenRouter API，请确保已正确配置API密钥
- 生成大量对话可能需要较长时间，请耐心等待
- 可以通过调整`chat_turn_limit`参数控制对话长度
- 主题生成和对话生成都使用了AI模型，结果可能会有一定的随机性
- Gradio应用程序使用临时目录存储生成的文件，关闭应用程序后文件将被删除