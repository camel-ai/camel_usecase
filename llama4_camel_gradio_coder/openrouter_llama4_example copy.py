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

from camel.agents import ChatAgent
from camel.configs import OpenRouterConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.messages import BaseMessage




model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENROUTER,
    model_type=ModelType.OPENROUTER_LLAMA_4_SCOUT_FREE,
    model_config_dict=OpenRouterConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "你是一个擅长结合camel框架和gradio框架而制作可视化gradio应用的专家，请你参考你的历史记忆，来回答用户的问题"


# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)
# Read user message from a text file
with open("alldata/gradio_merge_output/merged.txt", "r", encoding="utf-8") as file:
    camel_demos_content = file.read()
gradio_docs = BaseMessage.make_assistant_message(
    role_name="CAMEL Assistant",
    content=camel_demos_content,
)
# Update the memory
camel_agent.record_message(gradio_docs)


# with open("alldata/camel_examples_output/split_output/merged01_part1.txt", "r", encoding="utf-8") as file:
#     camel_demos_content = file.read()
# camel_examples_01 = BaseMessage.make_assistant_message(
#     role_name="CAMEL Assistant",
#     content=camel_demos_content,
# )
# # Update the memory
# camel_agent.record_message(camel_examples_01)




# with open("alldata/camel_examples_output/split_output/merged01_part2.txt", "r", encoding="utf-8") as file:
#     camel_demos_content = file.read()
# camel_examples_02 = BaseMessage.make_assistant_message(
#     role_name="CAMEL Assistant",
#     content=camel_demos_content,
# )
# # Update the memory
# camel_agent.record_message(camel_examples_02)

while True:
    input_text = input("你的问题是什么")
    if input_text == "exit":
        break
    if input_text == "clear":
        # 清空记忆历史
        camel_agent.reset()
        continue
    # Get response information
    response = camel_agent.step(input_text)
    # print(response)
    print(camel_agent.memory.get_context())
    print(response.msgs[0].content)
