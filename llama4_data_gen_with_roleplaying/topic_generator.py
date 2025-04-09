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
    """Load input content from a file"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def save_topics(topics, output_file):
    """Save the list of topics to a file"""
    with open(output_file, "w", encoding="utf-8") as f:
        for topic in topics:
            f.write(f"{topic}\n")
    
    print(Fore.CYAN + f"Topics saved to: {output_file}")


def generate_topics(model, input_content, num_topics=5):
    """Generate a list of topics from the input content"""
    system_message = f"""You are an AI assistant skilled at extracting topics from text.
Based on the provided text content, generate {num_topics} highly relevant and diverse topics.
Topics should be concise and clear, one per line, without numbering or other markers."""

    # Create a chat agent
    chat_agent = ChatAgent(system_message=system_message, model=model)
    
    # Message content
    message = f"""Please generate {num_topics} highly relevant and diverse topics based on the following content:

{input_content}

Remember, just provide the list of topics, one per line, without numbering or other markers."""

    try:
        # Get the response
        response = chat_agent.step(message)
        
        # Check the response
        if not response.msgs or len(response.msgs) == 0:
            print("Warning: The model returned an empty response")
        
        
        # Parse the topics
        topics_text = response.msgs[0].content
        topics = [line.strip() for line in topics_text.strip().split('\n') if line.strip()]

        if len(topics) > num_topics:
            topics = topics[:num_topics]
        
        return topics
    except Exception as e:
        print(f"Error generating topics: {str(e)}")
        


def main():
    # Initialize colorama
    init()
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a list of topics based on an input file")
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input file")
    parser.add_argument("--output_file", type=str, default="generated_topics.txt", help="Path to the output topics file")
    parser.add_argument("--num_topics", type=int, default=10, help="Number of topics to generate")

    args = parser.parse_args()
    
    # Create the model
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENROUTER,
        model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
        model_config_dict=OpenRouterConfig(temperature=0.7).as_dict(),
    )
    
    # Load the input file
    input_content = load_input_file(args.input_file)
    print(Fore.YELLOW + f"Input file loaded: {args.input_file}")
    
    # Generate topics
    print(Fore.MAGENTA + f"Starting to generate {args.num_topics} topics...")
    topics = generate_topics(
        model=model,
        input_content=input_content,
        num_topics=args.num_topics,
     
    )
    
    # Save topics
    save_topics(topics, args.output_file)
    print(Fore.GREEN + f"Successfully generated {len(topics)} topics!")


if __name__ == "__main__":
    main()