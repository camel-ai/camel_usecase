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
import argparse
import json
from datetime import datetime
from colorama import Fore, init

from camel.agents import ChatAgent
from camel.configs import OpenRouterConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.messages import BaseMessage


def load_input_file(file_path):
    """从文件中加载输入内容"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def save_topics(topics, output_file):
    """保存主题列表到文件"""
    with open(output_file, "w", encoding="utf-8") as f:
        for topic in topics:
            f.write(f"{topic}\n")
    
    print(Fore.CYAN + f"主题已保存到: {output_file}")


def generate_topics(model, input_content, num_topics=5, topic_type="编程项目"):
    """从输入内容生成主题列表"""
    system_message = f"""你是一个擅长从文本中提取主题的AI助手。
请根据提供的文本内容，生成{num_topics}个关于{topic_type}的主题。
主题应该简洁明了，每行一个，不要有编号或其他标记。"""

    # 创建聊天代理
    chat_agent = ChatAgent(system_message=system_message, model=model)
    
    # 消息内容
    message = f"""请根据以下内容，生成{num_topics}个关于{topic_type}的主题：

{input_content}

记住，只需提供主题列表，每行一个，不要有编号或其他标记。"""

    try:
        # 获取响应
        response = chat_agent.step(message)
        
        # 检查响应
        if not response.msgs or len(response.msgs) == 0:
            print("警告：模型返回了空响应")
            # 返回一个默认主题列表
            return [f"{topic_type} {i+1}" for i in range(num_topics)]
        
        # 解析主题
        topics_text = response.msgs[0].content
        topics = [line.strip() for line in topics_text.strip().split('\n') if line.strip()]
        
        # 确保我们有足够的主题
        if len(topics) < num_topics:
            # 如果主题不足，添加一些通用主题
            print(f"警告：生成的主题数量不足（{len(topics)} < {num_topics}）")
            for i in range(len(topics), num_topics):
                topics.append(f"{topic_type} {i+1}")
        
        # 如果主题太多，只取需要的数量
        topics = topics[:num_topics]
        
        return topics
    except Exception as e:
        print(f"生成主题时出错：{str(e)}")
        # 返回一个默认主题列表
        return [f"{topic_type} {i+1}" for i in range(num_topics)]


def main():
    # 初始化colorama
    init()
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="基于输入文件生成主题列表")
    parser.add_argument("--input_file", type=str, required=True, help="输入文件路径")
    parser.add_argument("--output_file", type=str, default="generated_topics.txt", help="输出主题文件路径")
    parser.add_argument("--num_topics", type=int, default=10, help="生成的主题数量")
    parser.add_argument("--topic_type", type=str, default="编程项目", help="主题类型")
    args = parser.parse_args()
    
    # 创建模型
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENROUTER,
        model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
        model_config_dict=OpenRouterConfig(temperature=0.7).as_dict(),
    )
    
    # 加载输入文件
    input_content = load_input_file(args.input_file)
    print(Fore.YELLOW + f"已加载输入文件: {args.input_file}")
    
    # 生成主题
    print(Fore.MAGENTA + f"开始生成 {args.num_topics} 个 {args.topic_type} 主题...")
    topics = generate_topics(
        model=model,
        input_content=input_content,
        num_topics=args.num_topics,
        topic_type=args.topic_type
    )
    
    # 保存主题
    save_topics(topics, args.output_file)
    print(Fore.GREEN + f"成功生成 {len(topics)} 个主题！")


if __name__ == "__main__":
    main() 