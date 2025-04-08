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
import traceback

from camel.societies import RolePlaying
from camel.utils import print_text_animated
from camel.agents import ChatAgent
from camel.configs import OpenRouterConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType


def load_topics_from_file(file_path):
    """从文件中加载主题列表"""
    with open(file_path, "r", encoding="utf-8") as file:
        topics = [line.strip() for line in file if line.strip()]
    return topics


def save_dialogue(dialogue, output_dir, topic, index):
    """保存对话到JSON文件"""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{topic.replace(' ', '_')}_{index}_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(dialogue, f, ensure_ascii=False, indent=2)
    
    print(Fore.CYAN + f"对话已保存到: {filepath}")


def generate_dialogue(model, topic, assistant_role, user_role, chat_turn_limit=50, context=None):
    """生成单个主题的对话"""
    dialogue = {
        "topic": topic,
        "assistant_role": assistant_role,
        "user_role": user_role,
        "messages": []
    }
    try:
        # 如果有上下文，将其添加到任务提示中
        task_prompt = topic
        if context:
            task_prompt = f"基于以下内容进行对话：\n\n{context}\n\n对话主题：{topic}"
        
        print(f"[generate_dialogue] 准备创建RolePlaying实例，任务提示: {task_prompt[:100]}...")
        role_play_session = RolePlaying(
            assistant_role_name=assistant_role,
            assistant_agent_kwargs=dict(model=model),
            user_role_name=user_role,
            user_agent_kwargs=dict(model=model),
            task_prompt=task_prompt,
            with_task_specify=False,
        )
        print("[generate_dialogue] RolePlaying实例创建成功")

        specified_task_prompt = getattr(role_play_session, 'specified_task_prompt', task_prompt)

        print(
            Fore.GREEN
            + f"AI助手系统消息:\n{role_play_session.assistant_sys_msg}\n"
        )
        print(
            Fore.BLUE + f"AI用户系统消息:\n{role_play_session.user_sys_msg}\n"
        )

        print(Fore.YELLOW + f"原始任务提示:\n{topic}\n")
        print(
            Fore.CYAN
            + "指定任务提示 (已禁用):"
            + f"\n{specified_task_prompt}\n"
        )
        print(Fore.RED + f"最终任务提示:\n{role_play_session.task_prompt}\n")

        # 重新初始化对话消息列表
        dialogue["messages"] = []

        n = 0
        print("[generate_dialogue] 准备初始化聊天")
        input_msg = role_play_session.init_chat()
        print("[generate_dialogue] 聊天初始化完成，开始对话循环")
        dialogue["messages"].append({
            "role": "system",
            "content": role_play_session.task_prompt
        })
        
        while n < chat_turn_limit:
            n += 1
            print(f"[generate_dialogue] 对话轮次 {n}/{chat_turn_limit}")
            try:
                print(f"[generate_dialogue] 准备调用 role_play_session.step")
                assistant_response, user_response = role_play_session.step(input_msg)
                print(f"[generate_dialogue] role_play_session.step 调用成功")

                # 记录助手回复
                if assistant_response.msg and assistant_response.msg.content:
                    dialogue["messages"].append({
                        "role": "assistant",
                        "content": assistant_response.msg.content
                    })
                else:
                    print(f"[generate_dialogue] 警告: 助手响应为空或无内容")
                
                # 记录用户回复
                if user_response.msg and user_response.msg.content:
                    dialogue["messages"].append({
                        "role": "user",
                        "content": user_response.msg.content
                    })
                else:
                    print(f"[generate_dialogue] 警告: 用户响应为空或无内容")

                if assistant_response.terminated:
                    reason = assistant_response.info.get('termination_reasons', ['未知原因'])
                    print(
                        Fore.GREEN
                        + (
                            "AI助手终止。原因: "
                            f"{reason}."
                        )
                    )
                    dialogue["messages"].append({"role": "system", "content": f"AI助手终止: {reason}"})
                    break
                if user_response.terminated:
                    reason = user_response.info.get('termination_reasons', ['未知原因'])
                    print(
                        Fore.GREEN
                        + (
                            "AI用户终止。"
                            f"原因: {reason}."
                        )
                    )
                    dialogue["messages"].append({"role": "system", "content": f"AI用户终止: {reason}"})
                    break

                print_text_animated(
                    Fore.BLUE + f"AI用户:\n\n{user_response.msg.content}\n"
                )
                print_text_animated(
                    Fore.GREEN + "AI助手:\n\n"
                    f"{assistant_response.msg.content}\n"
                )

                if "CAMEL_TASK_DONE" in user_response.msg.content:
                    print("[generate_dialogue] 检测到 CAMEL_TASK_DONE，结束对话")
                    break

                input_msg = assistant_response.msg
            except Exception as step_e:
                error_trace = traceback.format_exc()
                print(f"[generate_dialogue] 对话生成过程中出错 (轮次 {n}): {str(step_e)}\n{error_trace}")
                # 添加一个错误消息到对话中
                dialogue["messages"].append({
                    "role": "system",
                    "content": f"对话生成过程中出错 (轮次 {n}): {str(step_e)}"
                })
                break
        
        print("[generate_dialogue] 对话生成循环结束")
        return dialogue
    except Exception as e:
        error_trace = traceback.format_exc()
        print(f"[generate_dialogue] 创建或初始化对话时出错: {str(e)}\n{error_trace}")
        # 返回一个包含错误信息的对话结构
        dialogue["messages"].append({
            "role": "system",
            "content": f"创建或初始化对话时出错: {str(e)}"
        })
        return dialogue


def main():
    # 初始化colorama
    init()
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="基于roleplay生成对话数据")
    parser.add_argument("--topics_file", type=str, required=True, help="包含主题列表的文本文件路径")
    parser.add_argument("--output_dir", type=str, default="generated_dialogues", help="输出对话的目录")
    parser.add_argument("--num_dialogues", type=int, default=1, help="每个主题生成的对话数量")
    parser.add_argument("--assistant_role", type=str, default="Python程序员", help="助手角色名称")
    parser.add_argument("--user_role", type=str, default="股票交易员", help="用户角色名称")
    parser.add_argument("--chat_turn_limit", type=int, default=50, help="对话轮次限制")
    args = parser.parse_args()
    
    # 创建模型
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENROUTER,
        model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
        model_config_dict=OpenRouterConfig(temperature=0.7).as_dict(),
    )
    
    # 加载主题
    topics = load_topics_from_file(args.topics_file)
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