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
    """Load topic list from file"""
    with open(file_path, "r", encoding="utf-8") as file:
        topics = [line.strip() for line in file if line.strip()]
    return topics


def load_context_from_file(file_path):
    """Load context from file"""
    with open(file_path, "r", encoding="utf-8") as file:
        context = file.read().strip()
    return context


def save_dialogue(dialogue, output_dir, topic, index):
    """Save dialogue to JSON file"""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{topic.replace(' ', '_')}_{index}_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(dialogue, f, ensure_ascii=False, indent=2)
    
    print(Fore.CYAN + f"Dialogue saved to: {filepath}")


def generate_dialogue(model, assistant_role, user_role, chat_turn_limit=50, context=None, topic=None):
    """Generate dialogue for a single topic"""
    dialogue = {
        "assistant_role": assistant_role,
        "user_role": user_role,
        "messages": []
    }
    try:
        # If context is provided, add it to the task prompt
        task_prompt = f"Converse based on the following content:\n\n{context}\n\nDialogue topic: {topic}"
        
        print(f"[generate_dialogue] Preparing to create RolePlaying instance, task prompt: {task_prompt[:100]}...")
        role_play_session = RolePlaying(
            assistant_role_name=assistant_role,
            assistant_agent_kwargs=dict(model=model),
            user_role_name=user_role,
            user_agent_kwargs=dict(model=model),
            task_prompt=task_prompt,
            with_task_specify=False,
        )
        print("[generate_dialogue] RolePlaying instance created successfully")

        print(
            Fore.GREEN
            + f"AI Assistant System Message:\n{role_play_session.assistant_sys_msg}\n"
        )
        print(
            Fore.BLUE + f"AI User System Message:\n{role_play_session.user_sys_msg}\n"
        )

        print(Fore.YELLOW + f"Original Task Prompt:\n{topic}\n")
        print(
            Fore.RED + f"Final Task Prompt:\n{role_play_session.task_prompt}\n"
        )

        # Reinitialize dialogue messages list
        dialogue["messages"] = []

        n = 0
        print("[generate_dialogue] Preparing to initialize chat")
        input_msg = role_play_session.init_chat()
        print("[generate_dialogue] Chat initialization completed, starting dialogue loop")
     
        
        while n < chat_turn_limit:
            n += 1
            print(f"[generate_dialogue] Dialogue turn {n}/{chat_turn_limit}")
            try:
                print(f"[generate_dialogue] Preparing to call role_play_session.step")
                assistant_response, user_response = role_play_session.step(input_msg)
                print(f"[generate_dialogue] role_play_session.step called successfully")

                # Record assistant response
                if assistant_response.msg and assistant_response.msg.content:
                    dialogue["messages"].append({
                        "role": "assistant",
                        "content": assistant_response.msg.content
                    })
                else:
                    print(f"[generate_dialogue] Warning: Assistant response is empty or has no content")
                
                # Record user response
                if user_response.msg and user_response.msg.content:
                    dialogue["messages"].append({
                        "role": "user",
                        "content": user_response.msg.content
                    })
                else:
                    print(f"[generate_dialogue] Warning: User response is empty or has no content")

                if assistant_response.terminated:
                    reason = assistant_response.info.get('termination_reasons', ['Unknown reason'])
                    print(
                        Fore.GREEN
                        + (
                            "AI Assistant terminated. Reason: "
                            f"{reason}."
                        )
                    )
                    dialogue["messages"].append({"role": "system", "content": f"AI Assistant terminated: {reason}"})
                    break
                if user_response.terminated:
                    reason = user_response.info.get('termination_reasons', ['Unknown reason'])
                    print(
                        Fore.GREEN
                        + (
                            "AI User terminated. "
                            f"Reason: {reason}."
                        )
                    )
                    dialogue["messages"].append({"role": "system", "content": f"AI User terminated: {reason}"})
                    break

                print_text_animated(
                    Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
                )
                print_text_animated(
                    Fore.GREEN + "AI Assistant:\n\n"
                    f"{assistant_response.msg.content}\n"
                )

                if "CAMEL_TASK_DONE" in user_response.msg.content:
                    print("[generate_dialogue] Detected CAMEL_TASK_DONE, ending dialogue")
                    break

                input_msg = assistant_response.msg
            except Exception as step_e:
                error_trace = traceback.format_exc()
                print(f"[generate_dialogue] Error during dialogue generation (turn {n}): {str(step_e)}\n{error_trace}")
                # Add an error message to the dialogue
                dialogue["messages"].append({
                    "role": "system",
                    "content": f"Error during dialogue generation (turn {n}): {str(step_e)}"
                })
                break
        
        print("[generate_dialogue] Dialogue generation loop ended")
        return dialogue
    except Exception as e:
        error_trace = traceback.format_exc()
        print(f"[generate_dialogue] Error creating or initializing dialogue: {str(e)}\n{error_trace}")
        # Return a dialogue structure containing error information
        dialogue["messages"].append({
            "role": "system",
            "content": f"Error creating or initializing dialogue: {str(e)}"
        })
        return dialogue


def main():
    # Initialize colorama
    init()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate dialogue data based on roleplay")
    parser.add_argument("--topics_file", type=str, required=True, help="Path to text file containing topic list")
    parser.add_argument("--output_dir", type=str, default="generated_dialogues", help="Output directory for dialogues")
    parser.add_argument("--num_dialogues", type=int, default=1, help="Number of dialogues to generate per topic")
    parser.add_argument("--assistant_role", type=str, default="Python Programmer", help="Assistant role name")
    parser.add_argument("--user_role", type=str, default="Stock Trader", help="User role name")
    parser.add_argument("--chat_turn_limit", type=int, default=6, help="Dialogue turn limit")
    parser.add_argument("--context", type=str, required=True, help="Context file path")
    args = parser.parse_args()
    
    # Create model
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENROUTER,
        model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
        model_config_dict=OpenRouterConfig(temperature=0.7).as_dict(),
    )
    
    # Load topics
    topics = load_topics_from_file(args.topics_file)
    print(Fore.YELLOW + f"Loaded {len(topics)} topics")

    context = load_context_from_file(args.context)
    
    # Generate specified number of dialogues for each topic
    for topic in topics:
        print(Fore.MAGENTA + f"\nStarting dialogue generation for topic '{topic}'")
        for i in range(args.num_dialogues):
            print(Fore.CYAN + f"Generating dialogue {i+1}/{args.num_dialogues}")
            dialogue = generate_dialogue(
                model=model,
                topic=topic,
                assistant_role=args.assistant_role,
                user_role=args.user_role,
                chat_turn_limit=args.chat_turn_limit,
                context=context
            )
            save_dialogue(dialogue, args.output_dir, topic, i+1)
    
    print(Fore.GREEN + "\nAll dialogues generated successfully!")


if __name__ == "__main__":
    main()