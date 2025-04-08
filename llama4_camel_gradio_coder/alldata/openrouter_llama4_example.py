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
    model_type=ModelType.OPENROUTER_LLAMA_4_MAVERICK_FREE,
    model_config_dict=OpenRouterConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."


# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)
# Read user message from a text file
with open("user_message.txt", "r", encoding="utf-8") as file:
    camel_demos_content = file.read()
new_user_msg = BaseMessage.make_user_message(
    role_name="CAMEL Assistant",
    content=camel_demos_content,
)
# Update the memory
camel_agent.record_message(new_user_msg)


# Get response information
response = camel_agent.step("总结一下代码")

print(camel_agent.memory.get_context())
print(response.msgs[0].content)
