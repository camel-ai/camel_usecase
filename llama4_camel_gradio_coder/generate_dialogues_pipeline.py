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
import subprocess
from colorama import Fore, init

# 导入主题生成和对话生成模块
from llama4_data_gen.topic_generator import generate_topics, load_input_file, save_topics
from llama4_data_gen.roleplay_dialogue_generator import generate_dialogue, save_dialogue


def main():
    # 初始化colorama
    init()
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="生成主题并基于主题生成对话数据")
    parser.add_argument("--input_file", type=str, required=True, help="输入文件路径")
    parser.add_argument("--output_dir", type=str, default="generated_dialogues", help="输出对话的目录")
    parser.add_argument("--num_topics", type=int, default=10, help="生成的主题数量")
    parser.add_argument("--num_dialogues", type=int, default=1, help="每个主题生成的对话数量")
    parser.add_argument("--topic_type", type=str, default="编程项目", help="主题类型")
    parser.add_argument("--assistant_role", type=str, default="Python程序员", help="助手角色名称")
    parser.add_argument("--user_role", type=str, default="股票交易员", help="用户角色名称")
    parser.add_argument("--chat_turn_limit", type=int, default=50, help="对话轮次限制")
    parser.add_argument("--skip_topic_generation", action="store_true", help="跳过主题生成步骤，使用现有主题文件")
    parser.add_argument("--topics_file", type=str, default="generated_topics.txt", help="主题文件路径（如果跳过主题生成）")
    args = parser.parse_args()
    
    # 创建模型
    from camel.configs import OpenRouterConfig
    from camel.models import ModelFactory
    from camel.types import ModelPlatformType, ModelType
    
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENROUTER,
        model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
        model_config_dict=OpenRouterConfig(temperature=0.7).as_dict(),
    )
    
    # 步骤1：生成主题
    topics_file = args.topics_file
    if not args.skip_topic_generation:
        print(Fore.YELLOW + "步骤1：生成主题")
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
        save_topics(topics, topics_file)
        print(Fore.GREEN + f"成功生成 {len(topics)} 个主题！")
    else:
        print(Fore.YELLOW + f"跳过主题生成，使用现有主题文件: {topics_file}")
    
    # 步骤2：生成对话
    print(Fore.YELLOW + "\n步骤2：生成对话")
    # 加载主题
    from llama4_data_gen.roleplay_dialogue_generator import load_topics_from_file
    topics = load_topics_from_file(topics_file)
    print(Fore.YELLOW + f"已加载 {len(topics)} 个主题")
    
    # 为每个主题生成指定数量的对话
    for topic in topics:
        print(Fore.MAGENTA + f"\n开始生成主题 '{topic}' 的对话")
        for i in range(args.num_dialogues):
            print(Fore.CYAN + f"生成第 {i+1}/{args.num_dialogues} 个对话")
            dialogue = generate_dialogue(
                model=model,
                topic=topic,
                assistant_role=args.assistant_role,
                user_role=args.user_role,
                chat_turn_limit=args.chat_turn_limit
            )
            save_dialogue(dialogue, args.output_dir, topic, i+1)
    
    print(Fore.GREEN + "\n所有对话生成完成！")


if __name__ == "__main__":
    main() 