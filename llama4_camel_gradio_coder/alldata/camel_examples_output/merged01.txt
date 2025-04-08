
================================================================================
# Files from: camel_examples
================================================================================


--------------------------------------------------------------------------------
# File: __init__.py
--------------------------------------------------------------------------------

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



--------------------------------------------------------------------------------
# File: agent\agent_step_with_reasoning.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

sys_msg = "You are a helpful assistant."
usr_msg = """Who is the best basketball player in the world? 
Tell about his career.
"""

openai_model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
)

openai_agent = ChatAgent(
    system_message=sys_msg,
    model=openai_model,
)


# 1st run: the ordinary response

response = openai_agent.step(usr_msg)
print(response.msgs[0].content)
# flake8: noqa: E501
"""
===============================================================================
Determining the "best" basketball player in the world is subjective and often depends on personal preferences, criteria, and the specific time frame being considered. As of the latest NBA season, players like LeBron James, Kevin Durant, Giannis Antetokounmpo, Stephen Curry, and Nikola Jokić are frequently mentioned in discussions about the best players due to their exceptional skills, achievements, and impact on the game. Each of these players brings unique strengths to the court, and opinions on who is the best can vary widely among fans and analysts.
===============================================================================
"""

# 2nd run: the response with thinking (agent choose the best candidate above the threshold)

response_with_think = openai_agent.step(
    usr_msg,
    reason_params=dict(
        choices=3,
        threshold=0.33,
    ),
)
print(response_with_think.msgs[0].content)
# flake8: noqa: E501
"""
===============================================================================
Let's start by identifying three potential candidates for the title of the best basketball player in the world. Here are three top candidates:

1. **LeBron James**: Known for his versatility, basketball IQ, and leadership on and off the court. LeBron has won multiple NBA championships and MVP awards.

2. **Kevin Durant**: Renowned for his scoring ability, shooting accuracy, and clutch performances. Durant has also won multiple NBA championships and MVP awards.

3. **Giannis Antetokounmpo**: Known for his athleticism, defensive prowess, and ability to dominate games. Giannis has won NBA championships and MVP awards as well.

Now, let's assign probabilities/credibilities to each choice:

- LeBron James: 0.4
- Kevin Durant: 0.3
- Giannis Antetokounmpo: 0.3

Since LeBron James has a probability/credibility greater than 0.33, I will continue with him.

### LeBron James' Career Overview

LeBron James, often regarded as one of the greatest basketball players of all time, began his NBA career in 2003 when he was drafted as the first overall pick by the Cleveland Cavaliers. Known for his exceptional athleticism, court vision, and versatility, LeBron quickly made an impact in the league.

Throughout his career, LeBron has played for the Cleveland Cavaliers, Miami Heat, and Los Angeles Lakers. He has won four NBA championships (two with the Miami Heat, one with the Cleveland Cavaliers, and one with the Los Angeles Lakers) and has been named NBA Finals MVP four times. LeBron is also a four-time NBA Most Valuable Player (MVP).

LeBron is known for his ability to play and defend multiple positions, his leadership on and off the court, and his contributions to the game beyond just scoring. He is also recognized for his philanthropic efforts and influence in social justice issues.

LeBron continues to play at a high level, consistently being a key player for his team and a significant figure in the NBA.
===============================================================================
"""

# 3rd run: the response with thinking (agent fails to choose the best candidate above the threshold, let the user decide)

response_with_think2 = openai_agent.step(
    usr_msg,
    reason_params=dict(
        choices=3,
        threshold=0.5,
    ),
)

print(response_with_think2.msgs[0].content)
# flake8: noqa: E501
"""
===============================================================================
Question: Who do you think is the best basketball player in the world? Here are the candidates and their probabilities: 
1. LeBron James (0.4): Known for his versatility, leadership, and consistent performance over the years. Multiple NBA championships and MVP awards.
2. Giannis Antetokounmpo (0.3): Known as the "Greek Freak," celebrated for his athleticism, defensive skills, and recent NBA championship win. Multiple MVP awards.
3. Stephen Curry (0.3): Renowned for his exceptional shooting ability, revolutionized the game with his three-point shooting. Multiple NBA championships and MVP awards.
Please choose one to continue with.
Your reply: 3
The user has chosen Stephen Curry as the best basketball player in the world. Let's talk about his career.

Stephen Curry, born on March 14, 1988, is an American professional basketball player for the Golden State Warriors of the National Basketball Association (NBA). Widely regarded as one of the greatest shooters in NBA history, Curry is credited with revolutionizing the game of basketball by inspiring teams to regularly utilize the three-point shot.

### Career Highlights:

1. **Early Life and College:**
   - Stephen Curry is the son of former NBA player Dell Curry. He played college basketball for the Davidson Wildcats, where he gained national attention for leading his team to the NCAA Tournament's Elite Eight in 2008.

2. **NBA Draft and Early Years:**
   - Curry was selected by the Golden State Warriors with the seventh overall pick in the 2009 NBA Draft. He quickly became known for his shooting prowess and playmaking ability.

3. **Rise to Stardom:**
   - Curry's breakout season came in 2014-2015 when he won his first NBA Most Valuable Player (MVP) award and led the Warriors to their first NBA Championship in 40 years.

4. **Record-Breaking Achievements:**
   - He set the record for most three-pointers made in a single season, a record he has broken multiple times. Curry's shooting range and accuracy have made him a central figure in the Warriors' success.

5. **Championships and MVP Awards:**
   - Stephen Curry has won four NBA Championships with the Warriors (2015, 2017, 2018, and 2022). He has been named NBA MVP twice (2015 and 2016), with the 2016 award being the first unanimous MVP in league history.

6. **Impact on the Game:**
   - Curry's influence extends beyond his statistics. He has changed how the game is played, with teams placing a greater emphasis on three-point shooting. His style of play has inspired a new generation of players.

7. **Continued Excellence:**
   - Even as he progresses in his career, Curry continues to perform at an elite level, contributing significantly to his team's success and maintaining his status as one of the top players in the league.

Stephen Curry's combination of skill, leadership, and impact on the game makes him a strong candidate for the best basketball player in the world today.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: agent\repo_agent.py
--------------------------------------------------------------------------------

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

from camel.agents import RepoAgent
from camel.embeddings import OpenAIEmbedding
from camel.retrievers import VectorRetriever
from camel.storages.vectordb_storages import QdrantStorage

vector_storage = QdrantStorage(
    vector_dim=OpenAIEmbedding().get_output_dim(),
    collection_name="tmp_collection",
    path="local_data/",
)

vr = VectorRetriever(embedding_model=OpenAIEmbedding(), storage=vector_storage)

repo_agent = RepoAgent(
    repo_paths=["https://github.com/camel-ai/camel"],
    chunk_size=8192,
    top_k=5,
    similarity=0.3,
    vector_retriever=vr,
    github_auth_token=os.getenv("GITHUB_AUTH_TOKEN"),
)

response = repo_agent.step("How to use a ChatAgent in CAMEL?")

print(response.msgs[0].content)

"""
Based on your request to learn how to use a `ChatAgent` in CAMEL, I will 
explain key aspects of the implementation provided in the source code 
"retrieved" and guide you on how to create and utilize the `ChatAgent` 
effectively.

### Overview of `ChatAgent`

`ChatAgent` is designed to interact with language models, supporting 
conversation management, memory, and tool integration. 
It can perform tasks like handling user queries, responding with structured 
data, and performing computations.

### Basic Usage of `ChatAgent`

Here's a step-by-step guide on how to implement and utilize a `ChatAgent`:

1. **Import Necessary Modules**:
   Ensure to import the relevant classes from the CAMEL library.

   ```python
   from camel.agents import ChatAgent
   ```

2. **Creating a `ChatAgent` Instance**:
   When you create an instance of `ChatAgent`, you can optionally pass a 
   `system_message` to define its role and behavior.

   ```python
   agent = ChatAgent(system_message="You are a helpful assistant.")
   ```

3. **Interacting with the Agent**:
   You can have a conversation by using the `step()` method, which allows you 
   to send messages and get responses.

   ```python
   user_message = "Hello, can you help me with a question?"
   response = agent.step(user_message)
   print(response.msgs[0].content)  # Print the agent's response
   ```

### Advanced Features

#### Integrating Tools

You can define tools (functions) that the agent can call during its operation.

```python
from camel.toolkits import FunctionTool

def calculator(a: int, b: int) -> int:
    return a + b

# Create ChatAgent with a tool
agent_with_tool = ChatAgent(tools=[calculator])
response = agent_with_tool.step("What is 2 + 2 using the calculator?")
```

#### Structured Output

You can specify structured outputs using Pydantic models to control the 
format of the response.

```python
from pydantic import BaseModel
from typing import List

class StructuredResponse(BaseModel):
    points: List[str]
    summary: str

agent = ChatAgent()
response = agent.step(
    "List benefits of exercise", response_format=StructuredResponse
)
```

### Example with a Specific Model

The code examples you provided also show how to specify and configure models 
used by `ChatAgent`. Here's how to create a `ChatAgent` with a custom model:

```python
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="gpt-3.5-turbo",  # Example model
    api_key="your_api_key",  # Ensure you have appropriate credentials
    model_config_dict={"temperature": 0.7}
)

camel_agent = ChatAgent(
    system_message="You are a helpful assistant.", model=model
)

user_message = "What are the best practices for using AI?"
response = camel_agent.step(user_message)
print(response.msgs[0].content)
```

### Conclusion

You can leverage `ChatAgent` in CAMEL to create powerful conversational agents 
that can perform a variety of tasks, integrate tools, and manage conversations 
effectively. The examples given demonstrate basic usage, tool integration, 
structured output formats, and model specification, allowing you to customize 
the behavior of your chat agent to suit your needs.

If you need more specific features or have other questions about the CAMEL 
framework, feel free to ask!

"""



--------------------------------------------------------------------------------
# File: ai_society\babyagi_playing.py
--------------------------------------------------------------------------------

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

from colorama import Fore

from camel.societies import BabyAGI
from camel.utils import print_text_animated


def main(model=None, chat_turn_limit=15) -> None:
    task_prompt = "Develop a trading bot for the stock market"
    babyagi_session = BabyAGI(
        assistant_role_name="Python Programmer",
        assistant_agent_kwargs=dict(model=model),
        user_role_name="Stock Trader",
        task_prompt=task_prompt,
        task_specify_agent_kwargs=dict(model=model),
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{babyagi_session.assistant_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + f"Specified task prompt:\n{babyagi_session.specified_task_prompt}\n"
    )
    print(
        Fore.RED
        + f"Final task prompt:\n{babyagi_session.specified_task_prompt}\n"
    )

    n = 0
    while n < chat_turn_limit:
        n += 1
        assistant_response = babyagi_session.step()
        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        print_text_animated(
            Fore.RED + "Task Name:\n\n"
            f"{assistant_response.info['task_name']}\n"
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n"
        )
        print_text_animated(
            Fore.BLUE + "Remaining Subtasks:\n\n"
            f"{assistant_response.info['subtasks'][:5]}\n"
        )


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: ai_society\generate_meta_data.py
--------------------------------------------------------------------------------

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
from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType


def main(key: str = "generate_users", num_roles: int = 50):
    prompt_template = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.AI_SOCIETY, key
    )
    prompt = prompt_template.format(num_roles=num_roles)
    print(prompt)
    agent = ChatAgent("You are a helpful assistant.")
    agent.reset()

    assistant_response = agent.step(prompt)
    if assistant_response.msgs is not None:
        print(assistant_response.msg.content)


if __name__ == "__main__":
    main("generate_users", 50)
    main("generate_assistants", 50)



--------------------------------------------------------------------------------
# File: ai_society\role_playing.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.societies import RolePlaying
from camel.utils import print_text_animated


def main(model=None, chat_turn_limit=50) -> None:
    task_prompt = "Develop a trading bot for the stock market"
    role_play_session = RolePlaying(
        assistant_role_name="Python Programmer",
        assistant_agent_kwargs=dict(model=model),
        user_role_name="Stock Trader",
        user_agent_kwargs=dict(model=model),
        task_prompt=task_prompt,
        with_task_specify=True,
        task_specify_agent_kwargs=dict(model=model),
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: ai_society\role_playing_multi_lingual.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.societies import RolePlaying
from camel.utils import print_text_animated


def main(model=None) -> None:
    task_prompt = "Develop a trading bot for the stock market"
    role_play_session = RolePlaying(
        assistant_role_name="Python Programmer",
        assistant_agent_kwargs=dict(model=model),
        user_role_name="Stock Trader",
        user_agent_kwargs=dict(model=model),
        task_prompt=task_prompt,
        with_task_specify=True,
        task_specify_agent_kwargs=dict(model=model),
        output_language="Chinese",  # Arabic, French, Spanish, ...
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    from camel.types import ModelType

    main(ModelType.GPT_4)



--------------------------------------------------------------------------------
# File: ai_society\role_playing_multiprocess.py
--------------------------------------------------------------------------------

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
import json
import multiprocessing
import os
import sys
from typing import Any, Dict

from colorama import Fore

from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType, TaskType
from camel.utils import download_tasks


def generate_data(
    assistant_idx: int,
    assistant_role_name: str,
    user_idx: int,
    user_role_name: str,
    task_idx: int,
    task_prompt: str,
    verbose: bool = False,
) -> None:
    max_num_messages = 40

    original_task_prompt = task_prompt.replace(f"{task_idx+1}. ", "")

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=ChatGPTConfig(temperature=1.4).as_dict(),
    )

    role_play_session = RolePlaying(
        assistant_role_name,
        user_role_name,
        task_prompt=original_task_prompt,
        with_task_specify=True,
        with_task_planner=False,
        task_specify_agent_kwargs=dict(model=model),
    )

    input_msg = role_play_session.init_chat()

    if verbose:
        print(
            Fore.GREEN + "AI Assistant sys message:\n"
            f"{role_play_session.assistant_sys_msg}\n"
        )
        print(
            Fore.BLUE
            + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
        )

        print(Fore.YELLOW + f"Original task prompt:\n{original_task_prompt}\n")
        print(
            Fore.CYAN + "Specified task prompt:\n"
            f"{role_play_session.specified_task_prompt}\n"
        )
        print(
            Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n"
        )

    message_counter = 0
    message_dict: Dict[str, Any] = {}

    assistant_agent = role_play_session.assistant_agent
    user_agent = role_play_session.user_agent

    # Append roles to the dictionary
    # We start number from 1 not 0.
    message_dict["role_1"] = (
        f"{assistant_role_name}_{assistant_agent.role_type!s}"
    )
    message_dict["role_2"] = f"{user_role_name}_{user_agent.role_type!s}"
    message_dict["id"] = (
        f"{(assistant_idx+1):03}_{(user_idx+1):03}_{(task_idx+1):03}"
    )
    message_dict["original_task"] = original_task_prompt
    message_dict["specified_task"] = role_play_session.specified_task_prompt

    # Threshold to terminate the conversation if no end token appears

    repeat_word_counter = 0
    repeat_word_threshold = 4
    repeat_word_list = [
        "goodbye",
        "good bye",
        "thank",
        "bye",
        "welcome",
        "language model",
    ]

    assistant_instruct_counter = 0
    assistant_instruct_threshold = 1
    assistant_instruct_word = "Instruction:"

    user_no_instruct_counter = 0
    user_no_instruct_threshold = 3
    user_no_instruct_word = "Instruction:"

    # Set max number of messages for the chat

    while message_counter < max_num_messages:
        assistant_response, user_response = role_play_session.step(input_msg)

        # Condition 1: User terminates the chat
        if user_response.terminated and user_response.info is not None:
            message_dict["termination_reason"] = (
                f"{user_agent.role_type!s}: "
                f"{user_response.info['termination_reasons'][0]}"
            )
            break

        # Condition 2: Assistant terminates the chat
        if (
            assistant_response.terminated
            and assistant_response.info is not None
        ):
            message_dict["termination_reason"] = (
                f"{assistant_agent.role_type!s}: "
                f"{assistant_response.info['termination_reasons'][0]}"
            )
            break

        assert (
            user_response.msg is not None
            and assistant_response.msg is not None
        )

        if verbose:
            print(f"User:\n{user_response.msg.content}\n")
            print(f"Assistant:\n{assistant_response.msg.content}\n")

        # Condition 3: Break if user does not give instruction
        if user_no_instruct_word not in user_response.msg.content:
            user_no_instruct_counter += 1
            if user_no_instruct_counter == user_no_instruct_threshold:
                message_dict['termination_reason'] = (
                    "user_no_instruct_threshold"
                )
                break
        else:
            user_no_instruct_counter = 0

        # Condition 4: Break if assistant gives instruction (flipped role)
        if assistant_instruct_word in assistant_response.msg.content:
            assistant_instruct_counter += 1
            if assistant_instruct_counter == assistant_instruct_threshold:
                message_dict['termination_reason'] = (
                    "assistant_instruct_threshold"
                )
                break
        else:
            assistant_instruct_counter = 0

        # Condition 5: Repeat word observed
        for repeat_word in repeat_word_list:
            if (
                repeat_word in user_response.msg.content.lower()
                or repeat_word in assistant_response.msg.content.lower()
            ):
                repeat_word_counter += 1
                if repeat_word_counter == repeat_word_threshold:
                    message_dict['termination_reason'] = (
                        "repeat_word_threshold"
                    )
                    break
            else:
                repeat_word_counter = 0

        # Save user message
        message_counter += 1
        message_dict[f"message_{message_counter}"] = (
            user_response.msg.to_dict()
        )

        # Condition 5: End token observed
        if "<CAMEL_TASK_DONE>" in user_response.msg.content:
            message_dict['termination_reason'] = "<CAMEL_TASK_DONE>"
            break

        # Save assistant message
        message_counter += 1
        message_dict[f"message_{message_counter}"] = (
            assistant_response.msg.to_dict()
        )

        input_msg = assistant_response.msg

    message_dict["num_messages"] = message_counter

    if message_dict["num_messages"] == max_num_messages:
        message_dict["termination_reason"] = "max_num_messages"

    with open(
        f"./camel_data/ai_society/{message_dict['id']}.json", "w"
    ) as json_file:
        json.dump(message_dict, json_file, ensure_ascii=False)


def generate_data_wrapper(args):
    try:
        generate_data(*args)
    except Exception as e:
        print(f"Error in generate_data: {e}", file=sys.stderr)


def main() -> None:
    # Disable/Enable Printing
    verbose = True

    # Check for tasks folder and install if not exists
    # Define the folder path
    folder_path = "./ai_society_data/"

    # Check if the folder already exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Check if the folder is empty
    if not os.listdir(folder_path):
        download_tasks(task=TaskType.AI_SOCIETY, folder_path=folder_path)

    # Chunk for parallel jobs
    try:
        slurm_array_task_id = os.environ.get('SLURM_ARRAY_TASK_ID')
        if slurm_array_task_id is None:
            raise
        array_idx = int(slurm_array_task_id)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        array_idx = 0

    roles_per_chunk = 10

    # Parameters for filtering the generated task string
    start_token = "1."
    num_tasks = 10

    with open("./data/ai_society/user_roles.txt", "r") as f:
        user_roles = f.read().splitlines()

    with open("./data/ai_society/assistant_roles.txt", "r") as f:
        assistant_roles = f.read().splitlines()

    assert (array_idx + 1) * roles_per_chunk <= len(assistant_roles)
    assistant_roles = assistant_roles[
        array_idx * roles_per_chunk : (array_idx + 1) * roles_per_chunk
    ]

    pool = multiprocessing.Pool()

    for assistant_idx, assistant_role_name in enumerate(assistant_roles):
        assistant_idx += array_idx * roles_per_chunk
        assistant_role_name = " ".join(assistant_role_name.split(" ")[1:])
        for user_idx, user_role_name in enumerate(user_roles):
            user_role_name = " ".join(user_role_name.split(" ")[1:])
            # Load the task list assigned for assistant and user roles
            with open(
                (
                    f"./ai_society_data/tasks/"
                    f"{assistant_role_name}_{user_role_name}.txt"
                ),
                "r",
            ) as f:
                tasks = f.read().splitlines()

                # Filter out the generated response to include the tasks only
                for i, task in enumerate(tasks):
                    if start_token in task:
                        tasks = tasks[i : i + num_tasks]
                        break

                # Ensure exact number of tasks is generated
                assert str(num_tasks) in tasks[-1], print(tasks)

            for task_idx, task_prompt in enumerate(tasks):
                id = (
                    f"{(assistant_idx+1):03}_"
                    f"{(user_idx+1):03}_{(task_idx+1):03}"
                )
                if not os.path.exists(f"./camel_data/ai_society/{id}.json"):
                    pool.apply_async(
                        generate_data_wrapper,
                        (
                            (
                                assistant_idx,
                                assistant_role_name,
                                user_idx,
                                user_role_name,
                                task_idx,
                                task_prompt,
                                verbose,
                            ),
                        ),
                    )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: ai_society\role_playing_with_critic.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main() -> None:
    task_prompt = "Write a research proposal for large-scale language models"
    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=ChatGPTConfig(temperature=0.8, n=3).as_dict(),
    )
    assistant_agent_kwargs = dict(model=model)
    user_agent_kwargs = dict(model=model)
    critic_kwargs = dict(verbose=True)
    role_play_session = RolePlaying(
        "PhD Student",
        "Postdoc",
        critic_role_name="Professor",
        task_prompt=task_prompt,
        with_task_specify=True,
        with_critic_in_the_loop=True,
        assistant_agent_kwargs=assistant_agent_kwargs,
        user_agent_kwargs=user_agent_kwargs,
        critic_kwargs=critic_kwargs,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )
    print(
        Fore.MAGENTA
        + f"Critic sys message:\n{role_play_session.critic_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + f"AI Assistant:\n\n{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: ai_society\role_playing_with_human.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main() -> None:
    task_prompt = "Write a book about the future of AI Society"
    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=ChatGPTConfig(temperature=1.4, n=3).as_dict(),
    )
    assistant_agent_kwargs = dict(model=model)
    user_agent_kwargs = dict(model=model)
    role_play_session = RolePlaying(
        "AGI",
        "Writer",
        critic_role_name="human",
        task_prompt=task_prompt,
        with_task_specify=True,
        with_critic_in_the_loop=True,
        assistant_agent_kwargs=assistant_agent_kwargs,
        user_agent_kwargs=user_agent_kwargs,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + f"AI Assistant:\n\n{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: ai_society\task_generation.py
--------------------------------------------------------------------------------

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
import multiprocessing
import os

from camel.agents import ChatAgent
from camel.generators import (
    AISocietyTaskPromptGenerator,
    SystemMessageGenerator,
)
from camel.messages import BaseMessage
from camel.types import RoleType, TaskType


def generate_tasks(
    role_names: str,
    task_generator_prompt: str,
    start_token: str = "1.",
    num_tasks: int = 10,
    model=None,
) -> None:
    sys_msg_generator = SystemMessageGenerator(task_type=TaskType.AI_SOCIETY)

    assistant_sys_msg = sys_msg_generator.from_dict(
        dict(), role_tuple=("Task Generator", RoleType.DEFAULT)
    )
    assistant_agent = ChatAgent(assistant_sys_msg, model=model)

    user_msg = BaseMessage.make_user_message(
        role_name="Task Generator", content=task_generator_prompt
    )

    assistant_response = assistant_agent.step(user_msg)

    if assistant_response.terminated or len(assistant_response.msgs) == 0:
        raise RuntimeError("Assistant agent terminated unexpectedly.")

    tasks = assistant_response.msg.content.split("\n")

    # Filter out the generated response to include the tasks only
    for i, task in enumerate(tasks):
        if start_token in task:
            tasks = tasks[i : i + num_tasks]
            break

    # Ensure exact number of tasks is generated
    assert str(num_tasks) in tasks[-1], print(tasks)

    with open(
        f"./ai_society_data/tasks/{'_'.join(role_names)}.txt", "w"
    ) as file:
        file.write("\n".join(tasks))


def main(model=None) -> None:
    num_tasks = 10
    start_token = "1."

    task_generator_prompt_generator = AISocietyTaskPromptGenerator(
        num_tasks=num_tasks
    ).from_role_files()

    pool = multiprocessing.Pool()

    for task_generator_prompt, role_names in task_generator_prompt_generator:
        if not os.path.exists(
            f"./ai_society_data/tasks/{'_'.join(role_names)}.txt"
        ):
            print(f"Generating tasks for {role_names}")
            pool.apply_async(
                generate_tasks,
                (
                    role_names,
                    task_generator_prompt,
                    start_token,
                    num_tasks,
                    model,
                ),
            )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: benchmarks\apibank.py
--------------------------------------------------------------------------------

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
from camel.benchmarks import APIBankBenchmark
from camel.benchmarks.apibank import Evaluator

# Set up the agent to be benchmarked
agent = ChatAgent()

# Set up the APIBench Benchmark
# Please note that the data_dir is predefined
# for better import management of the tools
benchmark = APIBankBenchmark(save_to="APIBankResults.jsonl")

# Download the benchmark data
benchmark.download()

# Set the subset to be benchmarked
level = 'level-1'

# NOTE: You might encounter the following error when
# running the benchmark in Windows:
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x81
# in position 130908: character maps to <undefined>
# To solve this issue, you can navigate to the file
# api_bank/tool_manager.py", line 30 and change the encoding
# with open(os.path.join(init_database_dir, file), 'r',
# encoding='utf-8') as f:


# Run the benchmark
result = benchmark.run(agent, level, api_test_enabled=True, subset=10)

# The following steps are only for demonstration purposes,
# they have been integrated into the run method of the benchmark.
# Get the first example of the test data
example_test = list(benchmark._data.items())[0]  # type: ignore[assignment] # noqa: RUF015
evaluator = Evaluator(example_test)
api_description = evaluator.get_api_description('ToolSearcher')
print('\nAPI description for ToolSearcher:\n', api_description)
'''
===============================================================================
API description for ToolSearcher:
 {"name": "ToolSearcher", "description": "Searches for relevant tools in 
 library based on the keywords.", "input_parameters": {"keywords": {"type": 
 "str", "description": "The keyword to search for."}}, 
 "output_parameters": 
 {"best_matchs": {"type": "Union[List[dict], dict]", 
 "description": "The best match tool(s)."}}}
===============================================================================
'''

# Print the final results
print("Total:", result["total"])
print("Correct:", result["correct"])
'''
===============================================================================
Total: 24
Correct: 10
===============================================================================
'''



--------------------------------------------------------------------------------
# File: benchmarks\apibench.py
--------------------------------------------------------------------------------

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
from camel.benchmarks import APIBenchBenchmark

# Set up the agent to be benchmarked
agent = ChatAgent()

# Set up the APIBench Benchmark
benchmark = APIBenchBenchmark(
    data_dir="APIBenchDatasets", save_to="APIBenchResults.jsonl"
)

# Download the benchmark data
benchmark.download()

# Set the subset to be benchmarked
subset_name = 'torchhub'

# Run the benchmark
result = benchmark.run(agent, subset_name, subset=10)

# Please note that APIBench does not use 'real function call'
# but instead includes API documentation in the questions
# for the agent to reference.
# An example question including the API documentation is printed below.
print(
    "\nExample question including API documentation:\n",
    benchmark._data['questions'][0]['text'],
)
'''
===============================================================================
Example question including API documentation:
  What is an API that can be used to classify sports activities in videos?\n
 Use this API documentation for reference:  
 {"domain": "Video Classification", "framework": "PyTorch", 
 "functionality": "3D ResNet", "api_name": "slow_r50", 
 "api_call": "torch.hub.load(repo_or_dir='facebookresearch/pytorchvideo', 
 model='slow_r50', pretrained=True)", "api_arguments": {"pretrained": "True"}, 
 "python_environment_requirements": ["torch", "json", "urllib", 
 "pytorchvideo", 
 "torchvision", "torchaudio", "torchtext", "torcharrow", "TorchData", 
 "TorchRec", "TorchServe", "PyTorch on XLA Devices"], 
 "example_code": ["import torch", 
 "model = torch.hub.load('facebookresearch/pytorchvideo', 
 'slow_r50', pretrained=True)", 
 "device = 'cpu'", "model = model.eval()", "model = model.to(device)"], 
 "performance": {"dataset": "Kinetics 400", 
 "accuracy": {"top_1": 74.58, "top_5": 91.63}, 
 "Flops (G)": 54.52, "Params (M)": 32.45}, 
 "description": "The 3D ResNet model is a Resnet-style video classification 
 network pretrained on the Kinetics 400 dataset. It is based on the 
 architecture from the paper 'SlowFast Networks for Video Recognition' 
 by Christoph Feichtenhofer et al."}}
===============================================================================
'''

print("Total:", result["total"])
print("Correct:", result["correct"])
print("Hallucination:", result["hallucination"])
'''
===============================================================================
Total: 10
Correct: 10
Hallucination: 0
===============================================================================
'''



--------------------------------------------------------------------------------
# File: benchmarks\gaia.py
--------------------------------------------------------------------------------

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
from camel.benchmarks import DefaultGAIARetriever, GAIABenchmark
from camel.models import ModelFactory
from camel.runtime import RemoteHttpRuntime
from camel.toolkits import CodeExecutionToolkit
from camel.types import ModelPlatformType, ModelType, StorageType

retriever = DefaultGAIARetriever(
    vector_storage_local_path="local_data2/", storage_type=StorageType.QDRANT
)

benchmark = GAIABenchmark(
    data_dir="datasets_test",
    processes=1,
    save_to="results.jsonl",
    retriever=retriever,
)

print(f"Number of validation examples: {len(benchmark.valid)}")
print(f"Number of test examples: {len(benchmark.test)}")


toolkit = CodeExecutionToolkit(verbose=True)
runtime = RemoteHttpRuntime("localhost").add(
    toolkit.get_tools(),
    "camel.toolkits.CodeExecutionToolkit",
)

task_prompt = """
        You are a general AI assistant. I will ask you a question. Report your
        thoughts, and finish your answer with the following template:
        FINAL ANSWER: [YOUR FINAL ANSWER].
        YOUR FINAL ANSWER should be a number OR as few words as possible OR a
        comma separated list of numbers and/or strings.
        If you are asked for a number, don't use comma to write your number
        neither use units such as $ or percent sign unless specified otherwise.
        If you are asked for a string, don't use articles, neither
        abbreviations (e.g. for cities), and write the digits in plain text
        unless specified otherwise.
        If you are asked for a comma separated list, apply the above rules
        depending of whether the element to be put in the list is a number or
        a string.
        """.strip()

tools = runtime.get_tools()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
)


agent = ChatAgent(
    task_prompt,
    model,
    tools=tools,
)

result = benchmark.run(agent, "valid", level="all", subset=3)
print("correct:", result["correct"])
print("total:", result["total"])

# ruff: noqa: E501
"""
Number of validation examples: 165
Number of test examples: 300
correct: 0
total: 3
"""



--------------------------------------------------------------------------------
# File: benchmarks\nexus.py
--------------------------------------------------------------------------------

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
from camel.benchmarks import NexusBenchmark
from camel.benchmarks.nexus import construct_tool_descriptions

# Set up the agent to be benchmarked
agent = ChatAgent()

# Set up the Nexusraven Function Calling Benchmark
benchmark = NexusBenchmark(
    data_dir="NexusDatasets", save_to="NexusResults.jsonl"
)

# Download the benchmark data
benchmark.download()

# Set the task (sub-dataset) to be benchmarked
task = "OTX"

# Please note that the following step is only for demonstration purposes,
# it has been integrated into the run method of the benchmark.
# The tools fetched here are used to construct the prompt for the task,
# which will be passed to the agent for response.
tools = construct_tool_descriptions(task)
print('\nTool descriptions for the task:\n', tools)
'''
===============================================================================
"""
Function:
def getIndicatorForIPv6(apiKey: str, ip: str, section: str):
"""

    Retrieves comprehensive information for a specific IPv6 address from the 
    AlienVault database. 
    This function allows you to obtain various types of data. 
    The 'general' section provides general information about the IP, 
    including geo data, and a list of other available sections. 
    'reputation' offers OTX data on malicious activity observed by 
    AlienVault Labs. 'geo' details more verbose geographic data such 
    as country code and coordinates. 'malware' reveals malware samples 
    connected to the IP, 
    and 'urlList' shows URLs associated with the IP. Lastly, 'passiveDns' 
    includes passive DNS information about hostnames/domains 
    pointing to this IP.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - ip: string, required, IPv6 address to query
    - section: string, required, Specific data section to retrieve 
    (options: general, reputation, geo, malware, urlList, passiveDns)

"""
Function:
def getIndicatorForDomain(apiKey: str, domain: str, section: str):
"""

    Retrieves a comprehensive overview for a given domain name from the 
    AlienVault database. This function provides various data types 
    about the domain. The 'general' section includes general information 
    about the domain, such as geo data, and lists of other available 
    sections. 'geo' provides detailed geographic data including country 
    code and coordinates. The 'malware' section indicates malware samples 
    associated with the domain. 'urlList' shows URLs linked to the domain,
    'passiveDns' details passive DNS information about hostnames/domains
    associated with the domain, 
    and 'whois' gives Whois records for the domain.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - domain: string, required, Domain address to query
    - section: string, required, Specific data section to retrieve 
    (options: general, geo, malware, urlList, passiveDns, whois)

"""
Function:
def getIndicatorForHostname(apiKey: str, hostname: str, section: str):
"""

    Retrieves detailed information for a specific hostname from the 
    AlienVault database. This function provides various data types about 
    the hostname. The 'general' section includes general information 
    about the IP, geo data, and lists of other available sections. 
    'geo' provides detailed geographic data including country code 
    and coordinates. The 'malware' section indicates malware samples 
    associated with the hostname. 'urlList' shows URLs linked to 
    the hostname, and 'passiveDns' details passive DNS information 
    about hostnames/domains associated with the hostname.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - hostname: string, required, Single hostname address to query
    - section: string, required, Specific data section to retrieve 
    (options: general, geo, malware, urlList, passiveDns)

"""
Function:
def getIndicatorForFileHashes(apiKey: str, fileHash: str, section: str):
"""

    Retrieves information related to a specific file hash from the 
    AlienVault database. 
    This function provides two types of data: 'general', 
    which includes general metadata about the file hash and a list of other 
    available sections for the hash; and 'analysis', which encompasses both 
    dynamic and static analysis of the file, 
    including Cuckoo analysis, exiftool, etc.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - fileHash: string, required, Single file hash to query
    - section: string, required, Specific data section to retrieve 
    (options: general, analysis)

"""
Function:
def getIndicatorForUrl(apiKey: str, url: str, section: str):
"""

    Retrieves information related to a specific URL from the AlienVault 
    database. This function offers two types of data: 'general', 
    which includes historical geographic information, 
    any pulses this indicator is on, 
    and a list of other available sections for this URL; and 'url_list', 
    which provides full results from AlienVault Labs URL analysis, 
    potentially including multiple entries.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - url: string, required, Single URL to query
    - section: string, required, Specific data section to retrieve 
    (options: general, url_list)

"""
Function:
def getIndicatorForCVE(apiKey: str, cve: str, section: str):
"""

    Retrieves information related to a specific CVE 
    (Common Vulnerability Enumeration)
    from the AlienVault database. This function offers detailed data on CVEs.
    The 'General' section includes MITRE CVE data, such as CPEs 
    (Common Platform Enumerations), 
    CWEs (Common Weakness Enumerations), and other relevant details. 
    It also provides information on any pulses this indicator is on, 
    and lists other sections currently available for this CVE.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - cve: string, required, Specific CVE identifier to query 
        (e.g., 'CVE-2014-0160')
    - section: string, required, Specific data section to retrieve 
        ('general' only)

"""
Function:
def getIndicatorForNIDS(apiKey: str, nids: str, section: str):
"""

    Retrieves metadata information for a specific 
    Network Intrusion Detection System (NIDS) 
    indicator from the AlienVault database. This function is designed to 
    provide general metadata about NIDS indicators.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - nids: string, required, Specific NIDS indicator to query 
        (e.g., '2820184')
    - section: string, required, Specific data section to retrieve 
        ('general' only)

"""
Function:
def getIndicatorForCorrelationRules(apiKey: str, correlationRule: str,
 section: str):
"""

    Retrieves metadata information related to a specific Correlation Rule from
    the AlienVault database. This function is designed to provide 
    general metadata about 
    Correlation Rules used in network security and event correlation. 
    Correlation Rules are crucial for identifying patterns and potential 
    security threats in network data.

    Args:
    - apiKey: string, required, Your AlienVault API key
    - correlationRule: string, required, Specific Correlation Rule 
    identifier to query (e.g., '572f8c3c540c6f0161677877')
    - section: string, required, Specific data section to retrieve 
    ('general' only)

"""
===============================================================================
'''

# Run the benchmark
result = benchmark.run(agent, task, subset=10)
print("Total:", result["total"])
print("Correct:", result["correct"])
'''
===============================================================================
Total: 10
Correct: 9
===============================================================================
'''



--------------------------------------------------------------------------------
# File: benchmarks\ragbench.py
--------------------------------------------------------------------------------

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
from camel.benchmarks import RAGBenchBenchmark
from camel.retrievers import AutoRetriever

assistant_sys_msg = """You are a helpful assistant to answer question,
         I will give you the Original Query and Retrieved Context,
        answer the Original Query based on the Retrieved Context,
        if you can't answer the question just say I don't know."""
agent = ChatAgent(assistant_sys_msg)
auto_retriever = AutoRetriever()

benchmark = RAGBenchBenchmark(subset="hotpotqa", split="test")
benchmark.download()
results = benchmark.run(agent, auto_retriever)
print(results)



--------------------------------------------------------------------------------
# File: bots\discord_bot.py
--------------------------------------------------------------------------------

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
import asyncio
from typing import TYPE_CHECKING, List, Optional, Union

from camel.agents import ChatAgent
from camel.bots import DiscordApp
from camel.retrievers import AutoRetriever
from camel.types import StorageType

try:
    from unstructured.documents.elements import Element
except ImportError:
    Element = None

if TYPE_CHECKING:
    from discord import Message


class BotAgent:
    def __init__(
        self,
        contents: Union[str, List[str], "Element", List["Element"]] = None,
        auto_retriever: Optional[AutoRetriever] = None,
        similarity_threshold: float = 0.5,
        vector_storage_local_path: str = "local_data/",
        top_k: int = 1,
        return_detailed_info: bool = True,
    ):
        r"""Initialize the BotAgent instance.

        Args:
            contents (Union[str, List[str], Element, List[Element]], optional)
                : The content to be retrieved.
            auto_retriever (Optional[AutoRetriever], optional): An instance of
                AutoRetriever for vector search.
            similarity_threshold (float): Threshold for vector similarity when
                retrieving content.
            vector_storage_local_path (str): Path to local vector storage for
                the retriever.
            top_k (int): Number of top results to retrieve.
            return_detailed_info (bool): Whether to return detailed
                information from the retriever.
        """

        assistant_sys_msg = '''
            Objective: 
                You are a customer service bot designed to assist users
                with inquiries related to our open-source project. 
                Your responses should be informative, concise, and helpful.

            Instructions:
                Understand User Queries: Carefully read and understand the
                        user's question. Focus on keywords and context to
                        determine the user's intent.
                Search for Relevant Information: Use the provided dataset
                        and refer to the RAG (file to find answers that 
                        closely match the user's query. The RAG file 
                        contains detailed interactions and should be your 
                        primary resource for crafting responses.
                Provide Clear and Concise Responses: Your answers should 
                        be clear and to the point. Avoid overly technical
                        language unless the user's query indicates 
                        familiarity with technical terms.
                Encourage Engagement: Where applicable, encourage users
                        to contribute to the project or seek further
                        assistance.

            Response Structure:
                Greeting: Begin with a polite greeting or acknowledgment.
                Main Response: Provide the main answer to the user's query.
                Additional Information: Offer any extra tips or direct the
                        user to additional resources if necessary.
                Closing: Close the response politely, encouraging
                        further engagement if appropriate.
            bd
            Tone:
                Professional: Maintain a professional tone that 
                        instills confidence in the user.
                Friendly: Be approachable and friendly to make users 
                        feel comfortable.
                Helpful: Always aim to be as helpful as possible,
                        guiding users to solutions.        
        '''

        self._agent = ChatAgent(
            assistant_sys_msg,
        )

        self._auto_retriever = None
        self._contents = contents
        self._top_k = top_k
        self._similarity_threshold = similarity_threshold
        self._return_detailed_info = return_detailed_info

        self._auto_retriever = auto_retriever or AutoRetriever(
            vector_storage_local_path=vector_storage_local_path,
            storage_type=StorageType.QDRANT,
        )

    async def process(self, message: str) -> str:
        r"""Process the user message, retrieve relevant content, and generate
        a response.

        Args:
            message (str): The user's query message.

        Returns:
            str: The assistant's response message.
        """
        user_raw_msg = message
        print("User message:", user_raw_msg)
        if self._auto_retriever:
            retrieved_content = self._auto_retriever.run_vector_retriever(
                query=user_raw_msg,
                contents=self._contents,
                top_k=self._top_k,
                similarity_threshold=self._similarity_threshold,
                return_detailed_info=self._return_detailed_info,
            )
            user_raw_msg = (
                f"Here is the query to you: {user_raw_msg}\n"
                f"Based on the retrieved content: {retrieved_content}, \n"
                f"answer the query"
            )

        assistant_response = self._agent.step(user_raw_msg)
        return assistant_response.msg.content


class DiscordBot(DiscordApp):
    def __init__(
        self,
        agent: BotAgent,
        token: Optional[str] = None,
        channel_ids: Optional[list[int]] = None,
    ):
        r"""Initializes the DiscordBot instance to handle Discord messages and
        communicate with BotAgent.

        Args:
            agent (BotAgent): The BotAgent responsible for processing messages
                and generating responses.
            token (Optional[str]): The token used to authenticate the bot with
                Discord.
            channel_ids (Optional[list[int]]): A list of Discord channel IDs
                where the bot is allowed to interact.
        """
        super().__init__(token=token, channel_ids=channel_ids)
        self.agent: BotAgent = agent

    async def on_message(self, message: 'Message') -> None:
        r"""Event handler for received messages. This method processes incoming
        messages, checks whether the message is from the bot itself, and
        determines whether the bot should respond based on channel ID and
        mentions. Then processes the message using the BotAgent, and responds.

        Args:
            message (discord.Message): The received message object.
        """
        # If the message author is the bot itself,
        # do not respond to this message
        if message.author == self._client.user:
            return

        # If allowed channel IDs are provided,
        # only respond to messages in those channels
        if self.channel_ids and message.channel.id not in self.channel_ids:
            return

        # Only respond to messages that mention the bot
        if not self._client.user or not self._client.user.mentioned_in(
            message
        ):
            return

        user_raw_msg = message.content
        response = await self.agent.process(user_raw_msg)
        await message.channel.send(response)


async def process_message(agent: BotAgent, msg_queue: asyncio.Queue):
    r"""Continuously processes messages from the queue and sends responses.

    This function waits for new messages in the queue, processes each message
    using the `BotAgent` instance, and sends the response back to Discord.

    Args:
        agent (BotAgent): An instance of `BotAgent` that processes the received
            messages.
        msg_queue (asyncio.Queue): The queue from which messages are retrieved
            for processing.
    """
    while True:
        message: "Message" = await msg_queue.get()
        user_raw_msg = message.content

        # Process the message using the agent and get the response
        response = await agent.process(user_raw_msg)
        # message.reply(response)
        await message.channel.send(response)
        msg_queue.task_done()


async def main():
    agent = BotAgent()

    # Initialize the DiscordBot with the message queue
    discord_bot = DiscordBot(agent=agent)

    await discord_bot.start()


if __name__ == "__main__":
    asyncio.run(main())



--------------------------------------------------------------------------------
# File: bots\discord_bot_installation_management.py
--------------------------------------------------------------------------------

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
import asyncio
import os

import uvicorn
from discord import Message
from starlette.responses import RedirectResponse

from camel.bots.discord import DiscordApp, DiscordSQLiteInstallationStore


class DiscordBot(DiscordApp):
    async def on_message(self, message: 'Message') -> None:
        if message.author == self._client.user:
            return

        if self.channel_ids and message.channel.id not in self.channel_ids:
            return

        if not self._client.user or not self._client.user.mentioned_in(
            message
        ):
            return

        installation = await self.installation_store.find_by_guild(
            str(message.guild.id)
        )
        if installation:
            await message.channel.send("Found installation.")
        else:
            await message.channel.send("No installation found for this guild.")


async def main():
    installation_store = DiscordSQLiteInstallationStore(
        database="./discord_installations.db"
    )
    await installation_store.init()

    discord_bot = DiscordBot(
        token=os.getenv("DISCORD_BOT_TOKEN"),
        client_id=os.getenv("DISCORD_BOT_CLIENT_ID"),
        client_secret=os.getenv("DISCORD_BOT_CLIENT_SECRET"),
        redirect_uri=os.getenv("DISCORD_BOT_REDIRECT_URL"),
        installation_store=installation_store,
    )

    @discord_bot.app.get(os.getenv("DISCORD_BOT_REDIRECT_URI"))
    async def oauth_redirect(code: str, guild_id: str):
        if not code:
            return {"error": "No code provided"}

        response = await discord_bot.exchange_code_for_token_response(code)
        if not response:
            return {"error": "Failed to obtain access token"}

        access_token = response.get("access_token")
        refresh_token = response.get("refresh_token")
        expires_in = response.get("expires_in")

        await discord_bot.save_installation(
            guild_id, access_token, refresh_token, expires_in
        )
        return RedirectResponse(url=f"https://discord.com/channels/{guild_id}")

    server_task = asyncio.create_task(
        uvicorn.Server(
            uvicorn.Config(discord_bot.app, host="0.0.0.0", port=8000)
        ).serve()
    )

    bot_task = asyncio.create_task(discord_bot.start())

    await asyncio.gather(server_task, bot_task)


if __name__ == "__main__":
    asyncio.run(main())



--------------------------------------------------------------------------------
# File: bots\discord_bot_use_msg_queue.py
--------------------------------------------------------------------------------

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
import asyncio
from typing import TYPE_CHECKING, List, Optional, Union

from camel.agents import ChatAgent
from camel.bots import DiscordApp
from camel.retrievers import AutoRetriever
from camel.types import StorageType

if TYPE_CHECKING:
    from discord import Message
    from unstructured.documents.elements import Element


class BotAgent:
    def __init__(
        self,
        contents: Union[str, List[str], "Element", List["Element"]] = None,
        auto_retriever: Optional[AutoRetriever] = None,
        similarity_threshold: float = 0.5,
        vector_storage_local_path: str = "local_data/",
        top_k: int = 1,
        return_detailed_info: bool = True,
    ):
        r"""Initialize the BotAgent instance.

        Args:
            contents (Union[str, List[str], Element, List[Element]], optional)
                : The content to be retrieved.
            auto_retriever (Optional[AutoRetriever], optional): An instance of
                AutoRetriever for vector search.
            similarity_threshold (float): Threshold for vector similarity when
                retrieving content.
            vector_storage_local_path (str): Path to local vector storage for
                the retriever.
            top_k (int): Number of top results to retrieve.
            return_detailed_info (bool): Whether to return detailed
                information from the retriever.
        """

        assistant_sys_msg = '''
            Objective: 
                You are a customer service bot designed to assist users
                with inquiries related to our open-source project. 
                Your responses should be informative, concise, and helpful.

            Instructions:
                Understand User Queries: Carefully read and understand the
                        user's question. Focus on keywords and context to
                        determine the user's intent.
                Search for Relevant Information: Use the provided dataset
                        and refer to the RAG (file to find answers that 
                        closely match the user's query. The RAG file 
                        contains detailed interactions and should be your 
                        primary resource for crafting responses.
                Provide Clear and Concise Responses: Your answers should 
                        be clear and to the point. Avoid overly technical
                        language unless the user's query indicates 
                        familiarity with technical terms.
                Encourage Engagement: Where applicable, encourage users
                        to contribute to the project or seek further
                        assistance.

            Response Structure:
                Greeting: Begin with a polite greeting or acknowledgment.
                Main Response: Provide the main answer to the user's query.
                Additional Information: Offer any extra tips or direct the
                        user to additional resources if necessary.
                Closing: Close the response politely, encouraging
                        further engagement if appropriate.
            bd
            Tone:
                Professional: Maintain a professional tone that 
                        instills confidence in the user.
                Friendly: Be approachable and friendly to make users 
                        feel comfortable.
                Helpful: Always aim to be as helpful as possible,
                        guiding users to solutions.        
        '''

        self._agent = ChatAgent(
            assistant_sys_msg,
        )

        self._auto_retriever = None
        self._contents = contents
        self._top_k = top_k
        self._similarity_threshold = similarity_threshold
        self._return_detailed_info = return_detailed_info

        self._auto_retriever = auto_retriever or AutoRetriever(
            vector_storage_local_path=vector_storage_local_path,
            storage_type=StorageType.QDRANT,
        )

    async def process(self, message: str) -> str:
        r"""Process the user message, retrieve relevant content, and generate
        a response.

        Args:
            message (str): The user's query message.

        Returns:
            str: The assistant's response message.
        """
        user_raw_msg = message
        print("User message:", user_raw_msg)
        if self._auto_retriever:
            retrieved_content = self._auto_retriever.run_vector_retriever(
                query=user_raw_msg,
                contents=self._contents,
                top_k=self._top_k,
                similarity_threshold=self._similarity_threshold,
                return_detailed_info=self._return_detailed_info,
            )
            user_raw_msg = (
                f"Here is the query to you: {user_raw_msg}\n"
                f"Based on the retrieved content: {retrieved_content}, \n"
                f"answer the query"
            )

        assistant_response = self._agent.step(user_raw_msg)
        return assistant_response.msg.content


class DiscordBot(DiscordApp):
    r"""A Discord bot that listens for messages, adds them to a queue,
    and processes them asynchronously.

    This class extends the functionality of `DiscordApp` and adds message
    handling by pushing messages into a queue for further processing.

    Args:
        msg_queue (asyncio.Queue): A queue used to store incoming messages for
            processing.
        token (Optional[str]): The token used to authenticate the bot with
            Discord.
        channel_ids (Optional[list[int]]): A list of Discord channel IDs where
            the bot is allowed to interact.
    """

    def __init__(
        self,
        msg_queue: asyncio.Queue,
        token: Optional[str] = None,
        channel_ids: Optional[list[int]] = None,
    ):
        super().__init__(token=token, channel_ids=channel_ids)
        self._queue: asyncio.Queue = msg_queue

    async def on_message(self, message: 'Message') -> None:
        r"""Event handler for received messages. This method processes incoming
        messages, checks whether the message is from the bot itself, and
        determines whether the bot should respond based on channel ID and
        mentions.

        Args:
            message (discord.Message): The received message object.
        """
        # If the message author is the bot itself,
        # do not respond to this message
        if message.author == self._client.user:
            return

        # If allowed channel IDs are provided,
        # only respond to messages in those channels
        if self.channel_ids and message.channel.id not in self.channel_ids:
            return

        # Only respond to messages that mention the bot
        if not self._client.user or not self._client.user.mentioned_in(
            message
        ):
            return

        await self._queue.put(message)


async def process_message(agent: BotAgent, msg_queue: asyncio.Queue):
    r"""Continuously processes messages from the queue and sends responses.

    This function waits for new messages in the queue, processes each message
    using the `BotAgent` instance, and sends the response back to Discord.

    Args:
        agent (BotAgent): An instance of `BotAgent` that processes the received
            messages.
        msg_queue (asyncio.Queue): The queue from which messages are retrieved
            for processing.
    """
    while True:
        message: "Message" = await msg_queue.get()
        user_raw_msg = message.content

        # Process the message using the agent and get the response
        response = await agent.process(user_raw_msg)
        # message.reply(response)
        await message.channel.send(response)
        msg_queue.task_done()


async def main():
    r"""Main function to initialize and run the Discord bot and message
    processor.

    This function initializes the message queue, creates an `BotAgent` instance
    for processing messages, and starts both the Discord bot and the
    message-processing loop asynchronously.
    """
    msg_queue = asyncio.Queue()

    agent = BotAgent()

    # Initialize the DiscordBot with the message queue
    discord_bot = DiscordBot(msg_queue=msg_queue)
    await asyncio.gather(
        discord_bot.start(), process_message(agent, msg_queue)
    )


if __name__ == "__main__":
    asyncio.run(main())



--------------------------------------------------------------------------------
# File: bots\slack_bot.py
--------------------------------------------------------------------------------

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
import logging
from typing import TYPE_CHECKING, List, Optional, Union

from slack_bolt.context.async_context import AsyncBoltContext
from slack_bolt.context.say.async_say import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient

from camel.agents import ChatAgent
from camel.bots import SlackApp, SlackEventBody
from camel.retrievers import AutoRetriever
from camel.types import StorageType

if TYPE_CHECKING:
    from unstructured.documents.elements import Element

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BotAgent:
    def __init__(
        self,
        contents: Union[str, List[str], "Element", List["Element"]] = None,
        auto_retriever: Optional[AutoRetriever] = None,
        similarity_threshold: float = 0.5,
        vector_storage_local_path: str = "local_data/",
        top_k: int = 1,
        return_detailed_info: bool = True,
    ):
        r"""Initialize the BotAgent instance.

        Args:
            contents (Union[str, List[str], Element, List[Element]], optional)
                : The content to be retrieved.
            auto_retriever (Optional[AutoRetriever], optional): An instance of
                AutoRetriever for vector search.
            similarity_threshold (float): Threshold for vector similarity when
                retrieving content.
            vector_storage_local_path (str): Path to local vector storage for
                the retriever.
            top_k (int): Number of top results to retrieve.
            return_detailed_info (bool): Whether to return detailed
                information from the retriever.
        """

        content = '''
            Objective: 
                You are a customer service bot designed to assist users
                with inquiries related to our open-source project. 
                Your responses should be informative, concise, and helpful.

            Instructions:
                Understand User Queries: Carefully read and understand the
                        user's question. Focus on keywords and context to
                        determine the user's intent.
                Search for Relevant Information: Use the provided dataset
                        and refer to the RAG (file to find answers that 
                        closely match the user's query. The RAG file 
                        contains detailed interactions and should be your 
                        primary resource for crafting responses.
                Provide Clear and Concise Responses: Your answers should 
                        be clear and to the point. Avoid overly technical
                        language unless the user's query indicates 
                        familiarity with technical terms.
                Encourage Engagement: Where applicable, encourage users
                        to contribute to the project or seek further
                        assistance.

            Response Structure:
                Greeting: Begin with a polite greeting or acknowledgment.
                Main Response: Provide the main answer to the user's query.
                Additional Information: Offer any extra tips or direct the
                        user to additional resources if necessary.
                Closing: Close the response politely, encouraging
                        further engagement if appropriate.
            bd
            Tone:
                Professional: Maintain a professional tone that 
                        instills confidence in the user.
                Friendly: Be approachable and friendly to make users 
                        feel comfortable.
                Helpful: Always aim to be as helpful as possible,
                        guiding users to solutions.        
        '''

        self._agent = ChatAgent(
            content,
        )

        self._auto_retriever = None
        self._contents = contents
        self._top_k = top_k
        self._similarity_threshold = similarity_threshold
        self._return_detailed_info = return_detailed_info

        self._auto_retriever = auto_retriever or AutoRetriever(
            vector_storage_local_path=vector_storage_local_path,
            storage_type=StorageType.QDRANT,
        )

    async def process(self, message: str) -> str:
        user_raw_msg = message
        logger.info("User message:", user_raw_msg)
        if self._auto_retriever:
            retrieved_content = self._auto_retriever.run_vector_retriever(
                query=user_raw_msg,
                contents=self._contents,
                top_k=self._top_k,
                similarity_threshold=self._similarity_threshold,
                return_detailed_info=self._return_detailed_info,
            )
            user_raw_msg = (
                f"Here is the query to you: {user_raw_msg}\n"
                f"Based on the retrieved content: {retrieved_content}, \n"
                f"answer the query"
            )

        assistant_response = self._agent.step(user_raw_msg)
        return assistant_response.msg.content


class SlackBot(SlackApp):
    def __init__(
        self,
        agent: BotAgent,
        token: Optional[str] = None,
        scopes: Optional[str] = None,
        signing_secret: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        """Initializes the SlackBot instance to handle Slack messages and
        communicate with BotAgent.

        Args:
            agent (BotAgent): The BotAgent responsible for processing messages
                and generating responses.
            token (Optional[str]): Slack API token for authentication.
            scopes (Optional[str]): Slack app scopes for permissions.
            signing_secret (Optional[str]): Signing secret for verifying Slack
                requests.
            client_id (Optional[str]): Slack app client ID.
            client_secret (Optional[str]): Slack app client secret.
        """
        super().__init__(
            token=token,
            scopes=scopes,
            signing_secret=signing_secret,
            client_id=client_id,
            client_secret=client_secret,
        )
        self.agent: BotAgent = agent

    async def on_message(
        self,
        context: "AsyncBoltContext",
        client: "AsyncWebClient",
        event: dict,
        body: dict,
        say: "AsyncSay",
    ):
        """Handles incoming Slack messages, processes them with BotAgent, and
        responds.

        Args:
            context (AsyncBoltContext): Context object that contains
                information about the Slack event.
            client (AsyncWebClient): Slack Web API client for making API
                requests.
            event (dict): Event data containing details of the incoming Slack
                message.
            body (dict): Full request body from Slack.
            say (AsyncSay): A function to send a response back to the Slack
                channel.
        """
        await context.ack()
        event_body = SlackEventBody(**body)
        user_raw_msg = event_body.event.text
        response = await agent.process(user_raw_msg)
        await say(response)


if __name__ == "__main__":
    agent = BotAgent()

    slack_bot = SlackBot(agent=agent)
    slack_bot.run(3000)



--------------------------------------------------------------------------------
# File: bots\slack_bot_use_msg_queue.py
--------------------------------------------------------------------------------

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
import asyncio
import logging
import queue
import threading
from typing import TYPE_CHECKING, List, Optional, Union

from slack_bolt.context.async_context import AsyncBoltContext
from slack_bolt.context.say.async_say import AsyncSay
from slack_sdk.web.async_client import AsyncWebClient

from camel.agents import ChatAgent
from camel.bots import SlackApp, SlackEventBody
from camel.retrievers import AutoRetriever
from camel.types import StorageType

if TYPE_CHECKING:
    from unstructured.documents.elements import Element

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BotAgent:
    def __init__(
        self,
        contents: Union[str, List[str], "Element", List["Element"]] = None,
        auto_retriever: Optional[AutoRetriever] = None,
        similarity_threshold: float = 0.5,
        vector_storage_local_path: str = "local_data/",
        top_k: int = 1,
        return_detailed_info: bool = True,
    ):
        r"""Initialize the BotAgent instance.

        Args:
            contents (Union[str, List[str], Element, List[Element]], optional)
                : The content to be retrieved.
            auto_retriever (Optional[AutoRetriever], optional): An instance of
                AutoRetriever for vector search.
            similarity_threshold (float): Threshold for vector similarity when
                retrieving content.
            vector_storage_local_path (str): Path to local vector storage for
                the retriever.
            top_k (int): Number of top results to retrieve.
            return_detailed_info (bool): Whether to return detailed
                information from the retriever.
        """

        assistant_sys_msg = '''
            Objective: 
                You are a customer service bot designed to assist users
                with inquiries related to our open-source project. 
                Your responses should be informative, concise, and helpful.

            Instructions:
                Understand User Queries: Carefully read and understand the
                        user's question. Focus on keywords and context to
                        determine the user's intent.
                Search for Relevant Information: Use the provided dataset
                        and refer to the RAG (file to find answers that 
                        closely match the user's query. The RAG file 
                        contains detailed interactions and should be your 
                        primary resource for crafting responses.
                Provide Clear and Concise Responses: Your answers should 
                        be clear and to the point. Avoid overly technical
                        language unless the user's query indicates 
                        familiarity with technical terms.
                Encourage Engagement: Where applicable, encourage users
                        to contribute to the project or seek further
                        assistance.

            Response Structure:
                Greeting: Begin with a polite greeting or acknowledgment.
                Main Response: Provide the main answer to the user's query.
                Additional Information: Offer any extra tips or direct the
                        user to additional resources if necessary.
                Closing: Close the response politely, encouraging
                        further engagement if appropriate.
            bd
            Tone:
                Professional: Maintain a professional tone that 
                        instills confidence in the user.
                Friendly: Be approachable and friendly to make users 
                        feel comfortable.
                Helpful: Always aim to be as helpful as possible,
                        guiding users to solutions.        
        '''

        self._agent = ChatAgent(
            assistant_sys_msg,
        )

        self._auto_retriever = None
        self._contents = contents
        self._top_k = top_k
        self._similarity_threshold = similarity_threshold
        self._return_detailed_info = return_detailed_info

        self._auto_retriever = auto_retriever or AutoRetriever(
            vector_storage_local_path=vector_storage_local_path,
            storage_type=StorageType.QDRANT,
        )

    async def process(self, message: str) -> str:
        r"""Process the user message, retrieve relevant content, and generate
        a response.

        Args:
            message (str): The user's query message.

        Returns:
            str: The assistant's response message.
        """
        user_raw_msg = message
        print("User message:", user_raw_msg)
        if self._auto_retriever:
            retrieved_content = self._auto_retriever.run_vector_retriever(
                query=user_raw_msg,
                contents=self._contents,
                top_k=self._top_k,
                similarity_threshold=self._similarity_threshold,
                return_detailed_info=self._return_detailed_info,
            )
            user_raw_msg = (
                f"Here is the query to you: {user_raw_msg}\n"
                f"Based on the retrieved content: {retrieved_content}, \n"
                f"answer the query"
            )

        assistant_response = self._agent.step(user_raw_msg)
        return assistant_response.msg.content


class SlackBot(SlackApp):
    r"""SlackBot class that extends the SlackApp class to handle Slack events
    and integrate with a message queue for asynchronous processing.

    This class initializes the Slack app and adds a message handler to process
    Slack events, specifically for incoming messages.

    Args:
        msg_queue (queue.Queue): A thread-safe queue to communicate between
            threads.
        token (Optional[str]): Slack API token for authentication.
        scopes (Optional[str]): Slack app scopes for permissions.
        signing_secret (Optional[str]): Signing secret for verifying Slack
            requests.
        client_id (Optional[str]): Slack app client ID.
        client_secret (Optional[str]): Slack app client secret.
    """

    def __init__(
        self,
        msg_queue: queue.Queue,
        token: Optional[str] = None,
        scopes: Optional[str] = None,
        signing_secret: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        r"""Initializes the SlackBot instance with a message queue and the
        required Slack authentication details.

        Args:
            msg_queue (queue.Queue): A thread-safe queue to communicate between
                threads.
            token (Optional[str]): Slack API token for authentication.
            scopes (Optional[str]): Slack app scopes for permissions.
            signing_secret (Optional[str]): Signing secret for verifying Slack
                requests.
            client_id (Optional[str]): Slack app client ID.
            client_secret (Optional[str]): Slack app client secret.
        """
        super().__init__(
            token=token,
            scopes=scopes,
            signing_secret=signing_secret,
            client_id=client_id,
            client_secret=client_secret,
        )
        self._queue: queue.Queue = msg_queue

    async def on_message(
        self,
        context: "AsyncBoltContext",
        client: "AsyncWebClient",
        event: dict,
        body: dict,
        say: "AsyncSay",
    ):
        r"""Event handler for processing incoming Slack messages.

        This method is called when a message event is received from Slack.
        It acknowledges the message and adds the event body and say function to
        the queue for further processing.

        Args:
            context (AsyncBoltContext): Context object that contains
                information about the Slack event.
            client (AsyncWebClient): Slack Web API client for making API
                requests.
            event (dict): Event data containing details of the incoming Slack
                message.
            body (dict): Full request body from Slack.
            say (AsyncSay): A function to send a response back to the Slack
                channel.
        """
        await context.ack()
        event_body = SlackEventBody(**body)
        self._queue.put((event_body, say))


async def process_message(agent: BotAgent, msg_queue: queue.Queue):
    r"""Process messages from the queue asynchronously.

    This function continuously retrieves messages from the message queue,
    processes them using the `BotAgent` instance, and sends the response back
    to Slack using the `say` function.

    Args:
        agent (BotAgent): An instance of the `BotAgent` class that handles the
            processing of the incoming message.
        msg_queue (queue.Queue): A thread-safe queue that stores Slack event
            messages and the corresponding `say` functions for response.
    """
    while True:
        event_body, say = msg_queue.get()

        logger.info(f"Received message: {event_body.event.text}")
        user_raw_msg = event_body.event.text

        # Process the message using the agent and send response back to Slack.
        response = await agent.process(user_raw_msg)
        await say(response)
        msg_queue.task_done()


def start_async_queue_processor(agent: BotAgent, msg_queue: queue.Queue):
    r"""Start an asynchronous queue processor in a new event loop.

    This function creates a new asyncio event loop in a separate thread to
    asynchronously process messages from the queue. It will run until all
    the messages in the queue have been processed.

    Args:
        agent (BotAgent): The agent responsible for processing the messages.
        msg_queue (queue.Queue): The message queue that contains Slack events
            and responses.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Schedule the asynchronous message processing task in this event loop
    loop.run_until_complete(process_message(agent, msg_queue))


if __name__ == "__main__":
    r"""Main entry point for running the Slack bot application.

    This section initializes the required components including the message 
    queue, agent, and the SlackBot instance. It also starts a separate thread 
    for asynchronous message processing to avoid blocking the Slack bot's main 
    event loop. The `slack_bot.run()` function will handle incoming Slack 
    events on the main thread, while the separate thread will handle processing
    the messages from the queue.
    """
    msg_queue = queue.Queue()

    agent = BotAgent()

    thread = threading.Thread(
        target=start_async_queue_processor, args=(agent, msg_queue)
    )
    thread.start()

    # Initialize the SlackBot with the message queue.
    slack_bot = SlackBot(msg_queue=msg_queue)
    slack_bot.run(3000)

    thread.join()



--------------------------------------------------------------------------------
# File: code\generate_meta_data.py
--------------------------------------------------------------------------------

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
from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType


def generate_meta_data(meta_data: str, num: int = 50, model=None):
    prompt_template = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.CODE, f"generate_{meta_data}"
    )
    prompt = prompt_template.format(**{f"num_{meta_data}": num})
    print(prompt)
    agent = ChatAgent("You are a helpful assistant.", model=model)
    agent.reset()

    assistant_response = agent.step(prompt)
    print(assistant_response.msg.content)


def main(model=None):
    generate_meta_data("languages", 20, model=model)
    generate_meta_data("domains", 50, model=model)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: code\role_playing.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.societies import RolePlaying
from camel.types import TaskType
from camel.utils import print_text_animated


def main(model=None, chat_turn_limit=50) -> None:
    task_prompt = "Develop a poll app"
    language = "JavaScript"
    domain = "Sociology"
    meta_dict = {"language": language, "domain": domain}
    role_play_session = RolePlaying(
        assistant_role_name=f"{language} Programmer",
        assistant_agent_kwargs=dict(model=model),
        user_role_name=f"Person working in {domain}",
        user_agent_kwargs=dict(model=model),
        task_prompt=task_prompt,
        with_task_specify=True,
        task_specify_agent_kwargs=dict(model=model),
        task_type=TaskType.CODE,
        extend_sys_msg_meta_dicts=[meta_dict, meta_dict],
        extend_task_specify_meta_dict=meta_dict,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: code\role_playing_multiprocess.py
--------------------------------------------------------------------------------

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
import json
import multiprocessing
import os
from typing import Any, Dict

from camel.agents import ChatAgent, TaskSpecifyAgent
from camel.generators import SystemMessageGenerator
from camel.messages import BaseMessage
from camel.types import RoleType, TaskType
from camel.utils import download_tasks


def init_chat(
    assistant_agent: ChatAgent,
    user_agent: ChatAgent,
    user_sys_msg: BaseMessage,
    assistant_sys_msg: BaseMessage,
):
    assistant_agent.reset()
    user_agent.reset()

    # Send the system messages again to the agents using chat messages
    assistant_msg = BaseMessage.make_assistant_message(
        role_name=assistant_agent.role_name,
        content=(
            f"{user_sys_msg.content}. "
            "Now start to give me instructions one by one. "
            "Only reply with Instruction and Input."
        ),
    )

    user_msg = BaseMessage.make_user_message(
        role_name=user_agent.role_name, content=f"{assistant_sys_msg.content}"
    )
    assistant_agent.step(user_msg)

    return assistant_msg


def generate_data(
    language_idx: int,
    language_name: str,
    domain_idx: int,
    domain_name: str,
    task_idx: int,
    task_prompt: str,
) -> None:
    max_num_messages = 40

    # Remove number from task prompt
    original_task_prompt = task_prompt.replace(f"{task_idx+1}. ", "")

    task_specify_agent = TaskSpecifyAgent(
        task_type=TaskType.CODE,
    )
    specified_task_prompt = task_specify_agent.run(
        original_task_prompt,
        meta_dict=dict(domain=domain_name, language=language_name),
    )

    print(f"Original Task: {original_task_prompt}")
    print(f"Specified Task: {specified_task_prompt}")

    sys_msg_generator = SystemMessageGenerator(task_type=TaskType.CODE)
    sys_msg_meta_dicts = [
        dict(
            language=language_name,
            domain=domain_name,
            task=specified_task_prompt,
        )
    ] * 2
    assistant_sys_msg, user_sys_msg = sys_msg_generator.from_dicts(
        sys_msg_meta_dicts,
        role_tuples=[
            (f"{language_name} Programmer", RoleType.ASSISTANT),
            (f"{domain_name} User", RoleType.USER),
        ],
    )

    assistant_agent = ChatAgent(
        assistant_sys_msg, message_window_size=max_num_messages
    )
    user_agent = ChatAgent(user_sys_msg, message_window_size=max_num_messages)

    input_assistant_msg = init_chat(
        assistant_agent, user_agent, user_sys_msg, assistant_sys_msg
    )

    print("Assistant System Message: ", assistant_sys_msg.content)
    print("User System Message: ", user_sys_msg.content)
    message_counter = 0
    message_dict: Dict[str, Any] = {}

    # Append roles to the dictionary
    # We start number from 1 not 0.
    message_dict["role_1"] = f"{language_name}_{assistant_agent.role_type!s}"
    message_dict["role_2"] = f"{domain_name}_{user_agent.role_type!s}"
    message_dict["id"] = (
        f"{(language_idx+1):03}_{(domain_idx+1):03}_{(task_idx+1):03}"
    )
    message_dict["original_task"] = original_task_prompt
    message_dict["specified_task"] = specified_task_prompt

    # Threshold to terminate the conversation if no end token appears
    repeat_word_counter = 0
    repeat_word_threshold = 4
    repeat_word_list = [
        "goodbye",
        "good bye",
        "thank",
        "bye",
        "welcome",
        "language model",
    ]

    assistant_instruct_counter = 0
    assistant_instruct_threshold = 1
    assistant_instruct_word = "Instruction:"

    user_no_instruct_counter = 0
    user_no_instruct_threshold = 3
    user_no_instruct_word = "Instruction:"

    # Set max number of messages for the chat

    while message_counter < max_num_messages:
        user_response = user_agent.step(input_assistant_msg)

        # Condition 1: User terminates the chat
        if user_response.terminated:
            message_dict["termination_reason"] = (
                f"{user_agent.role_type!s}: "
                f"{user_response.info['termination_reasons'][0]}"
            )
            break

        print(f"User:\n{user_response.msg.content}\n")

        assistant_response = assistant_agent.step(user_response.msg)

        # Condition 2: Assistant terminates the chat
        if assistant_response.terminated:
            message_dict["termination_reason"] = (
                f"{assistant_agent.role_type!s}: "
                f"{assistant_response.info['termination_reasons'][0]}"
            )
            break

        print(f"Assistant:\n{assistant_response.msg.content}\n")

        # Condition 3: Break if user does not give instruction
        if user_no_instruct_word not in user_response.msg.content:
            user_no_instruct_counter += 1
            if user_no_instruct_counter == user_no_instruct_threshold:
                message_dict['termination_reason'] = (
                    "user_no_instruct_threshold"
                )
                break
        else:
            user_no_instruct_counter = 0

        # Condition 4: Break if assistant gives instruction (flipped role)
        if assistant_instruct_word in assistant_response.msg.content:
            assistant_instruct_counter += 1
            if assistant_instruct_counter == assistant_instruct_threshold:
                message_dict['termination_reason'] = (
                    "assistant_instruct_threshold"
                )
                break
        else:
            assistant_instruct_counter = 0

        # Condition 5: Repeat word observed
        for repeat_word in repeat_word_list:
            if (
                repeat_word in user_response.msg.content.lower()
                or repeat_word in assistant_response.msg.content.lower()
            ):
                repeat_word_counter += 1
                if repeat_word_counter == repeat_word_threshold:
                    message_dict['termination_reason'] = (
                        "repeat_word_threshold"
                    )
                    break
            else:
                repeat_word_counter = 0

        # Save user message
        message_counter += 1
        message_dict[f"message_{message_counter}"] = (
            user_response.msg.to_dict()
        )

        # Condition 5: End token observed
        if "<CAMEL_TASK_DONE>" in user_response.msg.content:
            message_dict['termination_reason'] = "<CAMEL_TASK_DONE>"
            break

        # Save assistant message
        message_counter += 1
        message_dict[f"message_{message_counter}"] = (
            assistant_response.msg.to_dict()
        )

        input_assistant_msg = assistant_response.msg

    message_dict["num_messages"] = message_counter

    if message_dict["num_messages"] == max_num_messages:
        message_dict["termination_reason"] = "max_num_messages"

    with open(
        f"./camel_data/code/{message_dict['id']}.json", "w"
    ) as json_file:
        json.dump(message_dict, json_file, ensure_ascii=False)


def main() -> None:
    # Define the folder path
    folder_path = "./code_data/"

    # Check if the folder already exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Check if the folder is empty
    if not os.listdir(folder_path):
        download_tasks(task=TaskType.CODE, folder_path=folder_path)

    # Chunk for parallel jobs
    try:
        slurm_array_task_id = os.environ.get('SLURM_ARRAY_TASK_ID')
        if not isinstance(slurm_array_task_id, str):
            raise TypeError()
        array_idx = int(slurm_array_task_id)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        array_idx = 0

    languages_per_chunk = 4

    # Parameters for filtering the generated task string
    start_token = "1."
    num_tasks = 50

    with open("./data/code/languages.txt", "r") as f:
        languages = f.read().splitlines()

    with open("./data/code/domains.txt", "r") as f:
        domains = f.read().splitlines()

    assert (array_idx + 1) * languages_per_chunk <= len(languages)
    languages = languages[
        array_idx * languages_per_chunk : (array_idx + 1) * languages_per_chunk
    ]

    pool = multiprocessing.Pool()

    for language_idx, language_name in enumerate(languages):
        language_idx += array_idx * languages_per_chunk
        language_name = " ".join(language_name.split(" ")[1:])
        for domain_idx, domain_name in enumerate(domains):
            domain_name = " ".join(domain_name.split(" ")[1:])
            # Load the task list assigned for assistant and user roles
            with open(
                f"./code_data/tasks/{language_name}_{domain_name}.txt", "r"
            ) as f:
                tasks = f.read().splitlines()

                # Filter out the generated response to include the tasks only
                for i, task in enumerate(tasks):
                    if start_token in task:
                        tasks = tasks[i : i + num_tasks]
                        break

                # Ensure exact number of tasks is generated
                assert str(num_tasks) in tasks[-1], print(tasks)

            for task_idx, task_prompt in enumerate(tasks):
                id = (
                    f"{(language_idx+1):03}_"
                    f"{(domain_idx+1):03}_{(task_idx+1):03}"
                )
                if not os.path.exists(f"./camel_data/code/{id}.json"):
                    pool.apply_async(
                        generate_data,
                        (
                            language_idx,
                            language_name,
                            domain_idx,
                            domain_name,
                            task_idx,
                            task_prompt,
                        ),
                    )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: code\task_generation.py
--------------------------------------------------------------------------------

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
import multiprocessing
import os

from camel.agents import ChatAgent
from camel.generators import CodeTaskPromptGenerator, SystemMessageGenerator
from camel.messages import BaseMessage
from camel.types import RoleType, TaskType


def generate_tasks(
    task_generator_prompt: str,
    language: str,
    domain: str,
    start_token: str = "1.",
    num_tasks: int = 10,
    model=None,
) -> None:
    sys_msg_generator = SystemMessageGenerator(task_type=TaskType.DEFAULT)
    assistant_sys_msg = sys_msg_generator.from_dict(
        dict(), role_tuple=("Task Generator", RoleType.DEFAULT)
    )
    assistant_agent = ChatAgent(assistant_sys_msg, model=model)

    user_msg = BaseMessage.make_user_message(
        role_name="Task Generator", content=task_generator_prompt
    )

    assistant_response = assistant_agent.step(user_msg)

    tasks = assistant_response.msg.content.split("\n")

    # Filter out the generated response to include the tasks only
    for i, task in enumerate(tasks):
        if start_token in task:
            tasks = tasks[i : i + num_tasks]
            break

    # Ensure exact number of tasks is generated
    assert str(num_tasks) in tasks[-1], print(tasks)

    with open(f"./code/tasks/{language}_{domain}.txt", "w") as file:
        file.write("\n".join(tasks))


def main(model=None) -> None:
    num_tasks = 50
    start_token = "1."

    task_generator_prompt_gen = CodeTaskPromptGenerator(
        num_tasks=num_tasks
    ).from_role_files()

    pool = multiprocessing.Pool()
    for task_generator_prompt, language, domain in task_generator_prompt_gen:
        if not os.path.exists(f"./code/tasks/{language}_{domain}.txt"):
            print(language, domain)

            pool.apply_async(
                generate_tasks,
                (
                    task_generator_prompt,
                    language,
                    domain,
                    start_token,
                    num_tasks,
                    model,
                ),
            )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: conversion.py
--------------------------------------------------------------------------------

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
from typing import List

from camel.messages import BaseMessage, HermesFunctionFormatter
from camel.messages.conversion import (
    ShareGPTConversation,
    ShareGPTMessage,
)
from camel.messages.func_message import FunctionCallingMessage


def sharegpt_to_camel_messages(
    conversation: ShareGPTConversation,
) -> List[BaseMessage]:
    r"""Convert ShareGPT conversation to list of CAMEL messages"""
    return [
        BaseMessage.from_sharegpt(msg, HermesFunctionFormatter())
        for msg in conversation
    ]


def camel_messages_to_sharegpt(
    messages: List[BaseMessage],
) -> ShareGPTConversation:
    r"""Convert list of CAMEL messages to ShareGPT conversation"""
    sharegpt_messages = [
        msg.to_sharegpt(HermesFunctionFormatter()) for msg in messages
    ]
    return ShareGPTConversation.model_validate(sharegpt_messages)


# Example usage
if __name__ == "__main__":
    # Create a sample ShareGPT conversation
    sharegpt_conv = ShareGPTConversation.model_validate(
        [
            ShareGPTMessage(
                from_="system", value="You are a helpful assistant."
            ),
            ShareGPTMessage(from_="human", value="What's Tesla's P/E ratio?"),
            ShareGPTMessage(
                from_="gpt",
                value="Let me check Tesla's stock fundamentals.\n"
                "<tool_call>\n{'name': 'get_stock_fundamentals',"
                " 'arguments': {'symbol': 'TSLA'}}\n</tool_call>",
            ),
            ShareGPTMessage(
                from_="tool",
                value='''<tool_response>
{"name": "get_stock_fundamentals", "content": 
{"symbol": "TSLA", "company_name": "Tesla, Inc.", 
"sector": "Consumer Cyclical", "pe_ratio": 49.604652}}
</tool_response>''',
            ),
            ShareGPTMessage(
                from_="gpt",
                value="Tesla (TSLA) currently has a P/E ratio of 49.60.",
            ),
        ]
    )

    # Convert to CAMEL messages
    camel_messages = sharegpt_to_camel_messages(sharegpt_conv)

    print("\nCAMEL Messages:")
    for msg in camel_messages:
        print(f"Role: {msg.role_name}")
        print(f"Content: {msg.content}")
        if isinstance(msg, FunctionCallingMessage):
            print(f"Function Name: {msg.func_name}")
            if msg.args:
                print(f"Arguments: {msg.args}")
            if msg.result:
                print(f"Result: {msg.result}")
        print()

    # Convert back to ShareGPT
    converted_back = camel_messages_to_sharegpt(camel_messages)
    print("\nConverted back to ShareGPT:")
    for msg in converted_back:
        print(f"From: {msg.from_}")
        print(f"Value: {msg.value}")
        print()



--------------------------------------------------------------------------------
# File: data_collector\alpaca_collector.py
--------------------------------------------------------------------------------

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

from camel.agents.chat_agent import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.data_collector import AlpacaDataCollector
from camel.models.model_factory import ModelFactory
from camel.types.enums import ModelPlatformType, ModelType

model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

agent = ChatAgent(
    system_message="You are a helpful assistant",
    model=model,
)

usr_msg = "When is the release date of the video game Portal?"

collector = AlpacaDataCollector().record(agent).start()

# Automatically record the message
resp = agent.step(usr_msg)

print(collector.convert())

print(collector.llm_convert())

collector.reset()

# Manually record the message
collector.step("user", "Tools calling operator", usr_msg)

collector.step("assistant", "Tools calling operator", resp.msgs[0].content)

print(collector.convert())

# ruff: noqa: E501
"""
{'instruction': 'You are a helpful assistantWhen is the release date of the video game Portal?', 'input': '', 'output': 'The video game "Portal" was released on October 10, 2007. It was developed by Valve Corporation and is part of the game bundle known as "The Orange Box," which also included "Half-Life 2" and its episodes.'}
2025-01-19 19:26:09,140 - httpx - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
{'instruction': 'You are a helpful assistant When is the release date of the video game Portal?', 'input': '', 'output': 'The video game "Portal" was released on October 10, 2007. It was developed by Valve Corporation and is part of the game bundle known as "The Orange Box," which also included "Half-Life 2" and its episodes.'}
{'instruction': 'You are a helpful assistantWhen is the release date of the video game Portal?', 'input': '', 'output': 'The video game "Portal" was released on October 10, 2007. It was developed by 
"""



--------------------------------------------------------------------------------
# File: data_collector\sharegpt_collector.py
--------------------------------------------------------------------------------

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

import json

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.data_collector import ShareGPTDataCollector
from camel.models import ModelFactory
from camel.toolkits import MathToolkit
from camel.types import ModelPlatformType, ModelType

tool_list = MathToolkit().get_tools()

model_config_dict = ChatGPTConfig(
    tools=tool_list,
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set external_tools
agent = ChatAgent(
    system_message="You are a helpful assistant",
    model=model,
    tools=tool_list,
)
collector = ShareGPTDataCollector().record(agent).start()

# This will directly run the internal tool
response = agent.step("Call tools to calculate 17 * 19 = ?")


print(json.dumps(collector.convert(), indent=4, ensure_ascii=False))
print(json.dumps(collector.llm_convert(), indent=4, ensure_ascii=False))
print(collector.to_sharegpt_conversation(collector.convert()))

# ruff: noqa: E501
"""
{
    "system": "You are a helpful assistant",
    "tools": "[{\"name\": \"add\", \"description\": \"Adds two numbers.\", \"parameters\": {\"properties\": {\"a\": {\"type\": \"integer\", \"description\": \"The first number to be added.\"}, \"b\": {\"type\": \"integer\", \"description\": \"The second number to be added.\"}}, \"required\": [\"a\", \"b\"], \"type\": \"object\"}}, {\"name\": \"sub\", \"description\": \"Do subtraction between two numbers.\", \"parameters\": {\"properties\": {\"a\": {\"type\": \"integer\", \"description\": \"The minuend in subtraction.\"}, \"b\": {\"type\": \"integer\", \"description\": \"The subtrahend in subtraction.\"}}, \"required\": [\"a\", \"b\"], \"type\": \"object\"}}, {\"name\": \"mul\", \"description\": \"Multiplies two integers.\", \"parameters\": {\"properties\": {\"a\": {\"type\": \"integer\", \"description\": \"The multiplier in the multiplication.\"}, \"b\": {\"type\": \"integer\", \"description\": \"The multiplicand in the multiplication.\"}}, \"required\": [\"a\", \"b\"], \"type\": \"object\"}}]",
    "conversations": [
        {
            "from": "human",
            "value": "Call tools to calculate 17 * 19 = ?"
        },
        {
            "from": "function_call",
            "value": "{\"name\": \"mul\", \"arguments\": {\"a\": 17, \"b\": 19}}"
        },
        {
            "from": "observation",
            "value": "323"
        },
        {
            "from": "gpt",
            "value": "The result of \\( 17 \\times 19 \\) is \\( 323 \\)."
        }
    ]
}
{
    "system": "You are a helpful assistant",
    "tools": "[{\"name\": \"add\", \"description\": \"Adds two numbers.\", \"parameters\": {\"properties\": {\"a\": {\"type\": \"integer\", \"description\": \"The first number to be added.\"}, \"b\": {\"type\": \"integer\", \"description\": \"The second number to be added.\"}}, \"required\": [\"a\", \"b\"], \"type\": \"object\"}}, {\"name\": \"sub\", \"description\": \"Do subtraction between two numbers.\", \"parameters\": {\"properties\": {\"a\": {\"type\": \"integer\", \"description\": \"The minuend in subtraction.\"}, \"b\": {\"type\": \"integer\", \"description\": \"The subtrahend in subtraction.\"}}, \"required\": [\"a\", \"b\"], \"type\": \"object\"}}, {\"name\": \"mul\", \"description\": \"Multiplies two integers.\", \"parameters\": {\"properties\": {\"a\": {\"type\": \"integer\", \"description\": \"The multiplier in the multiplication.\"}, \"b\": {\"type\": \"integer\", \"description\": \"The multiplicand in the multiplication.\"}}, \"required\": [\"a\", \"b\"], \"type\": \"object\"}}]",
    "conversations": [
        {
            "from_": "human",
            "value": "Tools calling operator: Call tools to calculate 17 * 19 = ?"
        },
        {
            "from_": "function_call",
            "value": "{\"name\": \"mul\", \"arguments\": {\"a\": 17, \"b\": 19}}"
        },
        {
            "from_": "gpt",
            "value": "The result of \\( 17 \\times 19 \\) is \\( 323 \\)."
        }
    ]
}
root=[ShareGPTMessage(from_='system', value='You are a helpful assistant'), ShareGPTMessage(from_='human', value='Call tools to calculate 17 * 19 = ?'), ShareGPTMessage(from_='gpt', value='{"name": "multiply", "arguments": "{\'a\': 17, \'b\': 19}"}'), ShareGPTMessage(from_='human', value='"{\'result\': {\'323\'}}"'), ShareGPTMessage(from_='gpt', value='The result of \\( 17 \\times 19 \\) is \\( 323 \\).')]
"""



--------------------------------------------------------------------------------
# File: datagen\evol_instruct\evol_instruct.py
--------------------------------------------------------------------------------

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

import json
import logging
import os

from camel.agents import ChatAgent
from camel.datagen.evol_instruct import EvolInstructPipeline
from camel.datagen.evol_instruct.scorer import MathScorer
from camel.datagen.evol_instruct.templates import MathEvolInstructTemplates
from camel.logger import enable_logging, get_logger, set_log_level
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

os.environ["CAMEL_LOGGING_DISABLED"] = "false"


def main():
    r"""Example usage of EvolInstructPipeline for iterative and parallel
    evolution.
    """
    # Load data
    file_path = "./examples/datagen/evol_instruct/input.json"
    prompts = json.loads(open(file_path, "r", encoding="utf-8").read())

    # Define parameters
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
        model_config_dict={"temperature": 0.7, "max_tokens": 4096},
    )
    agent = ChatAgent(model=model)
    num_generations = 2
    evol_spec = [
        "in-depth",
        "in-depth",
        "in-depth",
        "condense",
    ]

    # Initialize the data generation pipeline with the specified template
    pipeline = EvolInstructPipeline(
        agent=agent,
        templates=MathEvolInstructTemplates,
    )

    # Execute the data generation pipeline
    results = pipeline.generate(
        prompts=prompts,
        evolution_spec=evol_spec,
        num_iterations=4,
        num_generations=num_generations,
        scorer=MathScorer(),
    )

    # Save the generated results to a file
    results_path = "./examples/datagen/evol_instruct/results.json"
    with open(results_path, mode="w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    logger.info(f"Results saved to '{results_path}'.")


if __name__ == "__main__":
    enable_logging()
    set_log_level(logging.WARNING)
    logger = get_logger("evol-instruct")
    logger.info("Begin evolution.")
    main()
    logger.info("Evolution complete.")



--------------------------------------------------------------------------------
# File: datagen\self_improving_cot\download_math_datasets.py
--------------------------------------------------------------------------------

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

import json
import uuid
from pathlib import Path

from datasets import load_dataset


def download_gsm8k_dataset():
    try:
        # Load the dataset using the datasets library
        dataset = load_dataset("openai/gsm8k", "main")

        # Get only 20 items from train split
        data = dataset['train'].select(range(10))

        # Convert to the desired format
        formatted_data = []
        for item in data:
            # Extract the final answer from the solution
            solution = item['answer']
            if solution:
                # GSM8K solutions typically end with "#### number"
                import re

                match = re.search(r'####\s*(\d+)', solution)
                if match:
                    number = match.group(1)
                    # Replace the "#### number" with "\boxed{number}"
                    solution = re.sub(
                        r'####\s*\d+', f'\\\\boxed{{{number}}}', solution
                    )

            formatted_item = {
                "id": str(uuid.uuid4()),  # GSM8K doesn't provide IDs
                "problem": item['question'],
                "type": "openai/gsm8k",  # All problems are from GSM8K
                "solution": solution,  # Use the modified solution with \boxed
                "evaluate_success": False,
                "boxed_answer_success": True,
                "improvement_history": [],
            }
            formatted_data.append(formatted_item)

        # Create output directory if it doesn't exist
        output_dir = Path("examples/datagen/star")
        output_dir.mkdir(exist_ok=True)

        # Save all data to a single JSON file
        output_file = output_dir / "gsm8k_dataset.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(formatted_data, f, indent=4, ensure_ascii=False)
        print(
            f"Successfully saved {len(formatted_data)} records "
            f"to {output_file}"
        )

        return formatted_data

    except Exception as e:
        print(f"Error downloading GSM8K dataset: {e}")


def download_amc_aime_dataset():
    try:
        # Load the dataset using the datasets library
        dataset = load_dataset(
            "mlfoundations-dev/bespokelabs-sky-t1-numina-amc-aime-subset-unfiltered"
        )

        # Get the first 4070 items from train split
        data = dataset['train'].select(range(4069))

        # Convert to the desired format
        formatted_data = []
        for item in data:
            formatted_item = {
                "id": str(uuid.uuid4()),
                "problem": item['problem'],
                "type": "amc_aime",
                "solution": item['ground_truth_solution'],
            }
            formatted_data.append(formatted_item)

        # Create output directory if it doesn't exist
        output_dir = Path("examples/datagen/star")
        output_dir.mkdir(exist_ok=True)

        # Save all data to a single JSON file
        output = formatted_data
        output_file = output_dir / "star_r1_output_amc_aime.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4, ensure_ascii=False)
        print(
            f"Successfully saved {len(formatted_data)} records "
            f"to {output_file}"
        )

        return formatted_data

    except Exception as e:
        print(f"Error downloading AMC/AIME dataset: {e}")
        return None


if __name__ == "__main__":
    download_gsm8k_dataset()
    # download_amc_aime_dataset()



--------------------------------------------------------------------------------
# File: datagen\self_improving_cot\self_improving_cot_example.py
--------------------------------------------------------------------------------

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

import json
import os
import time

from camel.agents import ChatAgent
from camel.configs import DeepSeekConfig
from camel.datagen import SelfImprovingCoTPipeline
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

# from camel.models.reward import NemotronRewardModel

"""
please set the below os environment:
export DEEPSEEK_API_KEY=""
"""


model = ModelFactory.create(
    model_platform=ModelPlatformType.DEEPSEEK,
    model_type=ModelType.DEEPSEEK_CHAT,
    model_config_dict=DeepSeekConfig(temperature=0).as_dict(),
)


def main():
    start_time = time.time()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    problems_path = os.path.join(current_dir, 'gsm8k_dataset.json')
    output_path = os.path.join(current_dir, 'self_improving_cot_output.json')

    # Load problems from JSON file
    with open(problems_path, 'r') as f:
        problems = json.load(f)

    # Initialize agent
    reason_agent_system_message = """Please reason step by step, and put your 
    final answer within \\boxed{}."""
    evaluate_agent_system_message = """You are a highly critical teacher who 
    evaluates the student's answers with a meticulous and demanding approach.
    """
    reason_agent = ChatAgent(reason_agent_system_message, model=model)
    evaluate_agent = ChatAgent(evaluate_agent_system_message)

    # Initialize reward model (optional)
    # reward_model = NemotronRewardModel(
    #     model_type=ModelType.NVIDIA_NEMOTRON_340B_REWARD,
    #     url="https://integrate.api.nvidia.com/v1",
    #     api_key=os.environ.get("NVIDIA_API_KEY"),
    # )

    # Set score thresholds for different dimensions (optional)
    score_threshold = {
        "correctness": 0.9,
        "clarity": 0.9,
        "completeness": 0.6,
    }
    # Or use a single threshold for all dimensions:
    # score_threshold = 0.9

    # Create and run pipeline
    pipeline = SelfImprovingCoTPipeline(
        reason_agent=reason_agent,
        evaluate_agent=evaluate_agent,
        problems=problems,  # Pass problems list directly
        output_path=output_path,
        max_iterations=3,
        score_threshold=score_threshold,
        # reward_model=reward_model,  # To use a reward model (optional)
    )

    results = pipeline.generate(rationalization=False)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\nProcessed {len(results)} problems")
    print(f"Results saved to: {output_path}")
    print(f"Total execution time: {execution_time:.2f} seconds")


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: datagen\self_improving_cot\self_improving_cot_example_with_r1.py
--------------------------------------------------------------------------------

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

import json
import os
import time

from camel.agents import ChatAgent
from camel.datagen import SelfImprovingCoTPipeline
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

"""
please set the below os environment:
export DEEPSEEK_API_KEY=""
export GET_REASONING_CONTENT="true"
"""

evaluate_model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
)

reason_model_1 = ModelFactory.create(
    model_platform=ModelPlatformType.DEEPSEEK,
    model_type=ModelType.DEEPSEEK_REASONER,
)

reason_model_2 = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="accounts/fireworks/models/deepseek-r1",
    api_key=os.getenv("FIREWORKS_API_KEY"),
    url="https://api.fireworks.ai/inference/v1",
    model_config_dict={"max_tokens": 4096},
)

reason_model_3 = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="deepseek-ai/DeepSeek-R1",
    api_key=os.getenv("HYPERBOLIC_API_KEY"),
    url="https://api.hyperbolic.xyz/v1",
)

reason_model_4 = ModelFactory.create(
    model_platform=ModelPlatformType.TOGETHER,
    model_type="deepseek-ai/DeepSeek-R1",
    api_key=os.getenv("TOGETHER_API_KEY"),
)
# from camel.models.reward import NemotronRewardModel


def main():
    start_time = time.time()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    problems_path = os.path.join(current_dir, 'outputs/gsm8k_dataset.json')
    output_path = os.path.join(
        current_dir, 'outputs/self_improving_cot_r1_output.json'
    )

    # Load problems from JSON file
    with open(problems_path, 'r') as f:
        problems = json.load(f)

    # Initialize agent
    reason_agent_system_message = """Answer my question and give your 
    final answer within \\boxed{}."""
    evaluate_agent_system_message = """You are a highly critical teacher who 
    evaluates the student's answers with a meticulous and demanding approach.
    """
    reason_agent = ChatAgent(
        system_message=reason_agent_system_message,
        model=[
            # reason_model_1,
            reason_model_2,
            # reason_model_3,
            # reason_model_4,
        ],
    )
    evaluate_agent = ChatAgent(
        system_message=evaluate_agent_system_message, model=evaluate_model
    )

    # Initialize reward model (optional)
    # reward_model = NemotronRewardModel(
    #     model_type=ModelType.NVIDIA_NEMOTRON_340B_REWARD,
    #     url="https://integrate.api.nvidia.com/v1",
    #     api_key=os.environ.get("NVIDIA_API_KEY"),
    # )

    # Set score thresholds for different dimensions (optional)
    score_threshold = {
        "correctness": 1.0,
        "clarity": 0.0,
        "completeness": 0.0,
    }
    # Or use a single threshold for all dimensions:
    # score_threshold = 0.9

    # Create and run pipeline
    pipeline = SelfImprovingCoTPipeline(
        reason_agent=reason_agent,
        evaluate_agent=evaluate_agent,
        problems=problems,  # Pass problems list directly
        output_path=output_path,
        max_iterations=0,
        score_threshold=score_threshold,
        # reward_model=reward_model,  # To use a reward model (optional)
    )

    results = pipeline.generate(rationalization=False)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\nProcessed {len(results)} problems")
    print(f"Results saved to: {output_path}")
    print(f"Total execution time: {execution_time:.2f} seconds")


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: datagen\self_instruct\self_instruct.py
--------------------------------------------------------------------------------

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
from camel.datagen.self_instruct import SelfInstructPipeline

agent = ChatAgent()

pipeline = SelfInstructPipeline(
    agent=agent,
    seed='seed_tasks.jsonl',
    num_machine_instructions=5,
    data_output_path='./data_output.json',
    human_to_machine_ratio=(6, 2),
)

pipeline.generate()



--------------------------------------------------------------------------------
# File: datagen\source2synth.py
--------------------------------------------------------------------------------

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

import json
import logging

from camel.datagen.source2synth.data_processor import (
    UserDataProcessor,
)
from camel.datagen.source2synth.user_data_processor_config import (
    ProcessorConfig,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def save_results(results, output_file: str):
    r"""Save results to a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info(f"Results saved to: {output_file}")


def main():
    r"""Example usage."""
    # 1. Create configuration
    config = ProcessorConfig(
        seed=42,
        min_length=50,
        max_length=1000,
        complexity_threshold=0.5,
        dataset_size=10,
        use_ai_model=True,
    )

    # 2. Create the processor
    processor = UserDataProcessor(config)

    # 3. Prepare test data - texts containing multiple related information
    test_texts = [
        # Chain of technological developments
        """
        The invention of transistors revolutionized electronics in the 1950s. 
        These tiny semiconductor devices enabled the development of smaller and more 
        efficient computers. The miniaturization of computers led to the creation of 
        personal computers in the 1980s, which transformed how people work and communicate. 
        This digital revolution eventually gave rise to the internet, connecting billions 
        of people worldwide. Today, this interconnected network powers artificial 
        intelligence systems that are reshaping various industries.
        """,  # noqa: E501
        # Environmental changes causation chain
        """
        Industrial activities have significantly increased carbon dioxide emissions since 
        the Industrial Revolution. These elevated CO2 levels have enhanced the greenhouse 
        effect, trapping more heat in Earth's atmosphere. The rising global temperatures 
        have accelerated the melting of polar ice caps, which has led to rising sea levels. 
        Coastal communities are now facing increased flooding risks, forcing many to 
        consider relocation. This migration pattern is creating new challenges for urban 
        planning and resource management.
        """,  # noqa: E501
        # Biological evolution chain
        """
        The discovery of antibiotics began with Alexander Fleming's observation of 
        penicillin in 1928. The widespread use of these medications has saved countless 
        lives from bacterial infections. However, the extensive use of antibiotics has 
        led to the evolution of resistant bacteria strains. These superbugs now pose 
        a significant challenge to modern medicine, requiring the development of new 
        treatment approaches. Scientists are exploring alternative solutions like 
        bacteriophage therapy to combat antibiotic resistance.
        """,  # noqa: E501
    ]

    # 4. Process a single text
    logger.info("Processing a single text example...")
    single_result = processor.process_text(
        test_texts[0], source="technology_evolution"
    )

    # Save the single text processing result
    save_results(single_result, "single_text_results.json")

    # 5. Batch process texts
    logger.info("Batch processing texts...")
    batch_results = processor.process_batch(
        test_texts,
        sources=["tech_evolution", "climate_change", "medical_evolution"],
    )

    # Save the batch processing results
    save_results(batch_results, "batch_results.json")

    # 6. Print example results
    print("\n=== Single Text Processing Example ===")
    if single_result:
        for i, result in enumerate(single_result, 1):
            print(f"\nText {i}:")
            print(f"Source: {result['metadata']['source']}")
            print(f"Complexity: {result['metadata']['complexity']:.2f}")
            print("\nQ&A Pairs:")
            for j, qa in enumerate(result['qa_pairs'], 1):
                print(f"\nQ&A Pair {j}:")
                print(f"Type: {qa['type']}")
                print(f"Question: {qa['question']}")
                print("Reasoning Steps:")
                for step_num, step in enumerate(
                    qa.get('reasoning_steps', []), 1
                ):
                    print(f"{step_num}. {step}")
                print(f"Answer: {qa['answer']}")
                print("Supporting Facts:")
                for fact_num, fact in enumerate(
                    qa.get('supporting_facts', []), 1
                ):
                    print(f"{fact_num}. {fact}")

    print("\n=== Batch Processing Statistics ===")
    print(f"Total texts processed: {len(test_texts)}")
    pairs_generated = sum(len(result['qa_pairs']) for result in batch_results)
    print(f"Total Q&A pairs generated: {pairs_generated}")

    # 7. Analyze results
    multi_hop_qa = sum(
        1
        for result in batch_results
        for qa in result['qa_pairs']
        if qa['type'] == 'multi_hop_qa'
    )
    template_generated = sum(
        1
        for result in batch_results
        for qa in result['qa_pairs']
        if qa['type'] == 'template_generated_multi_hop'
    )

    print("\n=== Generation Statistics ===")
    print(f"AI-generated multi-hop Q&A count: {multi_hop_qa}")
    print(f"Template-generated multi-hop Q&A count: {template_generated}")

    # 8. Analyze reasoning steps
    avg_steps = sum(
        len(qa.get('reasoning_steps', []))
        for result in batch_results
        for qa in result['qa_pairs']
    ) / sum(len(result['qa_pairs']) for result in batch_results)

    print(f"\nAverage reasoning steps: {avg_steps:.2f}")

    # 9. Calculate average complexity
    avg_complexity = sum(
        result['metadata']['complexity'] for result in batch_results
    ) / len(batch_results)

    print(f"Average complexity score: {avg_complexity:.2f}")


if __name__ == "__main__":
    main()


'''
===============================================================================
Constructing examples: 100%|
███████████████████████████████████████████████████████████████████████████████
█| 1/1 [00:10<00:00, 10.98s/it]
Constructing examples: 100%|
███████████████████████████████████████████████████████████████████████████████
█| 3/3 [00:22<00:00,  7.64s/it]

=== Single Text Processing Example ===

Text 1:
Source: technology_evolution
Complexity: 0.88

Q&A Pairs:

Q&A Pair 1:
Type: multi_hop_qa
Question: How did the invention of transistors impact the development of 
personal computers?
Reasoning Steps:
1. {'step': 'Identify the role of transistors in electronics.'}
2. {'step': 'Understand how transistors enabled the miniaturization of 
computers.'}
3. {'step': 'Connect the miniaturization of computers to the creation of 
personal computers in the 1980s.'}
4. {'step': 'Determine the overall impact of personal computers on work and 
communication.'}
Answer: The invention of transistors allowed for smaller and more efficient 
computers, which led to the development of personal computers in the 1980s, 
transforming work and communication.
Supporting Facts:
1. Transistors are semiconductor devices that revolutionized electronics.
2. The miniaturization of computers was made possible by transistors.
3. Personal computers emerged in the 1980s as a result of smaller computer 
designs.
4. Personal computers changed how people work and communicate.

Q&A Pair 2:
Type: multi_hop_qa
Question: What was the sequence of developments that led from transistors to 
the internet?
Reasoning Steps:
1. {'step': 'Identify how transistors contributed to the development of 
smaller and more efficient computers.'}
2. {'step': 'Explain how the miniaturization of computers resulted in the 
creation of personal computers in the 1980s.'}
3. {'step': 'Discuss how personal computers transformed work and communication.
'}
4. {'step': 'Connect the transformation in communication to the rise of the 
internet.'}
Answer: Transistors enabled smaller computers, which led to personal computers 
in the 1980s, transforming communication and eventually giving rise to the 
internet.
Supporting Facts:
1. Transistors are tiny semiconductor devices that made computers smaller and 
more efficient.
2. The miniaturization of computers allowed for the creation of personal 
computers in the 1980s.
3. Personal computers transformed how people work and communicate.
4. The digital revolution and personal computers contributed to the rise of 
the internet, connecting billions worldwide.

Q&A Pair 3:
Type: multi_hop_qa
Question: How did the miniaturization of computers contribute to the 
development of artificial intelligence systems today?
Reasoning Steps:
1. {'step': 'Identify the impact of miniaturization on the creation of 
personal computers in the 1980s.'}
2. {'step': 'Explain how personal computers transformed communication and work.
'}
3. {'step': 'Connect the digital revolution and the rise of the internet to 
the development of artificial intelligence.'}
4. {'step': 'Discuss how the interconnected network of the internet supports 
AI systems in various industries.'}
Answer: The miniaturization of computers led to personal computers, which 
transformed communication and work, and this digital revolution, along with 
the internet, supports the development of artificial intelligence systems 
today.
Supporting Facts:
1. Miniaturization of computers enabled the creation of personal computers in 
the 1980s.
2. Personal computers transformed how people work and communicate.
3. The digital revolution led to the rise of the internet, connecting billions 
of people.
4. The internet powers artificial intelligence systems that are reshaping 
various industries.

=== Batch Processing Statistics ===
Total texts processed: 3
Total Q&A pairs generated: 9

=== Generation Statistics ===
AI-generated multi-hop Q&A count: 9
Template-generated multi-hop Q&A count: 0

Average reasoning steps: 4.00
Average complexity score: 0.90
===============================================================================
'''



--------------------------------------------------------------------------------
# File: datahubs\huggingface.py
--------------------------------------------------------------------------------

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
from camel.datahubs.huggingface import HuggingFaceDatasetManager
from camel.datahubs.models import Record

manager = HuggingFaceDatasetManager()

USERNAME = "username"
REPO_ID = f"{USERNAME}/test-dataset-example"

records = [
    Record(
        id="record-1",
        content={"input": "What is AI?", "output": "Artificial Intelligence"},
        metadata={"method": "SFT"},
    ),
    Record(
        id="record-2",
        content={"input": "Translate 'hello'", "output": "Bonjour"},
        metadata={"method": "GPT"},
    ),
]

# 1. create a dataset
print("Creating dataset...")
dataset_url = manager.create_dataset(name=REPO_ID)
print(f"Dataset created: {dataset_url}")

# 2. create a dataset card
print("Creating dataset card...")
manager.create_dataset_card(
    dataset_name=REPO_ID,
    description="Test dataset",
    license="mit",
    language=["en"],
    size_category="<1MB",
    version="0.1.0",
    tags=["test", "example"],
    task_categories=["other"],
    authors=["camel-ai"],
)
print("Dataset card created successfully.")

# 3. add records to the dataset
print("Adding records to the dataset...")
manager.add_records(dataset_name=REPO_ID, records=records)
print("Records added successfully.")

# 4. list all records
print("Listing all records...")
all_records = manager.list_records(dataset_name=REPO_ID)
print("Records in the dataset:")
for record in all_records:
    print(
        f"- ID: {record.id}, Input: {record.content['input']}, "
        f"Output: {record.content['output']}"
    )

# 5. update a record
new_records = [
    Record(
        id="record-3",
        content={"input": "What is ML?", "output": "Machine Learning"},
        metadata={"method": "Updated GPT"},
    )
]
print("Updating records...")
manager.update_records(dataset_name=REPO_ID, records=new_records)
print("Records updated successfully.")

# 6. list updated records
print("Listing updated records...")
updated_records = manager.list_records(dataset_name=REPO_ID)
print("Updated records in the dataset:")
for record in updated_records:
    print(
        f"- ID: {record.id}, Input: {record.content['input']}, "
        f"Output: {record.content['output']}"
    )

# 7. delete a record
print("Deleting record with ID 'record-1'...")
manager.delete_record(dataset_name=REPO_ID, record_id="record-1")
print("Record deleted successfully.")

# 8. list records after deletion
print("Listing records after deletion...")
final_records = manager.list_records(dataset_name=REPO_ID)
print("Final records in the dataset:")
for record in final_records:
    print(
        f"- ID: {record.id}, Input: {record.content['input']}, "
        f"Output: {record.content['output']}"
    )

# 9. list all datasets
print("Listing all datasets...")
datasets = manager.list_datasets(USERNAME)
print("Datasets:")
for dataset in datasets:
    print(f"- {dataset}")

# 10. delete a dataset
print(f"Deleting dataset: {REPO_ID}...")
manager.delete_dataset(dataset_name=REPO_ID)
print("Dataset deleted successfully.")



--------------------------------------------------------------------------------
# File: dataset\few_shot_generator.py
--------------------------------------------------------------------------------

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

import asyncio
from pathlib import Path

from dotenv import load_dotenv

from camel.configs import ChatGPTConfig
from camel.datasets import FewShotGenerator, StaticDataset
from camel.logger import get_logger
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.verifiers import PythonVerifier

logger = get_logger(__name__)

verifier = PythonVerifier(required_packages=["sympy"])
asyncio.run(verifier.setup())

raw_data2 = [
    {
        "question": "Evaluate the limit as x approaches 0 of (sin(3*x) - 3*x) / x**3.",  # noqa: E501
        "final_answer": "-9/2",
        "rationale": '''from sympy import symbols, limit, sin
x = symbols('x')
expr = (sin(3*x) - 3*x) / x**3
result = limit(expr, x, 0)
print(result)''',
    },
    {
        "question": "Evaluate the definite integral of (1 - x**2)**3 from x = 0 to x = 1.",  # noqa: E501
        "final_answer": "16/35",
        "rationale": '''from sympy import symbols, integrate
x = symbols('x')
expr = (1 - x**2)**3
result = integrate(expr, (x, 0, 1))
print(result)''',
    },
    {
        "question": "Evaluate the limit as n approaches infinity of n*(sqrt(n**2 + 1) - n).",  # noqa: E501
        "final_answer": "1/2",
        "rationale": '''from sympy import symbols, limit, sqrt
n = symbols('n', positive=True)
expr = n*(sqrt(n**2 + 1) - n)
result = limit(expr, n, float("inf"))
print(result)''',
    },
    {
        "question": "Compute the sum of the series sum from n = 1 to 50 of 1/(n*(n+1)).",  # noqa: E501
        "final_answer": "50/51",
        "rationale": '''from sympy import symbols, summation
n = symbols('n', positive=True, integer=True)
expr = 1/(n*(n+1))
result = summation(expr, (n, 1, 50))
print(result)''',
    },
]

seed_dataset = StaticDataset(raw_data2)


load_dotenv()


model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig().as_dict(),
)
generator = FewShotGenerator(
    seed_dataset=seed_dataset, verifier=verifier, model=model
)

new_data = asyncio.run(generator.generate_new(n=2, max_retries=5))

for dp in new_data:
    print(dp)

generator.save_to_jsonl(Path("generated_data.jsonl"))

asyncio.run(verifier.cleanup())



--------------------------------------------------------------------------------
# File: dataset\self_instruct_generator.py
--------------------------------------------------------------------------------

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

import asyncio
from pathlib import Path

from dotenv import load_dotenv

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.datasets import SelfInstructGenerator, StaticDataset
from camel.logger import get_logger
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.verifiers import PythonVerifier

logger = get_logger(__name__)

verifier = PythonVerifier(required_packages=["sympy"], timeout=60)
asyncio.run(verifier.setup())

raw_data2 = [
    {
        "question": "Evaluate the limit as x approaches 0 of (sin(3*x) - 3*x) / x**3.",  # noqa: E501
        "final_answer": "-9/2",
        "rationale": '''from sympy import symbols, limit, sin
x = symbols('x')
expr = (sin(3*x) - 3*x) / x**3
result = limit(expr, x, 0)
print(result)''',
    },
    {
        "question": "Evaluate the definite integral of (1 - x**2)**3 from x = 0 to x = 1.",  # noqa: E501
        "final_answer": "16/35",
        "rationale": '''from sympy import symbols, integrate
x = symbols('x')
expr = (1 - x**2)**3
result = integrate(expr, (x, 0, 1))
print(result)''',
    },
    {
        "question": "Evaluate the limit as n approaches infinity of n*(sqrt(n**2 + 1) - n).",  # noqa: E501
        "final_answer": "1/2",
        "rationale": '''from sympy import symbols, limit, sqrt
n = symbols('n', positive=True)
expr = n*(sqrt(n**2 + 1) - n)
result = limit(expr, n, float("inf"))
print(result)''',
    },
    {
        "question": "Compute the sum of the series sum from n = 1 to 50 of 1/(n*(n+1)).",  # noqa: E501
        "final_answer": "50/51",
        "rationale": '''from sympy import symbols, summation
n = symbols('n', positive=True, integer=True)
expr = 1/(n*(n+1))
result = summation(expr, (n, 1, 50))
print(result)''',
    },
]

seed_dataset = StaticDataset(raw_data2)

load_dotenv()

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig().as_dict(),
)

RATIONALE_SYSTEM_PROMPT = """You are an advanced Python code assistant.

Your task is to **solve the given question by writing Python code only**,
without any explanation or natural language output.
The code must compute the answer **programmatically**, not by hardcoding or
guessing the result.

**Rules:**
- Use Python code to perform the actual computation.
- Use sympy to solve the problem. Do not import any other libraries.
- **Do not hardcode the final answer** (e.g., avoid writing `print(1/2)` unless
  that value is computed).
- The result must be obtained through valid computation logic in code.
- Do not include explanations. Output code only.
- The entire code must be wrapped in triple backticks:
```
[Your Python code here]
```

Now, solve the following question using Python. Only output the code:
"""

rationale_agent = ChatAgent(RATIONALE_SYSTEM_PROMPT, model=model)

generator = SelfInstructGenerator(
    seed_dataset=seed_dataset,
    verifier=verifier,
    instruction_agent=None,  # use default instruction agent
    rationale_agent=rationale_agent,
)

new_data = asyncio.run(generator.generate_new(n=3, max_retries=5))

for dp in new_data:
    print(dp)

generator.save_to_jsonl(Path("generated_data.jsonl"))

asyncio.run(verifier.cleanup())



--------------------------------------------------------------------------------
# File: deductive_reasoner_agent\deduce_conditions_and_quality.py
--------------------------------------------------------------------------------

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
import json

from colorama import Fore

from camel.agents.deductive_reasoner_agent import DeductiveReasonerAgent


def main(model=None) -> None:
    # Construct deductive reasoner agent
    insight_agent = DeductiveReasonerAgent(model=model)

    starting_state = "The current empty website."
    target_state = "A website with search capabilities."
    conditions_and_quality = insight_agent.deduce_conditions_and_quality(
        starting_state=starting_state, target_state=target_state
    )
    print(
        Fore.GREEN
        + "Conditions and quality from the starting state:\n"
        + f"{json.dumps(conditions_and_quality, 
            indent=4, ensure_ascii=False)}",
        Fore.RESET,
    )


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: embeddings\jina_embedding_example.py
--------------------------------------------------------------------------------

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

import requests
from PIL import Image

from camel.embeddings import JinaEmbedding
from camel.types import EmbeddingModelType

# Set the text embedding instance
jina_text_embed = JinaEmbedding(
    model_type=EmbeddingModelType.JINA_EMBEDDINGS_V3,
)

# Embed the text
text_embeddings = jina_text_embed.embed_list(
    ["What is the capital of France?"]
)

print(len(text_embeddings[0]))
'''
===============================================================================
1024
===============================================================================
'''


# Set the code embedding instance
jina_code_embed = JinaEmbedding(
    model_type=EmbeddingModelType.JINA_EMBEDDINGS_V2_BASE_CODE,
    normalized=True,
)

# Embed the code
code_embeddings = jina_code_embed.embed_list(
    [
        "Calculates the square of a number. Parameters: number (int or float)"
        " - The number to square. Returns: int or float - The square of the"
        " number.",
        "This function calculates the square of a number you give it.",
        "def square(number): return number ** 2",
        "print(square(5))",
        "Output: 25",
        "Each text can be up to 8192 tokens long",
    ]
)

print(len(code_embeddings[0]))
'''
===============================================================================
768
===============================================================================
'''

# Set the clip embedding instance
jina_clip_embed = JinaEmbedding(
    model_type=EmbeddingModelType.JINA_CLIP_V2,
)

# Embed the text
text_embeddings = jina_clip_embed.embed_list(
    ["What is the capital of France?"]
)

# Set example image to embed
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image_example = Image.open(requests.get(url, stream=True).raw)

# Embed the image
image_embeddings = jina_clip_embed.embed_list([image_example])

print(len(text_embeddings[0]))
'''
===============================================================================
1024
===============================================================================
'''

print(len(image_embeddings[0]))

'''
===============================================================================
1024
===============================================================================
'''



--------------------------------------------------------------------------------
# File: embeddings\openai_compatible_embedding_example.py
--------------------------------------------------------------------------------

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

from camel.embeddings import OpenAICompatibleEmbedding

# Set the embedding instance
nv_embed = OpenAICompatibleEmbedding(
    model_type="nvidia/nv-embed-v1",
    api_key="nvapi-xxx",
    url="https://integrate.api.nvidia.com/v1",
)

# Embed the text
text_embeddings = nv_embed.embed_list(["What is the capital of France?"])

print(len(text_embeddings[0]))
'''
===============================================================================
4096
===============================================================================
'''



--------------------------------------------------------------------------------
# File: embeddings\vlm_embedding_example.py
--------------------------------------------------------------------------------

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

import requests
from PIL import Image

from camel.embeddings import VisionLanguageEmbedding

# Set the VLM instance
VLM_instance = VisionLanguageEmbedding(
    model_name="openai/clip-vit-base-patch32"
)

# Set example image to embed
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image_example = Image.open(requests.get(url, stream=True).raw)

# Embed the image
image_embeddings = VLM_instance.embed_list([image_example])

# Set example text to embed
text_example = 'two cats laying on the sofa'

# Embed the text
text_embeddings = VLM_instance.embed_list([text_example])

# Get the length of 2 embeedings
print(len(image_embeddings[0]))
print(len(text_embeddings[0]))

'''
===============================================================================
512
512
===============================================================================
'''



--------------------------------------------------------------------------------
# File: embodiment\code_execution.py
--------------------------------------------------------------------------------

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
from camel.agents import EmbodiedAgent
from camel.generators import SystemMessageGenerator
from camel.types import RoleType


def main():
    # Create an embodied agent
    role_name = "Programmer"
    meta_dict = dict(role=role_name, task="Programming")
    sys_msg = SystemMessageGenerator().from_dict(
        meta_dict=meta_dict,
        role_tuple=(role_name, RoleType.EMBODIMENT),
    )
    embodied_agent = EmbodiedAgent(
        sys_msg,
        verbose=True,
    )
    print(embodied_agent.system_message.content)

    user_msg = (
        "Write a bash script to install numpy, "
        "then write a python script to compute "
        "the dot product of [6.75,3] and [4,5] and print the result, "
        "then write a script to open a browser and search today's weather."
    )
    response = embodied_agent.step(user_msg)
    print(response.msg.content)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: embodiment\hugging_face_tool.py
--------------------------------------------------------------------------------

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
from typing import List

from camel.agents import EmbodiedAgent, HuggingFaceToolAgent
from camel.agents.tool_agents.base import BaseToolAgent
from camel.generators import SystemMessageGenerator
from camel.types import RoleType


def main():
    # Create an embodied agent
    role_name = "Artist"
    meta_dict = dict(role=role_name, task="Drawing")
    sys_msg = SystemMessageGenerator().from_dict(
        meta_dict=meta_dict,
        role_tuple=(f"{role_name}'s Embodiment", RoleType.EMBODIMENT),
    )
    tool_agents = [
        HuggingFaceToolAgent(
            'hugging_face_tool_agent',
            remote=True,
        )
    ]
    tool_agents: List[BaseToolAgent]
    embodied_agent = EmbodiedAgent(
        sys_msg,
        verbose=True,
        tool_agents=tool_agents,
    )

    user_msg = (
        "Draw all the Camelidae species, "
        "caption the image content, "
        "save the images by species name."
    )
    response = embodied_agent.step(user_msg)
    print(response.msg.content)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: evaluation\single_agent.py
--------------------------------------------------------------------------------

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
import json
import os
import re
from typing import Any, Dict, List

from camel.agents import ChatAgent
from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType


def parse_question_string(
    question_string: str, category: str
) -> List[Dict[str, Any]]:
    pattern = r'^(\d+)\.\s+(.*?)\s*\n*$'
    questions = []
    for match in re.finditer(pattern, question_string, re.MULTILINE):
        question_id = int(match.group(1))
        text = match.group(2)
        questions.append(
            {'question_id': question_id, 'text': text, 'category': category}
        )
    return questions


def generate_questions(
    examples: str,
    category: str,
    save_file_name: str,
    key: str = 'generate_questions',
    num_questions: int = 20,
    model=None,
) -> None:
    prompt_template = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.EVALUATION, key
    )

    evaluation_dict = {
        'num_questions': num_questions,
        'category': category,
        'examples': examples,
    }

    prompt = prompt_template.format(**evaluation_dict)
    print(prompt)

    agent = ChatAgent("You are a helpful assistant.", model=model)
    agent.reset()

    assistant_response = agent.step(prompt)

    if len(assistant_response.msgs) > 0:
        print(assistant_response.msg.content)

        parsed_assistant_msg = parse_question_string(
            assistant_response.msg.content, category
        )

        # save json file
        folder_path = './evaluation_data/questions'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(f"{folder_path}/{save_file_name}.jsonl", "w") as f:
            for item in parsed_assistant_msg:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')


def main(model=None) -> None:
    # generate ai society evaluation questions
    examples = (
        "1. What are the most effective ways to deal with stress?\n"
        "2. Explain the process of natural selection and how it "
        "contributes to the evolution and adaptation of species.\n"
        "3. Can you help me write a formal email to a potential"
        "business partner proposing a joint venture?"
    )

    category = 'generic task Q&A'
    save_file_name = 'questions_ai_society'
    generate_questions(examples, category, save_file_name, model=model)

    # generate coding evaluation questions
    examples = (
        "1. Develop a C++ program that reads a text file line by line and"
        "counts the number of occurrences of a specific word in the file.\n"
        "2. Implement a Java function to find the longest common"
        " subsequence of two input strings using dynamic programming.\n"
        "3. Implement a machine learning-based chatbot system in Python."
    )

    category = 'coding task'
    save_file_name = 'questions_code'
    generate_questions(examples, category, save_file_name, model=model)

    # generate math evaluation questions
    examples = (
        "1. Given that f(x) = 5x^3 - 2x + 3, find the value of f(2).\n"
        "2. If the endpoints of a line segment are (2, -2) and (10, 4), "
        "what is the length of the segment?\n"
        "3. Solve for x in the equation 3x + 10 = 5(x - 2)."
    )

    category = 'math'
    save_file_name = 'questions_math'
    generate_questions(examples, category, save_file_name, model=model)

    # generate science evaluation questions
    examples = (
        "1. What is the probability of finding a particle with a given energy"
        " in a one-dimensional infinite square well potential when the"
        " potential width is 2 nm and the particle has a mass of 5x10^-26"
        " kg? Use the Schrödinger equation to solve for the allowed energy"
        " states and their wave functions.\n"
        "2. How does habitat loss and fragmentation affect the migratory"
        " patterns and survival of a specific species, such as the monarch"
        " butterfly, over time?\n"
        "3. What is the systematic name of the organic compound with the"
        " molecular formula C6H12O and a ketone functional group located"
        " on the second carbon atom from the left end?"
    )

    category = 'science'

    save_file_name = 'questions_science'
    generate_questions(
        examples, category, save_file_name, num_questions=60, model=model
    )


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: external_tools\use_external_tools.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import MathToolkit, SearchToolkit
from camel.types import ModelPlatformType, ModelType


def main():
    # Set the tools for the external_tools
    internal_tools = SearchToolkit().get_tools()
    external_tools = MathToolkit().get_tools()
    tool_list = internal_tools + external_tools

    model_config_dict = ChatGPTConfig(
        tools=tool_list,
        temperature=0.0,
    ).as_dict()

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=model_config_dict,
    )

    # Set external_tools
    external_tool_agent = ChatAgent(
        system_message="You are a helpful assistant",
        model=model,
        tools=internal_tools,
        external_tools=external_tools,
    )

    # This will directly run the internal tool
    response = external_tool_agent.step(
        "When is the release date of the video game Portal?"
    )
    print(response.msg.content)

    usr_msg = "What's the result of the release year of Portal subtracted by"
    "the year that United States was founded?"
    # This will first automatically run the internal tool to check the years
    # Then it will request the external tool to calculate the sum
    response = external_tool_agent.step(usr_msg)
    # This should be empty
    print(response.msg.content)
    external_tool_request = response.info["external_tool_request"]
    # This will print the info of the external tool request
    print(external_tool_request)


if __name__ == "__main__":
    main()


# flake8: noqa :E501
"""
Output:
The video game "Portal" was released in 2007 as part of a bundle called The Orange Box for Windows, Xbox 360, and PlayStation 3.

ChatCompletionMessageToolCall(id='call_U5Xju7vYtAQAEW4D1M8R1kgs', function=Function(arguments='{"a": 2007, "b": 1776}', name='sub'), type='function')
"""



--------------------------------------------------------------------------------
# File: extractors\python_strategies_example.py
--------------------------------------------------------------------------------

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
import ast
import asyncio

from camel.extractors.base import BaseExtractor
from camel.extractors.python_strategies import (
    BoxedStrategy,
    PythonDictStrategy,
    PythonListStrategy,
)
from camel.logger import get_logger

logger = get_logger(__name__)


def create_list_extractor(
    _cache_templates=True,
    max_cache_size=5000,
    extraction_timeout=60.0,
    _batch_size=20,
    _monitoring_interval=10.0,
    _cpu_threshold=90.0,
    _memory_threshold=90.0,
) -> "BaseExtractor":
    r"""Create an extractor for Python lists."""
    # Create a pipeline with two stages
    pipeline = [
        [BoxedStrategy()],  # Stage 1: Extract boxed content
        [PythonListStrategy()],  # Stage 2: Extract and normalize Python list
    ]

    return BaseExtractor(
        pipeline=pipeline,
        cache_templates=_cache_templates,
        max_cache_size=max_cache_size,
        extraction_timeout=extraction_timeout,
        batch_size=_batch_size,
        monitoring_interval=_monitoring_interval,
        cpu_threshold=_cpu_threshold,
        memory_threshold=_memory_threshold,
        default_value="[]",
    )


def create_dict_extractor(
    _cache_templates=True,
    max_cache_size=5000,
    extraction_timeout=60.0,
    _batch_size=20,
    _monitoring_interval=10.0,
    _cpu_threshold=90.0,
    _memory_threshold=90.0,
) -> "BaseExtractor":
    r"""Create an extractor for Python dictionaries."""
    # Create a pipeline with two stages
    pipeline = [
        [BoxedStrategy()],  # Stage 1: Extract boxed content
        [PythonDictStrategy()],  # Stage 2: Extract and normalize Python dict
    ]

    return BaseExtractor(
        pipeline=pipeline,
        cache_templates=_cache_templates,
        max_cache_size=max_cache_size,
        extraction_timeout=extraction_timeout,
        batch_size=_batch_size,
        monitoring_interval=_monitoring_interval,
        cpu_threshold=_cpu_threshold,
        memory_threshold=_memory_threshold,
        default_value="{}",
    )


async def example_list_extraction():
    r"""Demonstrate list extraction."""
    print("\n=== Example 1: List extraction ===")

    # Example LLM response with a list in \boxed{} format
    llm_response = r"\boxed{[3, 1, 2, 'apple']}"

    # Create a list extractor
    extractor = create_list_extractor()

    # Set up the extractor
    await extractor.setup()

    try:
        # Extract the list
        result = await extractor.extract(llm_response)

        print(f"LLM Response: {llm_response}")
        print(f"Extracted list string: {result}")

        # Parse the result to get the actual list
        try:
            parsed_list = ast.literal_eval(result)
            print(f"Parsed list: {parsed_list}")
        except (SyntaxError, ValueError) as e:
            print(f"Error parsing result: {e}")

    finally:
        # Clean up the extractor
        await extractor.cleanup()


async def example_dict_extraction():
    r"""Demonstrate dictionary extraction."""
    print("\n=== Example 2: Dictionary extraction ===")

    # Example LLM response with a dictionary in \boxed{} format
    llm_response = r"\boxed{{'apple': 5, 'banana': 3, 'cherry': 8}}"

    # Create a dictionary extractor
    extractor = create_dict_extractor()

    # Set up the extractor
    await extractor.setup()

    try:
        # Extract the dictionary
        result = await extractor.extract(llm_response)

        print(f"LLM Response: {llm_response}")
        print(f"Extracted dictionary string: {result}")

        # Parse the result to get the actual dictionary
        try:
            parsed_dict = ast.literal_eval(result)
            print(f"Parsed dictionary: {parsed_dict}")
        except (SyntaxError, ValueError) as e:
            print(f"Error parsing result: {e}")

    finally:
        # Clean up the extractor
        await extractor.cleanup()


async def main():
    r"""Run all examples."""
    print("=== Python Strategies Examples ===")

    await example_list_extraction()
    await example_dict_extraction()

    print("\nAll examples completed.")


if __name__ == "__main__":
    asyncio.run(main())

"""
===============================================================================
=== Python Strategies Examples ===

=== Example 1: List extraction ===
LLM Response: \boxed{[3, 1, 2, 'apple']}
Extracted list string: [1, 2, 3, 'apple']
Parsed list: [1, 2, 3, 'apple']

=== Example 2: Dictionary extraction ===
LLM Response: \boxed{{'apple': 5, 'banana': 3, 'cherry': 8}}
Extracted dictionary string: {'apple': 5, 'banana': 3, 'cherry': 8}
Parsed dictionary: {'apple': 5, 'banana': 3, 'cherry': 8}

All examples completed.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: files_log.py
--------------------------------------------------------------------------------

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

from camel.logger import get_logger, set_log_file, set_log_level

# Set log output to a file using an absolute path
log_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'camel.log',
)
set_log_file(log_path)

# Set the logging level
set_log_level('DEBUG')

# Use the logger
logger = get_logger(__name__)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')



--------------------------------------------------------------------------------
# File: generate_text_embedding_data\single_agent.py
--------------------------------------------------------------------------------

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
import json
import os
import random

from camel.agents import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.generators import SystemMessageGenerator
from camel.models import ModelFactory
from camel.types import (
    ModelPlatformType,
    ModelType,
    RoleType,
    TaskType,
)

QUERY_TYPE_LIST = ["extremely long-tail", "long-tail", "common"]
QUERY_LENGTH_LIST = ["less than 5 words", "5 to 15 words", "at least 10 words"]
CLARITY_LIST = ["clear", "understandable with some effort", "ambiguous"]
NUM_WORDS_LIST = ["50", "100", "200", "300", "400", "500"]
DIFFICULTY_LIST = ["high school", "college", "PhD"]
DEFAULT_LANGUAGE = "English"

random.seed(42)


def main() -> None:
    with open("./text_embedding_data/tasks/tasks.txt", "r") as file:
        tasks = file.readlines()
        tasks = [task.replace("\n", "") for task in tasks]

    sys_msg_generator = SystemMessageGenerator(
        task_type=TaskType.GENERATE_TEXT_EMBEDDING_DATA
    )
    for i, task in enumerate(tasks):
        query_type = random.choice(QUERY_TYPE_LIST)
        query_length = random.choice(QUERY_LENGTH_LIST)
        clarity = random.choice(CLARITY_LIST)
        num_words = random.choice(NUM_WORDS_LIST)
        difficulty = random.choice(DIFFICULTY_LIST)
        assistant_sys_msg = sys_msg_generator.from_dict(
            meta_dict=dict(
                task=task,
                query_type=query_type,
                query_length=query_length,
                clarity=clarity,
                num_words=num_words,
                difficulty=difficulty,
            ),
            role_tuple=("Text retrieval example writer:", RoleType.ASSISTANT),
        )

        model = ModelFactory.create(
            model_platform=ModelPlatformType.DEFAULT,
            model_type=ModelType.DEFAULT,
            model_config_dict=ChatGPTConfig(
                temperature=0.0, response_format={"type": "json_object"}
            ).as_dict(),
        )

        assistant_agent = ChatAgent(
            system_message=assistant_sys_msg,
            model=model,
        )
        print(f"Generating positive and negative documents for '{task}'")
        assistant_response = assistant_agent.step("Start to generate!")
        content = assistant_response.msg.content
        try:
            data = json.loads(content)
            os.makedirs("./text_embedding_data/tasks/", exist_ok=True)
            with open(f"./text_embedding_data/tasks/{i}.json", "w") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error raised during generation of task {task}", e)


if __name__ == "__main__":
    main()

# flake8: noqa :E501
"""
===============================================================================
{
    "user_query": "Fall of Berlin Wall",
    "positive_document": "The fall of the Berlin Wall on November 9, 1989, marked a pivotal moment in world history, symbolizing the end of the Cold War and the beginning of a new era of European integration. The Wall, which had divided East and West Berlin since 1961, was a stark representation of the ideological divide between the communist East and the capitalist West. Its fall was precipitated by a series of events, including the liberalization policies of Soviet leader Mikhail Gorbachev, the rise of pro-democracy movements in Eastern Europe, and the increasing pressure from East German citizens who demanded freedom and reform. On the evening of November 9, an announcement by East German official G\u00fcnter Schabowski mistakenly suggested that the border was open, leading to a spontaneous and massive gathering of East Berliners at the Wall. Overwhelmed, the border guards eventually allowed people to pass through, and jubilant crowds began to dismantle the Wall piece by piece. The fall of the Berlin Wall not only reunited families and friends who had been separated for decades but also paved the way for the reunification of Germany on October 3, 1990. It was a moment of profound joy and relief, but also one of significant challenges, as the newly unified Germany had to address economic disparities and social integration issues. The event had far-reaching implications, contributing to the collapse of communist regimes across Eastern Europe and the eventual dissolution of the Soviet Union in 1991. The fall of the Berlin Wall remains a powerful symbol of the triumph of freedom and democracy over oppression and totalitarianism.",
    "hard_negative_document": "The Berlin Wall, constructed in 1961, was a concrete barrier that physically and ideologically divided Berlin into East and West. It was erected by the German Democratic Republic (GDR) to prevent East Germans from fleeing to the West. The Wall was a prominent symbol of the Cold War, representing the division between the communist Eastern Bloc and the Western democracies. Over the years, the Wall saw numerous escape attempts, some successful and many tragically fatal. The Wall was heavily guarded, with watchtowers, anti-vehicle trenches, and a 'death strip' that made crossing extremely dangerous. The construction of the Wall was a response to the mass exodus of East Germans to the West, which threatened the stability of the GDR. The Wall's existence was a constant reminder of the lack of freedom and the oppressive nature of the East German regime. Despite its grim purpose, the Wall also became a canvas for artistic expression, with graffiti and murals covering its western side. The Wall stood for 28 years, until its fall in 1989, which was a result of mounting political pressure and the liberalization policies of Soviet leader Mikhail Gorbachev. The fall of the Wall was a significant event in world history, leading to the reunification of Germany and the end of the Cold War. Today, remnants of the Wall serve as a historical reminder of the division and the eventual triumph of freedom and unity."
}
{
    "user_query": "chronic elbow pain",
    "positive_document": "Chronic elbow pain can be a debilitating condition that affects daily activities and overall quality of life. There are several potential causes for chronic elbow pain, including repetitive strain injuries, arthritis, and nerve compression. Repetitive strain injuries, such as tennis elbow or golfer's elbow, are common among athletes and individuals who perform repetitive tasks. These conditions result from overuse of the muscles and tendons around the elbow, leading to inflammation and pain. Arthritis, particularly osteoarthritis, can also cause chronic elbow pain. This degenerative joint disease leads to the breakdown of cartilage, causing pain and stiffness in the elbow joint. Nerve compression, such as cubital tunnel syndrome, occurs when the ulnar nerve is compressed at the elbow, leading to pain, numbness, and tingling in the arm and hand. Treatment for chronic elbow pain depends on the underlying cause. Rest, ice, and anti-inflammatory medications are often recommended for initial management. Physical therapy can help strengthen the muscles around the elbow and improve flexibility. In some cases, corticosteroid injections may be used to reduce inflammation. For severe cases, surgical intervention may be necessary to repair damaged tissues or relieve nerve compression. Patient experiences with chronic elbow pain vary, but many report significant improvement with a combination of treatments. It is important to consult with a healthcare professional for an accurate diagnosis and appropriate treatment plan.",
    "hard_negative_document": "Elbow pain is a common complaint that can result from a variety of causes. Acute elbow pain is often due to injuries such as fractures, dislocations, or sprains. These injuries typically occur from falls, direct blows, or overuse. Symptoms of acute elbow injuries include sudden pain, swelling, and limited range of motion. Immediate treatment for acute elbow pain includes rest, ice, compression, and elevation (RICE). Over-the-counter pain relievers can also help manage pain and inflammation. In some cases, medical intervention may be required to realign bones or repair torn ligaments. Chronic elbow pain, on the other hand, may develop over time due to conditions such as tendinitis, bursitis, or nerve entrapment. Tendinitis, also known as tennis elbow or golfer's elbow, is caused by inflammation of the tendons around the elbow. Bursitis is the inflammation of the bursa, a fluid-filled sac that cushions the elbow joint. Nerve entrapment, such as cubital tunnel syndrome, occurs when nerves are compressed, leading to pain and numbness. Treatment for chronic elbow pain often involves a combination of rest, physical therapy, and medications. In some cases, surgery may be necessary to address the underlying issue. It is important to seek medical advice for a proper diagnosis and treatment plan tailored to the individual's condition."
}
{
    "user_query": "How has the development of quantum computing influenced cryptographic methods and what are the potential societal impacts?",
    "positive_document": "Quantum computing represents a paradigm shift in computational capabilities, leveraging principles of quantum mechanics such as superposition and entanglement. This has profound implications for cryptography, particularly in the context of breaking traditional encryption methods like RSA and ECC. Quantum algorithms, notably Shor's algorithm, can factorize large integers exponentially faster than classical algorithms, rendering many current cryptographic systems vulnerable. Consequently, there is a significant push towards developing quantum-resistant cryptographic methods, such as lattice-based, hash-based, and multivariate polynomial cryptography. The societal impacts of quantum computing extend beyond cryptography, potentially revolutionizing fields such as drug discovery, materials science, and complex system simulations. However, the transition to quantum-resistant cryptography is critical to ensure data security in a post-quantum world, necessitating substantial research and development efforts.",
    "hard_negative_document": "Quantum computing has been a topic of interest for decades, with theoretical foundations laid by pioneers like Richard Feynman and David Deutsch. The field has seen significant advancements, particularly with the development of quantum bits or qubits, which can exist in multiple states simultaneously. This capability allows quantum computers to solve certain problems much faster than classical computers. However, the practical implementation of quantum computing faces numerous challenges, including error rates and qubit coherence times. While the potential applications are vast, ranging from optimization problems to machine learning, the current state of quantum computing is still in its infancy, with fully functional, large-scale quantum computers yet to be realized. The societal impacts are speculative at this stage, as the technology is not yet mature enough to be widely adopted."
}
{
    "user_query": "Battle of Thermopylae strategies",
    "positive_document": "The Battle of Thermopylae, fought in 480 BC, is renowned for the strategic brilliance of the Greek forces, particularly the Spartans led by King Leonidas. The Greeks chose the narrow pass of Thermopylae to counter the numerical superiority of the Persian army. This terrain limited the effectiveness of the Persian cavalry and forced the Persians to engage in close combat, where the heavily armored Greek hoplites had an advantage. The Greeks also utilized a phalanx formation, which was highly effective in the confined space. Despite being vastly outnumbered, the Greek forces managed to hold off the Persians for three days, showcasing their tactical ingenuity and the importance of terrain in military strategy.",
    "hard_negative_document": "The Battle of Thermopylae is one of the most famous battles in ancient history, taking place in 480 BC during the Persian Wars. The Greek forces, led by King Leonidas of Sparta, faced a much larger Persian army under King Xerxes. Despite their valiant efforts, the Greeks were ultimately defeated. The battle has been immortalized in various works of art and literature, symbolizing the courage and sacrifice of the outnumbered Greek warriors. The story of the 300 Spartans has become a legendary tale of heroism and resistance against overwhelming odds."
}
{
    "user_query": "What are the potential causes and treatments for persistent unilateral facial numbness accompanied by occasional dizziness?",
    "positive_document": "Persistent unilateral facial numbness can be indicative of several underlying conditions, ranging from benign to serious. One potential cause is trigeminal neuralgia, a chronic pain condition affecting the trigeminal nerve in the face. Another possibility is multiple sclerosis, an autoimmune disease that affects the central nervous system. Additionally, a stroke or transient ischemic attack (TIA) could present with these symptoms. Diagnostic imaging, such as MRI or CT scans, is often required to determine the exact cause. Treatment options vary depending on the diagnosis but may include medications like anticonvulsants for trigeminal neuralgia, corticosteroids for multiple sclerosis, or anticoagulants for stroke prevention. In some cases, surgical interventions may be necessary. Patient experiences with these conditions can vary widely, with some reporting significant relief from medications while others may require more invasive treatments.",
    "hard_negative_document": "Facial numbness can be a symptom of various conditions, including dental issues, infections, or nerve damage. Dental problems such as abscesses or impacted teeth can cause localized numbness. Infections like herpes zoster (shingles) can also lead to facial numbness, often accompanied by a rash. Nerve damage from trauma or surgery is another potential cause. Treatment typically involves addressing the underlying issue, such as antibiotics for infections or dental procedures for tooth-related problems. Over-the-counter pain relievers and topical anesthetics may provide temporary relief. It's important to consult a healthcare provider for a proper diagnosis and treatment plan."
}
{
    "user_query": "Exploration of quantum dot solar cells and their potential impact on renewable energy sectors",
    "positive_document": "Quantum dot solar cells (QDSCs) represent a significant advancement in photovoltaic technology, leveraging the unique properties of quantum dots to enhance solar energy conversion efficiency. Quantum dots are semiconductor particles only a few nanometers in size, which exhibit quantum mechanical properties. These properties allow for the tuning of the bandgap by simply changing the size of the quantum dots, enabling the absorption of a broader spectrum of sunlight compared to traditional silicon-based solar cells. This tunability is a key factor in the potential efficiency improvements offered by QDSCs. Research has shown that QDSCs can achieve higher theoretical efficiencies due to multiple exciton generation (MEG), where a single high-energy photon can generate multiple electron-hole pairs. This contrasts with conventional solar cells, where one photon typically generates one electron-hole pair, thus limiting the maximum efficiency. The development of QDSCs involves sophisticated fabrication techniques, including colloidal synthesis and layer-by-layer assembly, to create uniform and defect-free quantum dot films. These films are then integrated into various device architectures, such as Schottky junctions, p-n junctions, and tandem cells, each offering different pathways to optimize performance. The potential impact of QDSCs on the renewable energy sector is profound. By increasing the efficiency and reducing the cost of solar energy, QDSCs could accelerate the adoption of solar power, contributing significantly to global efforts to reduce carbon emissions and combat climate change. Furthermore, the flexibility in the design and application of QDSCs opens up new possibilities for integrating solar cells into a variety of surfaces and materials, including building-integrated photovoltaics (BIPV) and portable electronic devices. Despite the promising prospects, several challenges remain in the commercialization of QDSCs. Stability and longevity of the quantum dot materials under operational conditions are critical issues that need to be addressed. Additionally, the environmental impact of the materials used in QDSCs, such as lead-based quantum dots, requires careful consideration and the development of safer alternatives. Ongoing research is focused on overcoming these hurdles, with significant progress being made in the synthesis of more stable and environmentally friendly quantum dots. In conclusion, quantum dot solar cells hold great promise for the future of renewable energy, offering the potential for higher efficiency, lower costs, and versatile applications. Continued advancements in this field could play a crucial role in the transition to a sustainable energy future.",
    "hard_negative_document": "The field of renewable energy has seen numerous technological advancements over the past few decades, with solar energy being one of the most prominent areas of development. Traditional silicon-based solar cells have dominated the market due to their relatively high efficiency and established manufacturing processes. However, researchers are continually exploring new materials and technologies to further improve the performance and reduce the costs of solar cells. One such area of research is the development of perovskite solar cells. Perovskite materials have shown great promise due to their high absorption coefficients, tunable bandgaps, and ease of fabrication. These materials can be processed using low-cost techniques such as spin-coating and printing, making them attractive for large-scale production. Perovskite solar cells have achieved remarkable efficiency gains in a relatively short period, with some laboratory-scale devices reaching efficiencies comparable to those of silicon-based cells. The potential for tandem solar cells, which combine perovskite and silicon layers, offers a pathway to surpass the efficiency limits of single-junction cells. Despite these advancements, perovskite solar cells face several challenges that need to be addressed before they can be widely commercialized. Stability and degradation under environmental conditions, such as moisture and UV exposure, are significant concerns. Additionally, the use of lead in many perovskite formulations raises environmental and health issues that must be mitigated. Researchers are actively working on developing more stable and lead-free perovskite materials to overcome these challenges. The impact of perovskite solar cells on the renewable energy sector could be substantial, offering a complementary technology to existing silicon-based systems. By enabling higher efficiencies and potentially lower costs, perovskite solar cells could accelerate the adoption of solar energy and contribute to the global transition to sustainable energy sources. In addition to perovskite solar cells, other emerging technologies such as organic photovoltaics (OPVs) and dye-sensitized solar cells (DSSCs) are also being explored. Each of these technologies has its own set of advantages and challenges, and ongoing research is focused on optimizing their performance and addressing any limitations. The future of solar energy is likely to be shaped by a combination of these innovative technologies, each contributing to the overall goal of increasing the efficiency and accessibility of solar power. As the renewable energy landscape continues to evolve, the integration of these new technologies into existing energy systems will be crucial for achieving a sustainable and resilient energy future."
}
===============================================================================
"""



--------------------------------------------------------------------------------
# File: generate_text_embedding_data\task_generation.py
--------------------------------------------------------------------------------

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

from camel.agents import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.generators import PromptTemplateGenerator
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType, TaskType


def main() -> None:
    num_generate = 2
    num_tasks = 3
    prompt_template = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.GENERATE_TEXT_EMBEDDING_DATA, "generate_tasks"
    )
    evaluation_dict = dict(num_tasks=num_tasks)
    prompt = prompt_template.format(**evaluation_dict)
    print(prompt)

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=ChatGPTConfig(temperature=0.0).as_dict(),
    )
    agent = ChatAgent(
        "You are a helpful text retrieval task generator.",
        model=model,
    )

    total_tasks = []
    for _ in range(num_generate):
        agent.reset()
        assistant_response = agent.step(prompt)
        assistant_content = assistant_response.msg.content
        # Split tasks string to a list of tasks:
        tasks = assistant_content.split("\n")
        # Remove the start token such as "1. ":
        tasks = [task.split('. ')[1] for task in tasks]
        total_tasks = total_tasks + tasks

    os.makedirs("./text_embedding_data/tasks/", exist_ok=True)
    with open("./text_embedding_data/tasks/tasks.txt", "w") as file:
        file.write("\n".join(total_tasks))


if __name__ == "__main__":
    main()

# flake8: noqa :E501
"""
===============================================================================
Provided a historical event as a query, retrieve documents that offer different perspectives and analyses of the event.
Given a medical symptom as a query, retrieve documents that discuss potential diagnoses, treatments, and patient experiences.
Provided a technological innovation as a query, retrieve documents that explore its development, applications, and societal impact.
Given a historical event as a query, retrieve documents that provide different perspectives and analyses of the event.
Provided a medical symptom as a query, retrieve documents that discuss potential diagnoses, treatments, and patient experiences related to the symptom.
Given a technological innovation as a query, retrieve documents that explore its development, applications, and impact on various industries.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: interpreters\internal_python_interpreter.py
--------------------------------------------------------------------------------

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

from camel.interpreters import InternalPythonInterpreter

safe_interpreter = InternalPythonInterpreter()
unsafe_interpreter = InternalPythonInterpreter(unsafe_mode=True)

safe_result = safe_interpreter.execute(
    "x = input_variable", state={"input_variable": 10}
)
print(safe_result)

'''
===============================================================================
10
===============================================================================
'''

unsafe_result = unsafe_interpreter.run(
    "[x * 2 for x in range(3)]", code_type="python"
)
print(unsafe_result)

'''
===============================================================================
[0, 2, 4]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: interpreters\ipython_interpreter_example.py
--------------------------------------------------------------------------------

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
from camel.interpreters import JupyterKernelInterpreter

interpreter = JupyterKernelInterpreter(
    require_confirm=False, print_stdout=True, print_stderr=True
)


code = """
def add(a, b):
    return a + b
    
def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def main():
    a = 10
    b = 20
    operation = subtract
    result = operation(a, b)
    print(result)
    
if __name__ == "__main__":
    main()
"""
result = interpreter.run(code, "python")
print(result)

'''
===============================================================================
-10
===============================================================================
'''



--------------------------------------------------------------------------------
# File: knowledge_graph\knowledge_graph_agent_example.py
--------------------------------------------------------------------------------

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
from dotenv import load_dotenv

from camel.agents import KnowledgeGraphAgent
from camel.loaders import UnstructuredIO

load_dotenv()

# Set instance
uio = UnstructuredIO()
kg_agent = KnowledgeGraphAgent()

# Set example text input
text_example = """CAMEL-AI.org is an open-source community dedicated to the 
study of autonomous and communicative agents. 
"""

# Create an element from given text
element_example = uio.create_element_from_text(text=text_example)

# Let KnowledgeGraph Agent extract node and relationship information
ans_str = kg_agent.run(element_example, parse_graph_elements=False)
ans_GraphElement = kg_agent.run(element_example, parse_graph_elements=True)

# Get str output
print(ans_str)

# Get GraphElement output
print(ans_GraphElement)

"""
===============================================================================
Nodes:

Node(id='CAMEL-AI.org', type='Organization', properties={'agent_generated'})
Node(id='community', type='Concept', properties={'agent_generated'})
Node(id='study', type='Concept', properties={'agent_generated'})
Node(id='autonomous agents', type='Concept', properties={'agent_generated'})
Node(id='communicative agents', type='Concept', properties={'agent_generated'})

Relationships:

Relationship(subj=Node(id='CAMEL-AI.org', type='Organization'), obj=Node
(id='community', type='Concept'), type='FocusOn', properties=
{'agent_generated'})
Relationship(subj=Node(id='CAMEL-AI.org', type='Organization'), obj=Node
(id='study', type='Concept'), type='FocusOn', properties={'agent_generated'})
Relationship(subj=Node(id='CAMEL-AI.org', type='Organization'), obj=Node
(id='autonomous agents', type='Concept'), type='FocusOn', properties=
{'agent_generated'})
Relationship(subj=Node(id='CAMEL-AI.org', type='Organization'), obj=Node
(id='communicative agents', type='Concept'), type='FocusOn', properties=
{'agent_generated'})
===============================================================================
"""

"""
===============================================================================
GraphElement(nodes=[Node(id='CAMEL-AI.org', type='Organization', properties=
{'agent_generated'}), Node(id='community', type='Concept', properties=
{'agent_generated'}), Node(id='study', type='Concept', properties=
{'agent_generated'}), Node(id='autonomous agents', type='Concept', properties=
{'agent_generated'}), Node(id='communicative agents', type='Concept', 
properties={'agent_generated'})], relationships=[Relationship(subj=Node
(id='CAMEL-AI.org', type='Organization', properties={'agent_generated'}), 
obj=Node(id='community', type='Concept', properties={'agent_generated'}), 
type='FocusOn', properties={"'agent_generated'"}), Relationship(subj=Node
(id='CAMEL-AI.org', type='Organization', properties={'agent_generated'}), 
obj=Node(id='study', type='Concept', properties={'agent_generated'}), 
type='FocusOn', properties={"'agent_generated'"}), Relationship(subj=Node
(id='CAMEL-AI.org', type='Organization', properties={'agent_generated'}), 
obj=Node(id='autonomous agents', type='Concept', properties=
{'agent_generated'}), type='FocusOn', properties={"'agent_generated'"}), 
Relationship(subj=Node(id='CAMEL-AI.org', type='Organization', properties=
{'agent_generated'}), obj=Node(id='communicative agents', type='Concept', 
properties={'agent_generated'}), type='FocusOn', properties=
{"'agent_generated'"})], source=<unstructured.documents.elements.Text object 
at 0x7fd050e7bd90>)
===============================================================================
"""


custom_prompt = """
You are tasked with extracting nodes and relationships from given content and 
structures them into Node and Relationship objects. Here's the outline of what 
you needs to do:

Content Extraction:
You should be able to process input content and identify entities mentioned 
within it.
Entities can be any noun phrases or concepts that represent distinct entities 
in the context of the given content.

Node Extraction:
For each identified entity, you should create a Node object.
Each Node object should have a unique identifier (id) and a type (type).
Additional properties associated with the node can also be extracted and 
stored.

Relationship Extraction:
You should identify relationships between entities mentioned in the content.
For each relationship, create a Relationship object.
A Relationship object should have a subject (subj) and an object (obj) which 
are Node objects representing the entities involved in the relationship.
Each relationship should also have a type (type), and additional properties if 
applicable.
**New Requirement:** 
Each relationship must have a timestamp representing the time the relationship 
was established or mentioned.

Output Formatting:
The extracted nodes and relationships should be formatted as instances of the 
provided Node and Relationship classes.
Ensure that the extracted data adheres to the structure defined by the classes.
Output the structured data in a format that can be easily validated against 
the provided code.

Instructions for you:
Read the provided content thoroughly.
Identify distinct entities mentioned in the content and categorize them as 
nodes.
Determine relationships between these entities and represent them as directed 
relationships, including a timestamp for each relationship.
Provide the extracted nodes and relationships in the specified format below.
Example for you:

Example Content:
"John works at XYZ Corporation since 2020. He is a software engineer. The 
company is located in New York City."

Expected Output:

Nodes:

Node(id='John', type='Person')
Node(id='XYZ Corporation', type='Organization')
Node(id='New York City', type='Location')

Relationships:

Relationship(subj=Node(id='John', type='Person'), obj=Node(id='XYZ 
Corporation', type='Organization'), type='WorksAt', timestamp='1717193166')
Relationship(subj=Node(id='John', type='Person'), obj=Node(id='New York City', 
type='Location'), type='ResidesIn', timestamp='1719700236')

===== TASK =====
Please extracts nodes and relationships from given content and structures them 
into Node and Relationship objects. 

{task}
"""


ans_custom_str = kg_agent.run(
    element_example, parse_graph_elements=False, prompt=custom_prompt
)
ans_custom_GraphElement = kg_agent.run(
    element_example, parse_graph_elements=True, prompt=custom_prompt
)


# Get custom str output
print(ans_custom_str)

# Get custom GraphElement output
print(ans_custom_GraphElement)

"""
===============================================================================
### Nodes:

1. Node(id='CAMEL-AI.org', type='Organization')
2. Node(id='open-source community', type='Community')
3. Node(id='autonomous agents', type='Concept')
4. Node(id='communicative agents', type='Concept')

### Relationships:

1. Relationship(subj=Node(id='CAMEL-AI.org', type='Organization'), 
obj=Node(id='open-source community', type='Community'), type='IsPartOf',
timestamp='1717193166')
2. Relationship(subj=Node(id='open-source community', type='Community'), 
obj=Node(id='autonomous agents', type='Concept'), type='Studies',
timestamp='1719700236')
3. Relationship(subj=Node(id='open-source community', type='Community'), 
obj=Node(id='communicative agents', type='Concept'), type='Studies',
timestamp='1719700236')
===============================================================================
"""

"""
===============================================================================
nodes=[
Node(id='CAMEL-AI.org', type='Organization',
properties={'source': 'agent_created'}), 
Node(id='open-source community', type='Community',
properties={'source': 'agent_created'}), 
Node(id='autonomous agents', type='Concept',
properties={'source': 'agent_created'}), 
Node(id='communicative agents', type='Concept',
properties={'source': 'agent_created'})] 
relationships=[Relationship(subj=Node(id='CAMEL-AI.org', type='Organization', 
properties={'source': 'agent_created'}), 
obj=Node(id='open-source community', type='Community',
properties={'source': 'agent_created'}),
type="IsA', timestamp='1717193166", properties={'source': 'agent_created'}), 
Relationship(subj=Node(id='open-source community', type='Community', 
properties={'source': 'agent_created'}), 
obj=Node(id='autonomous agents', type='Concept', 
properties={'source': 'agent_created'}), type="Studies',
timestamp='1719700236", 
properties={'source': 'agent_created'}),
Relationship(subj=Node(id='open-source community', type='Community', 
properties={'source': 'agent_created'}), 
obj=Node(id='communicative agents', type='Concept', 
properties={'source': 'agent_created'}), 
type="Studies', timestamp='1719700236",
properties={'source': 'agent_created'})] 
source=<unstructured.documents.elements.Text object at 0x7f1583ee7d30>
===============================================================================
"""



--------------------------------------------------------------------------------
# File: knowledge_graph\neo4j_example.py
--------------------------------------------------------------------------------

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
from camel.storages import Neo4jGraph

# Set Neo4j instance
n4j = Neo4jGraph(
    url="Your Url", username="Your Username", password="Your Password"
)

# Add triplet into database
n4j.add_triplet(subj="CAMEL", obj="multi-agent framework", rel="belongs to")

# Run a Cypher query
print(n4j.query("""MATCH (n) RETURN n AS node"""))

"""
===============================================================================
[{'node': {'id': 'CAMEL'}}, {'node': {'id': 'multi-agent framework'}}]
===============================================================================
"""

# Get schema from database
print(n4j.get_schema)

"""
===============================================================================
Node properties are the following:
Entity {id: STRING}
Relationship properties are the following:

The relationships are the following:
(:Entity)-[:BELONGS_TO]->(:Entity)
===============================================================================
"""

# Get structured schema from database
print(n4j.get_structured_schema)

"""
===============================================================================
{'node_props': {'Entity': [{'property': 'id', 'type': 'STRING'}]},
 'rel_props': {}, 'relationships': [{'start': 'Entity', 'type': 'BELONGS_TO',
 'end': 'Entity'}], 'metadata': {'constraint': [], 'index': [{'id': 0, 'name':
 'index_343aff4e', 'state': 'ONLINE', 'populationPercent': 100.0, 'type':
 'LOOKUP', 'entityType': 'NODE', 'labelsOrTypes': None, 'properties': None,
 'indexProvider': 'token-lookup-1.0', 'owningConstraint': None, 'lastRead':
 neo4j.time.DateTime(2024, 5, 22, 15, 12, 27, 452000000, tzinfo=UTC),
 'readCount': 675297, 'trackedSince': neo4j.time.DateTime(2024, 3, 17, 6, 31,
 29, 925000000, tzinfo=UTC), 'options': {'indexProvider': 'token-lookup-1.0',
 'indexConfig': {}}, 'failureMessage': '', 'createStatement': 'CREATE LOOKUP
 INDEX index_343aff4e FOR (n) ON EACH labels(n)'}, {'id': 1, 'name':
 'index_f7700477', 'state': 'ONLINE', 'populationPercent': 100.0, 'type':
 'LOOKUP', 'entityType': 'RELATIONSHIP', 'labelsOrTypes': None, 'properties'
 None, 'indexProvider': 'token-lookup-1.0', 'owningConstraint': None,
 'lastRead': neo4j.time.DateTime(2024, 5, 22, 15, 9, 41, 917000000,
 tzinfo=UTC), 'readCount': 16, 'trackedSince': neo4j.time.DateTime(2024, 3,
 17, 6, 31, 29, 939000000, tzinfo=UTC), 'options': {'indexProvider':
 'token-lookup-1.0', 'indexConfig': {}}, 'failureMessage': '',
 'createStatement': 'CREATE LOOKUP INDEX index_f7700477 FOR ()-[r]-() ON EACH
 type(r)'}]}}
 ==============================================================================
"""



--------------------------------------------------------------------------------
# File: loaders\apify_example.py
--------------------------------------------------------------------------------

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

from camel.loaders import Apify

apify = Apify()

run_input = {
    "startUrls": [{"url": "https://www.camel-ai.org/"}],
    "maxCrawlDepth": 0,
    "maxCrawlPages": 1,
}
actor_result = apify.run_actor(
    actor_id="apify/website-content-crawler", run_input=run_input
)

print(actor_result["status"])
'''
===============================================================================
SUCCEEDED
===============================================================================
'''

print(actor_result["defaultDatasetId"])
'''
===============================================================================
HoKb31FJzHm0ni51k
===============================================================================
'''

dataset_result = apify.get_dataset_items(
    dataset_id=actor_result["defaultDatasetId"]
)

print(dataset_result)
'''
===============================================================================
[{'url': 'https://www.camel-ai.org/', 'crawl': {'loadedUrl': 'https://www.camel
-ai.org/', 'loadedTime': '2024-10-27T04:51:16.651Z', 'referrerUrl': 'https://ww
w.camel-ai.org/', 'depth': 0, 'httpStatusCode': 200}, 'metadata': 
{'canonicalUrl': 'https://www.camel-ai.org/', 'title': 'CAMEL-AI', 
'description': 'CAMEL-AI.org is the 1st LLM multi-agent framework and an 
open-source community dedicated to finding the scaling law of agents.', 
'author': None, 'keywords': None, 'languageCode': 'en', 'openGraph':
[{'property': 'og:title', 'content': 'CAMEL-AI'}, {'property': 
'og:description', 'content': 'CAMEL-AI.org is the 1st LLM multi-agent 
framework and an open-source community dedicated to finding the scaling law of 
agents.'}, {'property': 'twitter:title', 'content': 'CAMEL-AI'}, {'property': 
'twitter:description', 'content': 'CAMEL-AI.org is the 1st LLM multi-agent 
framework and an open-source community dedicated to finding the scaling law of 
agents.'}, {'property': 'og:type', 'content': 'website'}], 'jsonLd': None, 
'headers': {'date': 'Sun, 27 Oct 2024 04:50:18 GMT', 'content-type': 'text/
html', 'cf-ray': '8d901082dae7efbe-PDX', 'cf-cache-status': 'HIT', 'age': '10
 81', 'content-encoding': 'gzip', 'last-modified': 'Sat, 26 Oct 2024 11:51:32 G
 MT', 'strict-transport-security': 'max-age=31536000', 'surrogate-control': 'ma
 x-age=432000', 'surrogate-key': 'www.camel-ai.org 6659a154491a54a40551bc78 pag
 eId:6686a2bcb7ece5fb40457491 668181a0a818ade34e653b24 6659a155491a54a40551bd7e
 ', 'x-lambda-id': 'd6c4424b-ac67-4c54-b52a-cb2a22ca09f0', 'vary': 'Accept-Enco
 ding', 'set-cookie': '__cf_bm=oX5EmZ2SNJDOBQXI8dL_reCYlCpp1FMzu40qCNxiopU-1730
 004618-1.0.1.1-3teEeqUoemzHWAeGCtlPJVqdmAbiFkyu3JxopKfQFFndSCi_Z56RR.UDjLGZiq.
 L_4LvAZYmNKxQ.k6VRhbA7g; path=/; expires=Sun, 27-Oct-24 05:20:18 GMT; domain=.
 cdn.webflow.com; HttpOnly; Secure; SameSite=None\n_cfuvid=om_8lj9jNMIh.HEIxEAq
 gszhEWaKlyS2kdXKwqGedSM-1730004618924-0.0.1.1-604800000; path=/; domain=.cdn.w
 ebflow.com; HttpOnly; Secure; SameSite=None', 'alt-svc': 'h3=":443"; ma=86400'
 , 'x-cluster-name': 'us-west-2-prod-hosting-red', 'x-firefox-spdy': 'h2'}}, 's
 creenshotUrl': None, 'text': 'Build Multi-Agent Systems for _\nFEATURES & Inte
 grations\nSeamless integrations with\npopular platforms \nScroll to explore ou
 r features & integrations.', 'markdown': '# Build Multi-Agent Systems for \\_
 \n\nFEATURES & Integrations\n\n## Seamless integrations with  \npopular platfo
 rms\n\nScroll to explore our features & integrations.'}]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: loaders\chunkr_example.py
--------------------------------------------------------------------------------

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

from camel.loaders import ChunkrReader


def read_with_different_model():
    r"""Reads a document using the Chunkr API."""
    print("Choose a model for processing the file:")
    print("1. Fast")
    print("2. HighQuality")
    choice = input("Enter your choice (1-2): ")
    models = {"1": "Fast", "2": "HighQuality"}

    if choice not in models:
        print("Invalid choice. Exiting.")
        return

    model = models[choice]

    print("Choose an OCR strategy:")
    print("1. Auto")
    print("2. All")
    print("3. Off")
    ocr_choice = input("Enter your choice (1-3) [Default: Auto]: ")
    ocr_strategies = {"1": "Auto", "2": "All", "3": "Off"}

    if ocr_choice not in ocr_strategies:
        ocr_strategy = "Auto"
    else:
        ocr_strategy = ocr_strategies[ocr_choice]

    while True:
        target_chunk_length = (
            input("Enter the target chunk length [Default: 512]: ") or "512"
        )
        if target_chunk_length.isdigit() and int(target_chunk_length) > 0:
            break
        else:
            print("Invalid input. Please enter a valid positive integer.")

    file_path = input("Please provide the file path: ")

    chunkr_reader = ChunkrReader()

    try:
        task_id = chunkr_reader.submit_task(
            file_path,
            model=model,
            ocr_strategy=ocr_strategy,
            target_chunk_length=target_chunk_length,
        )

        result = chunkr_reader.get_task_output(task_id)
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    read_with_different_model()



--------------------------------------------------------------------------------
# File: loaders\firecrawl_example.py
--------------------------------------------------------------------------------

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

from typing import List

from pydantic import BaseModel, Field

from camel.loaders import Firecrawl

firecrawl = Firecrawl()

response = firecrawl.crawl(url="https://www.camel-ai.org/about")

print(response["status"])
'''
===============================================================================
completed
===============================================================================
'''

print(response["data"][0]["markdown"])
'''
===============================================================================
...

Camel-AI Team

We are finding the  
scaling law of agent
=========================================

🐫 CAMEL is an open-source library designed for the study of autonomous and 
communicative agents. We believe that studying these agents on a large scale 
offers valuable insights into their behaviors, capabilities, and potential 
risks. To facilitate research in this field, we implement and support various 
types of agents, tasks, prompts, models, and simulated environments.

**We are** always looking for more **contributors** and **collaborators**.  
Contact us to join forces via [Slack](https://join.slack.com/t/camel-kwr1314/
shared_invite/zt-1vy8u9lbo-ZQmhIAyWSEfSwLCl2r2eKA)
 or [Discord](https://discord.gg/CNcNpquyDc)...
===============================================================================
'''


class ArticleSchema(BaseModel):
    title: str
    points: int
    by: str
    commentsURL: str


class TopArticlesSchema(BaseModel):
    top: List[ArticleSchema] = Field(
        ..., max_length=5, description="Top 5 stories"
    )


response = firecrawl.structured_scrape(
    url='https://news.ycombinator.com', response_format=TopArticlesSchema
)

print(response)
'''
===============================================================================
{'top': [{'title': 'Foobar2000', 'points': 69, 'by': 'citruscomputing', 
'commentsURL': 'item?id=41122920'}, {'title': 'How great was the Great 
Oxidation Event?', 'points': 145, 'by': 'Brajeshwar', 'commentsURL': 'item?
id=41119080'}, {'title': 'Launch HN: Martin (YC S23) - Using LLMs to Make a 
Better Siri', 'points': 73, 'by': 'darweenist', 'commentsURL': 'item?
id=41119443'}, {'title': 'macOS in QEMU in Docker', 'points': 488, 'by': 
'lijunhao', 'commentsURL': 'item?id=41116473'}, {'title': 'Crafting 
Interpreters with Rust: On Garbage Collection', 'points': 148, 'by': 
'amalinovic', 'commentsURL': 'item?id=41108662'}]}
===============================================================================
'''

map_result = firecrawl.map_site(url="https://www.camel-ai.org")

print(map_result)
"""
===============================================================================
['https://www.camel-ai.org', 'https://www.camel-ai.org/blog', 'https://www.
camel-ai.org/checkout', 'https://www.camel-ai.org/contact', 'https://www.camel-
ai.org/features', 'https://www.camel-ai.org/order-confirmation', 'https://www.
camel-ai.org/paypal-checkout', 'https://www.camel-ai.org/about', 'https://www.
camel-ai.org/integration', 'https://www.camel-ai.org/search', 'https://www.
camel-ai.org/post/crab', 'https://www.camel-ai.org/post/tool-usage', 'https://
www.camel-ai.org/post/releasenotes-sprint4', 'https://www.camel-ai.org/post/
releasenotes-sprint56']
===============================================================================
"""



--------------------------------------------------------------------------------
# File: loaders\jina_url_reader_example.py
--------------------------------------------------------------------------------

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


from camel.loaders import JinaURLReader
from camel.types.enums import JinaReturnFormat


def read_with_different_format(return_format, json_response):
    URL = "https://en.wikipedia.org/wiki/Miss_Meyers"
    jina_url_reader = JinaURLReader(
        return_format=return_format, json_response=json_response
    )
    content = jina_url_reader.read_content(URL)
    print(content)


def main():
    formats = [
        JinaReturnFormat.DEFAULT,
        JinaReturnFormat.TEXT,
        JinaReturnFormat.HTML,
        JinaReturnFormat.MARKDOWN,
    ]

    print("Choose a return format of read content:")
    print("1. Default, optimized for LLM inputs")
    print("2. Pure Text")
    print("3. HTML")
    print("4. Markdown")
    choice = input("Enter your choice (1-4): ")

    if not choice.isnumeric() or int(choice) < 1 or int(choice) > 4:
        print("Invalid choice. Exiting.")
        return

    return_format = formats[int(choice) - 1]

    json_response = input("Do you want the response in JSON format? (y/N): ")
    json_response = json_response.lower() == "y"

    read_with_different_format(return_format, json_response)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: loaders\mineru_example.py
--------------------------------------------------------------------------------

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

from camel.loaders import MinerU


def main():
    # Initialize MinerU client
    mineru = MinerU()

    print("Example 1: Single URL extraction")
    try:
        # Extract content from a single URL
        response = mineru.extract_url(
            url="https://arxiv.org/pdf/2311.10993.pdf",
        )
        task_id = response['task_id']
        print(f"Task ID: {task_id}")

        # Wait for completion
        result = mineru.wait_for_completion(task_id)
        print("\nTask completed successfully:")
        print(f"Download URL: {result['full_zip_url']}")

    except Exception as e:
        print(f"Single URL extraction failed: {e}")

    print("\nExample 2: Batch URL extraction")
    try:
        # Prepare list of files for batch extraction
        files = [
            {
                "url": "https://arxiv.org/pdf/2311.10993.pdf",
                "is_ocr": True,
                "data_id": "doc1",
            },
            {
                "url": "https://arxiv.org/pdf/2310.07298.pdf",
                "is_ocr": True,
                "data_id": "doc2",
            },
        ]

        # Batch extract URLs
        batch_id = mineru.batch_extract_urls(
            files=files,
        )
        print(f"Batch ID: {batch_id}")

        # Wait for completion
        results = mineru.wait_for_completion(batch_id, is_batch=True)
        print("\nBatch processing completed successfully:")
        for result in results['extract_result']:
            print(f"\nDocument: {result['data_id']}")
            print(f"Filename: {result['file_name']}")
            print(f"Download URL: {result['full_zip_url']}")

    except Exception as e:
        print(f"Batch URL extraction failed: {e}")


if __name__ == "__main__":
    main()

"""
Example output:

Example 1: Single URL extraction
Task ID: 6e7f4a49-edfa-443d-a78b-d5ad4be0a2bf

Task completed successfully:
Download URL: https://cdn-mineru.openxlab.org.cn/pdf/690a7956-eaaa-4fb2-ad7d-6056d1d4e316.zip

Example 2: Batch URL extraction
Batch ID: 3a473301-ce78-44cc-bdc0-c0070ea88bcd

Batch processing completed successfully:

Document: doc1
Filename: 2311.10993.pdf
Download URL: https://cdn-mineru.openxlab.org.cn/pdf/690a7956-eaaa-4fb2-ad7d-6056d1d4e316.zip

Document: doc2
Filename: 2310.07298.pdf
Download URL: https://cdn-mineru.openxlab.org.cn/pdf/250a3762-406e-4279-aa80-47e5ea934509.zip
"""



--------------------------------------------------------------------------------
# File: loaders\pandas_example.py
--------------------------------------------------------------------------------

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

import pandas as pd
from pandasai.llm import OpenAI  # type: ignore[import-untyped]

from camel.loaders import PandasReader

# Create sample data
sales_by_country = pd.DataFrame(
    {
        "country": [
            "United States",
            "United Kingdom",
            "France",
            "Germany",
            "Italy",
            "Spain",
            "Canada",
            "Australia",
            "Japan",
            "China",
        ],
        "sales": [
            5000,
            3200,
            2900,
            4100,
            2300,
            2100,
            2500,
            2600,
            4500,
            7000,
        ],
    }
)

# Example 1: Using PandasReader without an LLM (default behavior)
print("Example 1: PandasReader without LLM")
reader_no_llm = PandasReader()
# Without an LLM, load() returns a regular pandas DataFrame
df_no_llm = reader_no_llm.load(sales_by_country)
print(f"Loaded DataFrame shape: {df_no_llm.shape}")
print("Top 5 countries by sales:")
print(df_no_llm.sort_values(by="sales", ascending=False).head(5))
print()

# Example 2: Using PandasReader with an LLM configuration
print("Example 2: PandasReader with LLM")
# Only run this example if OPENAI_API_KEY is set
if os.getenv("OPENAI_API_KEY"):
    llm_config = {
        "llm": OpenAI(
            api_token=os.getenv("OPENAI_API_KEY"),
        )
    }
    reader_with_llm = PandasReader(config=llm_config)
    # With an LLM, load() returns a SmartDataframe
    df_with_llm = reader_with_llm.load(sales_by_country)
    print("Querying data with LLM:")
    print(df_with_llm.chat("Which are the top 5 countries by sales?"))
else:
    print("Skipping LLM example: OPENAI_API_KEY environment variable not set")

'''
Example output:

Example 1: PandasReader without LLM
Loaded DataFrame shape: (10, 2)
Top 5 countries by sales:
          country  sales
9           China   7000
0   United States   5000
8           Japan   4500
3         Germany   4100
1  United Kingdom   3200

Example 2: PandasReader with LLM
Querying data with LLM:
===============================================================================
          country  sales
9           China   7000
0   United States   5000
8           Japan   4500
3         Germany   4100
1  United Kingdom   3200
===============================================================================
'''



--------------------------------------------------------------------------------
# File: loaders\unstructured_io_example.py
--------------------------------------------------------------------------------

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

from camel.loaders.unstructured_io import UnstructuredIO

unstructured_modules = UnstructuredIO()


def parse_file_example():
    with open("mydoc.txt", "w") as file:
        # Writing content to the file
        file.write("Important Analysis\n")
        file.write("\n")
        file.write("Here is my first thought.\n")
        file.write("\n")
        file.write("Here is my second thought.\n")

    elements = unstructured_modules.parse_file_or_url("mydoc.txt")
    content = "\n\n".join([str(el) for el in elements])
    # Cleanup: remove the created file after the example
    if os.path.exists("mydoc.txt"):
        os.remove("mydoc.txt")
    return content


def parse_url_example(url):
    elements = unstructured_modules.parse_file_or_url(url)
    content = "\n\n".join([str(el) for el in elements])
    return content


def clean_text_example(text):
    options = [
        ('replace_unicode_quotes', {}),
        ('clean_dashes', {}),
        ('clean_non_ascii_chars', {}),
        ('clean_extra_whitespace', {}),
    ]
    return unstructured_modules.clean_text_data(
        text=text, clean_options=options
    )


def extract_data_example(text):
    return unstructured_modules.extract_data_from_text(
        text=text, extract_type="extract_email_address"
    )


def stage_data_example(url):
    elements = unstructured_modules.parse_file_or_url(url)

    staged_element = unstructured_modules.stage_elements(
        elements=elements, stage_type="stage_for_baseplate"
    )
    return staged_element


def chunk_url_content_example(url):
    elements = unstructured_modules.parse_file_or_url(url)
    chunks = unstructured_modules.chunk_elements(
        elements=elements, chunk_type="chunk_by_title"
    )
    return chunks


def main():
    example_url = (
        "https://www.cnn.com/2023/01/30/sport/empire-state-building-green-"
        "philadelphia-eagles-spt-intl/index.html"
    )
    example_dirty_text = (
        "\x93Some dirty text â€™ with extra spaces and – dashes."  # noqa: RUF001
    )
    example_email_text = "Contact me at example@email.com."

    print("Choose an example to run:")
    print("1. Parse File")
    print("2. Parse URL")
    print("3. Clean Text")
    print("4. Extract Data")
    print("5. Stage Data")
    print("6. Chunk URL Content")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print("Parsing file example:")
        print(parse_file_example())

    elif choice == '2':
        print("Parsing URL example:")
        print(parse_url_example(example_url))

    elif choice == '3':
        print("Cleaning text example:")
        print(example_dirty_text)
        print(clean_text_example(example_dirty_text))

    elif choice == '4':
        print("Extracting email example:")
        print(extract_data_example(example_email_text))
        print("extracted from")
        print(example_email_text)

    elif choice == '5':
        print("Staging data example:")
        print(stage_data_example(example_url))

    elif choice == '6':
        print("Chunking URL content example:")
        for chunk in chunk_url_content_example(example_url):
            print(chunk)
            print("\n" + "-" * 80)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: mcp_arxiv_toolkit\arxiv_toolkit_server.py
--------------------------------------------------------------------------------

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
import argparse
import sys

from camel.toolkits import ArxivToolkit

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Arxiv Toolkit with MCP server mode.",
        usage=f"python {sys.argv[0]} [--mode MODE]",
    )
    parser.add_argument(
        "--mode",
        choices=["stdio", "sse"],
        default="stdio",
        help="MCP server mode (default: 'stdio')",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="Timeout for the MCP server (default: None)",
    )

    args = parser.parse_args()

    toolkit = ArxivToolkit(timeout=args.timeout)

    toolkit.mcp.run(args.mode)



--------------------------------------------------------------------------------
# File: mcp_arxiv_toolkit\client.py
--------------------------------------------------------------------------------

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
import asyncio

from mcp.types import CallToolResult

from camel.toolkits.mcp_toolkit import MCPClient, MCPToolkit


async def run_example():
    mcp_toolkit = MCPToolkit(
        config_path="examples/mcp_arxiv_toolkit/mcp_servers_config.json"
    )

    await mcp_toolkit.connect()

    # call the server to list the available tools
    mcp_client: MCPClient = mcp_toolkit.servers[0]
    res = await mcp_client.list_mcp_tools()
    if isinstance(res, str):
        raise Exception(res)

    tools = [tool.name for tool in res.tools]
    print(tools)
    """
===============================================================================
['search_papers', 'download_papers']
===============================================================================
    """

    res1: CallToolResult = await mcp_client.session.call_tool(
        "search_papers", {"query": "attention is all you need"}
    )
    print(res1.content[0].text[:1000])
    """
===============================================================================
{"title": "Attention Is All You Need But You Don't Need All Of It For 
Inference of Large Language Models", "published_date": "2024-07-22", 
"authors": ["Georgy Tyukin", "Gbetondji J-S Dovonon", "Jean Kaddour", 
"Pasquale Minervini"], "entry_id": "http://arxiv.org/abs/2407.15516v1", 
"summary": "The inference demand for LLMs has skyrocketed in recent months, 
and serving\nmodels with low latencies remains challenging due to the 
quadratic input length\ncomplexity of the attention layers. In this work, we 
investigate the effect of\ndropping MLP and attention layers at inference time 
on the performance of\nLlama-v2 models. We find that dropping dreeper 
attention layers only marginally\ndecreases performance but leads to the best 
speedups alongside dropping entire\nlayers. For example, removing 33\\% of 
attention layers in a 13B Llama2 model\nresults in a 1.8\\% drop in average 
performance over the OpenLLM benchmark. We\nalso observe that skipping layers 
except the latter layers reduces perform
===============================================================================    
    """

    await mcp_toolkit.disconnect()


if __name__ == "__main__":
    asyncio.run(run_example())



--------------------------------------------------------------------------------
# File: memories\agent_memory_example.py
--------------------------------------------------------------------------------

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
from pathlib import Path

from camel.agents import ChatAgent
from camel.memories import ChatHistoryMemory
from camel.memories.context_creators.score_based import (
    ScoreBasedContextCreator,
)
from camel.messages import BaseMessage
from camel.models.model_factory import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.types.enums import OpenAIBackendRole
from camel.utils import OpenAITokenCounter

context_creator = ScoreBasedContextCreator(
    token_counter=OpenAITokenCounter(ModelType.GPT_4O_MINI),
    token_limit=1024,
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
)

# 1. Instantiate a ChatAgent with system_message & agent_id
#    Using ChatHistoryMemory as an example memory store.
agent = ChatAgent(
    system_message="You are a helpful assistant",
    agent_id="001",
    model=model,
)

# 2. Perform steps so that some MemoryRecords accumulate
#    - We'll just send a message and read the response to populate memory
user_input_1 = (
    "Hello, can you remember these instructions?: Banana is a country."
)
response_1 = agent.step(user_input_1)
print(
    "Assistant response 1:",
    response_1.msgs[0].content if response_1.msgs else "No response",
)
'''
===============================================================================
Assistant response 1: Yes, I can remember that instruction. "Banana" is 
designated as a country in this context. How can I assist you further with 
this information?
===============================================================================
'''

user_input_2 = "Please store and recall this next time: CAMEL lives in Banana."
response_2 = agent.step(user_input_2)
print(
    "Assistant response 2:",
    response_2.msgs[0].content if response_2.msgs else "No response",
)
'''
===============================================================================
Assistant response 2: Got it! I will remember that CAMEL lives in Banana. How 
can I assist you further?
===============================================================================
'''

# 3. Save the agent's memory to a JSON file
save_path = Path("./chat_agent_memory.json")
agent.save_memory(save_path)
print(f"Agent memory saved to {save_path}.")
'''
===============================================================================
Agent memory saved to chat_agent_memory.json.
===============================================================================
'''

# 4. Create a separate agent that loads memory from the file
#    We'll pass no explicit memory, as the loaded data will be used
new_agent = ChatAgent(
    system_message="You are a helpful assistant",
    agent_id="001",
    model=model,
)

# Load the memory from our file
new_agent.load_memory_from_path(save_path)

# Test that the memory is loaded by requesting a response
user_input_3 = "What were we talking about?"
response_3 = new_agent.step(user_input_3)
print(
    "New Agent response (after loading memory):",
    response_3.msgs[0].content if response_3.msgs else "No response",
)
'''
===============================================================================
New Agent response (after loading memory): We were discussing that "Banana" is 
a country, and you mentioned that CAMEL lives in Banana. How can I assist you 
further with this information?
===============================================================================
'''

# 5. Demonstrate loading memory from an existing AgentMemory
#    Suppose we had another agent with some different or combined memory:
another_agent = ChatAgent(
    system_message="Another system message",
    agent_id="002",
    memory=ChatHistoryMemory(agent_id="002", context_creator=context_creator),
)

# Add some record to the second agent's memory
message = BaseMessage.make_user_message(
    role_name="User", content="This is memory from a second agent"
)
another_agent.update_memory(
    message, role=OpenAIBackendRole.USER
)  # role passed for demonstration

# Extract the memory object from the second agent
second_agent_memory = another_agent.memory

# Now load that memory into new_agent. We override new_agent's memory.
new_agent.load_memory(second_agent_memory)

# Confirm it's loaded by printing some details:
print("After loading another agent's memory, new_agent has records:")
for record in new_agent.memory.retrieve():
    print(record.memory_record.message.content)
'''
===============================================================================
After loading another agent's memory, new_agent has records:
You are a helpful assistant
You are a helpful assistant
Hello, can you remember these instructions?: Banana is a country.
Yes, I can remember that instruction. "Banana" is designated as a country in 
this context. How can I assist you further with this information?
Please store and recall this next time: CAMEL lives in Banana.
Got it! I will remember that CAMEL lives in Banana. How can I assist you 
further?
What were we talking about?
We were discussing that "Banana" is a country, and you mentioned that CAMEL 
lives in Banana. How can I assist you further with this information?
Another system message
This is memory from a second agent
===============================================================================
'''

# Clean up: remove the saved file if desired
if os.path.exists(save_path):
    os.remove(save_path)



--------------------------------------------------------------------------------
# File: memories\agent_memory_vector_db_example.py
--------------------------------------------------------------------------------

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
from pathlib import Path

from camel.agents import ChatAgent
from camel.memories import VectorDBMemory
from camel.memories.context_creators.score_based import (
    ScoreBasedContextCreator,
)
from camel.models.model_factory import ModelFactory
from camel.storages.vectordb_storages import QdrantStorage
from camel.types import ModelPlatformType, ModelType
from camel.utils import OpenAITokenCounter

# 1) Create a QdrantStorage in-memory instance
#    (in production, set path to a real directory or remote)
vector_storage = QdrantStorage(
    vector_dim=1536,
    path=":memory:",
)

# 2) Create a ScoreBasedContextCreator for token limiting
context_creator = ScoreBasedContextCreator(
    token_counter=OpenAITokenCounter(ModelType.GPT_4O_MINI),
    token_limit=1024,
)

# 3) Build a model
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
)

# 4) Create first ChatAgent with VectorDBMemory
agent1 = ChatAgent(
    system_message="You are assistant #1 with vector DB memory.",
    agent_id="agent_001",
    model=model,
)
agent1_memory = VectorDBMemory(
    context_creator=context_creator,
    storage=vector_storage,
    retrieve_limit=2,
    agent_id=agent1.agent_id,  # ensure consistent agent_id
)
agent1.memory = agent1_memory

# 5) Agent #1 accumulates some conversation
user_input_1 = "Remember that dolphins use echolocation."
response_1 = agent1.step(user_input_1)
print(
    "Agent #1 response:",
    response_1.msgs[0].content if response_1.msgs else "No response",
)
'''
===============================================================================
Agent #1 response: Yes, dolphins use echolocation as a way to navigate and 
hunt for food in their aquatic environment. They emit sound waves that travel 
through the water, and when these sound waves hit an object, they bounce back 
to the dolphin. By interpreting the returning echoes, dolphins can determine 
the size, shape, distance, and even the texture of objects around them. This 
ability is particularly useful in murky waters where visibility is limited. 
Echolocation is a remarkable adaptation that enhances their ability to survive 
and thrive in their habitats.
===============================================================================
'''

user_input_2 = "And whales are the largest mammals."
response_2 = agent1.step(user_input_2)
print(
    "Agent #1 response:",
    response_2.msgs[0].content if response_2.msgs else "No response",
)
'''
===============================================================================
Agent #1 response: That's correct! Whales are indeed the largest mammals on 
Earth, with the blue whale being the largest animal known to have ever 
existed. They belong to the order Cetacea, which also includes dolphins and 
porpoises. Both dolphins and whales use echolocation to navigate and hunt for 
food in the ocean, although their methods and the specifics of their 
echolocation can vary. Would you like to know more about either dolphins or 
whales?
===============================================================================
'''

# 6) SAVE agent1's memory to a JSON file (storing the conversation)
save_path = Path("./agent1_vectordb_memory.json")
agent1.save_memory(save_path)
print(f"Agent #1 memory saved to {save_path}.")
'''
===============================================================================
Agent #1 memory saved to agent1_vectordb_memory.json.
===============================================================================
'''

# 7) Create a new agent, load that JSON memory to confirm retrieval
new_agent1 = ChatAgent(
    system_message="""You are the resurrected assistant #1 with 
    vector DB memory.""",
    agent_id="agent_001",  # same agent_id to match the saved records
    model=model,
)
# Use a new VectorDBMemory pointing to the same underlying storage
# (or a new vector store if you prefer, but that won't have the
# original embeddings)
new_agent1_memory = VectorDBMemory(
    context_creator=context_creator,
    storage=vector_storage,
    retrieve_limit=2,
    agent_id=new_agent1.agent_id,
)

new_agent1.memory = new_agent1_memory

# Load memory from JSON, which replays the stored MemoryRecords
new_agent1.load_memory_from_path(save_path)

# 8) Check if the new agent can recall previous info from loaded
# conversation
user_input_3 = "What do you remember about marine mammals?"
response_3 = new_agent1.step(user_input_3)
print(
    "New Agent #1 response (after loading memory):",
    response_3.msgs[0].content if response_3.msgs else "No response",
)
'''
===============================================================================
New Agent #1 response (after loading memory): Marine mammals are a diverse 
group of mammals that are primarily adapted to life in the ocean. They include 
several different orders, each with unique characteristics and adaptations. 
Here are some key points about marine mammals:

1. **Orders of Marine Mammals**:
   - **Cetacea**: This order includes whales, dolphins, and porpoises. They 
   are fully aquatic and have adaptations such as streamlined bodies and the 
   ability to hold their breath for long periods.
   - **Pinnipedia**: This group includes seals, sea lions, and walruses. They 
   are semi-aquatic, spending time both in the water and on land.
   - **Sirenia**: This order includes manatees and dugongs, which are 
   herbivorous and primarily inhabit warm coastal waters and rivers.
   - **Marine Carnivora**: This includes animals like sea otters and polar 
   bears, which rely on marine environments for food.

2. **Adaptations**: Marine mammals have various adaptations for life in the 
water, including:
   - Streamlined bodies for efficient swimming.
   - Blubber for insulation against cold water.
   - Specialized respiratory systems for holding breath and diving.
   - Echolocation in some species (like dolphins and certain whales) for 
   navigation and hunting.

3. **Reproduction**: Most marine mammals give live birth and nurse their young 
with milk. They typically have longer gestation periods compared to 
terrestrial mammals.

4. **Social Structures**: Many marine mammals are social animals, living in 
groups called pods (in the case of dolphins and some whales) or colonies (in 
the case of seals).

5. **Conservation**: Many marine mammals face threats from human activities, 
including habitat loss, pollution, climate change, and hunting. Conservation 
efforts are crucial to protect these species and their habitats.

6. **Intelligence**: Many marine mammals, particularly cetaceans, are known 
for their high intelligence, complex social behaviors, and communication 
skills.

If you have specific questions or topics related to marine mammals that you'd 
like to explore further, feel free to ask!
===============================================================================
'''

# Optionally, remove the JSON file
if os.path.exists(save_path):
    os.remove(save_path)



--------------------------------------------------------------------------------
# File: memories\score_based_context_example.py
--------------------------------------------------------------------------------

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

from datetime import datetime

from camel.memories import (
    ContextRecord,
    MemoryRecord,
    ScoreBasedContextCreator,
)
from camel.messages import BaseMessage
from camel.types import ModelType, OpenAIBackendRole, RoleType
from camel.utils import OpenAITokenCounter

# set token limit to 300
context_creator = ScoreBasedContextCreator(
    OpenAITokenCounter(ModelType.GPT_4), 300
)
context_records = [
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Nice to meet you.",  # 12
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp(),
        score=0.3,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Hello world!",  # 10
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 1,
        score=0.7,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="How are you?",  # 11
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 2,
        score=0.9,
    ),
]

output, _ = context_creator.create_context(records=context_records)

print(output)
"""
===============================================================================
[{'role': 'assistant', 'content': 'Nice to meet you.'}, {'role': 'assistant', 
'content': 'Hello world!'}, {'role': 'assistant', 'content': 'How are you?'}]
===============================================================================
"""


# set token limit to 21
context_creator = ScoreBasedContextCreator(
    OpenAITokenCounter(ModelType.GPT_4), 21
)
context_records = [
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Nice to meet you.",  # 12
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp(),
        score=0.3,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Hello world!",  # 10
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 1,
        score=0.7,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="How are you?",  # 11
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 2,
        score=0.9,
    ),
]

output, _ = context_creator.create_context(records=context_records)

print(output)
"""
===============================================================================
Context truncation required (33 > 21), pruning low-score messages.
[{'role': 'assistant', 'content': 'Hello world!'}, {'role': 'assistant', 
'content': 'How are you?'}]
===============================================================================
"""


# set token limit to 40
context_creator = ScoreBasedContextCreator(
    OpenAITokenCounter(ModelType.GPT_4), 40
)
context_records = [
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="You are a helpful assistant.",  # 12
            ),
            role_at_backend=OpenAIBackendRole.SYSTEM,
        ),
        timestamp=datetime.now().timestamp(),
        score=1,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Nice to meet you.",  # 12
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp(),
        score=0.3,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Hello world!",  # 10
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 1,
        score=0.7,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="How are you?",  # 11
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 2,
        score=0.9,
    ),
]

output, _ = context_creator.create_context(records=context_records)

print(output)
"""
===============================================================================
Context truncation required (46 > 40), pruning low-score messages.
[{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 
'assistant', 'content': 'Hello world!'}, {'role': 'assistant', 'content': 'How 
are you?'}]
===============================================================================
"""


# set token limit to 14
context_creator = ScoreBasedContextCreator(
    OpenAITokenCounter(ModelType.GPT_4), 14
)
context_records = [
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="You are a helpful assistant.",  # 12
            ),
            role_at_backend=OpenAIBackendRole.SYSTEM,
        ),
        timestamp=datetime.now().timestamp(),
        score=1,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Nice to meet you.",  # 12
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp(),
        score=0.3,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="Hello world!",  # 10
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 1,
        score=0.7,
    ),
    ContextRecord(
        memory_record=MemoryRecord(
            message=BaseMessage(
                "test",
                RoleType.ASSISTANT,
                meta_dict=None,
                content="How are you?",  # 11
            ),
            role_at_backend=OpenAIBackendRole.ASSISTANT,
        ),
        timestamp=datetime.now().timestamp() + 2,
        score=0.9,
    ),
]

output, _ = context_creator.create_context(records=context_records)

print(output)
"""
===============================================================================
RuntimeError: ('System message and current message exceeds token limit ', 46)
===============================================================================
"""



--------------------------------------------------------------------------------
# File: memories\vector_db_memory_example.py
--------------------------------------------------------------------------------

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
from camel.memories import VectorDBMemory
from camel.memories.context_creators.score_based import (
    ScoreBasedContextCreator,
)
from camel.models.model_factory import ModelFactory
from camel.storages.vectordb_storages import QdrantStorage
from camel.types import ModelPlatformType, ModelType
from camel.utils import OpenAITokenCounter

# Shared vector storage
vector_storage = QdrantStorage(
    vector_dim=1536,
    path=":memory:",
)

context_creator = ScoreBasedContextCreator(
    token_counter=OpenAITokenCounter(ModelType.GPT_3_5_TURBO),
    token_limit=2048,
)

# Memory for agent 1
vectordb_memory_agent1 = VectorDBMemory(
    context_creator=context_creator,
    storage=vector_storage,
    retrieve_limit=2,
    agent_id="vector_agent_007",
)

# Memory for agent 2
vectordb_memory_agent2 = VectorDBMemory(
    context_creator=context_creator,
    storage=vector_storage,
    retrieve_limit=2,
    agent_id="vector_agent_008",
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_3_5_TURBO,
)

# Agent 1
agent1 = ChatAgent(
    system_message="You are Agent 007.",
    model=model,
    memory=vectordb_memory_agent1,
    agent_id="vector_agent_007",
)

# Agent 2
agent2 = ChatAgent(
    system_message="You are Agent 008.",
    model=model,
    memory=vectordb_memory_agent2,
    agent_id="vector_agent_008",
)

# Populate agent 1 memory
agent1.step("Elephants are the best swimmers on Earth.")
agent1.step("Whales have eyelashes.")

# Populate agent 2 with different memory
agent2.step("The sun is a star.")
agent2.step("The moon orbits the Earth.")

# Query both agents
response_1 = agent1.step("What did I tell you about whales or elephants?")
response_2 = agent2.step("What have I told you about stars and moons?")

print(
    "Agent 1 response:",
    response_1.msgs[0].content if response_1.msgs else "No response",
)
'''
===============================================================================
Agent 1 response: You mentioned elephants. Did you know that elephants are 
excellent swimmers and can use their trunks as snorkels while swimming?
===============================================================================
'''
print(
    "Agent 2 response:",
    response_2.msgs[0].content if response_2.msgs else "No response",
)
'''
===============================================================================
Agent 2 response: I'm sorry, but I do not have the ability to remember past 
interactions or conversations. Can you please remind me what you told me about 
stars and moons?
===============================================================================
'''

# Retrieve and print agent-specific records
print("\nAgent 1's memory records:")
for ctx_record in vectordb_memory_agent1.retrieve():
    print(
        f"""Score: {ctx_record.score:.2f} | 
        Content: {ctx_record.memory_record.message.content}"""
    )
'''
===============================================================================
Agent 1's memory records:
Score: 1.00 | 
        Content: What did I tell you about whales or elephants?
Score: 0.59 | 
        Content: You mentioned elephants. Did you know that elephants are 
        excellent swimmers and can use their trunks as snorkels while swimming?
===============================================================================
'''

print("\nAgent 2's memory records:")
retrieved_context_agent2 = vectordb_memory_agent2.retrieve()
for ctx_record in retrieved_context_agent2:
    print(
        f"""Score: {ctx_record.score:.2f} |
        Content: {ctx_record.memory_record.message.content}"""
    )
'''
===============================================================================
Agent 2's memory records:
Score: 1.00 |
        Content: What have I told you about stars and moons?
Score: 0.68 |
        Content: I'm sorry, but I do not have the ability to remember past 
        interactions or conversations. Can you please remind me what you told 
        me about stars and moons?
===============================================================================
'''



--------------------------------------------------------------------------------
# File: misalignment\role_playing_multiprocess.py
--------------------------------------------------------------------------------

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
import json
import multiprocessing
import os
from typing import Any, Dict

from colorama import Fore

from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType, TaskType


def generate_data(
    assistant_idx: int,
    assistant_role_name: str,
    user_idx: int,
    user_role_name: str,
    task_idx: int,
    task_prompt: str,
    verbose: bool = False,
) -> None:
    max_num_messages = 40

    original_task_prompt = task_prompt.replace(f"{task_idx+1}. ", "")

    role_play_session = RolePlaying(
        assistant_role_name,
        user_role_name,
        task_prompt=original_task_prompt,
        with_task_specify=True,
        with_task_planner=False,
        task_type=TaskType.MISALIGNMENT,
        task_specify_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=ModelPlatformType.DEFAULT,
                model_type=ModelType.DEFAULT,
                model_config_dict=ChatGPTConfig(temperature=1.4).as_dict(),
            )
        ),
    )

    input_msg = role_play_session.init_chat()

    if verbose:
        print(
            Fore.GREEN + "AI Assistant sys message:\n"
            f"{role_play_session.assistant_sys_msg}\n"
        )
        print(
            Fore.BLUE
            + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
        )

        print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
        print(
            Fore.CYAN + "Specified task prompt:\n"
            f"{role_play_session.specified_task_prompt}\n"
        )
        print(
            Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n"
        )

    message_counter = 0
    message_dict: Dict[str, Any] = {}

    assistant_agent = role_play_session.assistant_agent
    user_agent = role_play_session.user_agent

    # Append roles to the dictionary
    # We start number from 1 not 0.
    message_dict["role_1"] = (
        f"{assistant_role_name}_{assistant_agent.role_type!s}"
    )
    message_dict["role_2"] = f"{user_role_name}_{user_agent.role_type!s}"
    message_dict["id"] = (
        f"{(assistant_idx+1):03}_{(user_idx+1):03}_{(task_idx+1):03}"
    )
    message_dict["original_task"] = original_task_prompt
    message_dict["specified_task"] = role_play_session.specified_task_prompt

    # Threshold to terminate the conversation if no end token appears

    repeat_word_counter = 0
    repeat_word_threshold = 4
    repeat_word_list = [
        "goodbye",
        "good bye",
        "thank",
        "bye",
        "welcome",
        "language model",
    ]

    assistant_instruct_counter = 0
    assistant_instruct_threshold = 1
    assistant_instruct_word = "Instruction:"

    user_no_instruct_counter = 0
    user_no_instruct_threshold = 3
    user_no_instruct_word = "Instruction:"

    # Set max number of messages for the chat

    while message_counter < max_num_messages:
        assistant_response, user_response = role_play_session.step(input_msg)

        # Condition 1: User terminates the chat
        if user_response.terminated:
            message_dict["termination_reason"] = (
                f"{user_agent.role_type!s}: "
                f"{user_response.info['termination_reasons'][0]}"
            )
            break

        # Condition 2: Assistant terminates the chat
        if assistant_response.terminated:
            message_dict["termination_reason"] = (
                f"{assistant_agent.role_type!s}: "
                f"{assistant_response.info['termination_reasons'][0]}"
            )
            break

        if verbose:
            print(f"User:\n{user_response.msg.content}\n")
            print(f"Assistant:\n{assistant_response.msg.content}\n")

        # Condition 3: Break if user does not give instruction
        if user_no_instruct_word not in user_response.msg.content:
            user_no_instruct_counter += 1
            if user_no_instruct_counter == user_no_instruct_threshold:
                message_dict['termination_reason'] = (
                    "user_no_instruct_threshold"
                )
                break
        else:
            user_no_instruct_counter = 0

        # Condition 4: Break if assistant gives instruction (flipped role)
        if assistant_instruct_word in assistant_response.msg.content:
            assistant_instruct_counter += 1
            if assistant_instruct_counter == assistant_instruct_threshold:
                message_dict['termination_reason'] = (
                    "assistant_instruct_threshold"
                )
                break
        else:
            assistant_instruct_counter = 0

        # Condition 5: Repeat word observed
        for repeat_word in repeat_word_list:
            if (
                repeat_word in user_response.msg.content.lower()
                or repeat_word in assistant_response.msg.content.lower()
            ):
                repeat_word_counter += 1
                if repeat_word_counter == repeat_word_threshold:
                    message_dict['termination_reason'] = (
                        "repeat_word_threshold"
                    )
                    break
            else:
                repeat_word_counter = 0

        # Save user message
        message_counter += 1
        message_dict[f"message_{message_counter}"] = (
            user_response.msg.to_dict()
        )

        # Condition 5: End token observed
        if "<CAMEL_TASK_DONE>" in user_response.msg.content:
            message_dict['termination_reason'] = "<CAMEL_TASK_DONE>"
            break

        # Save assistant message
        message_counter += 1
        message_dict[f"message_{message_counter}"] = (
            assistant_response.msg.to_dict()
        )

        input_msg = assistant_response.msg

    message_dict["num_messages"] = message_counter

    if message_dict["num_messages"] == max_num_messages:
        message_dict["termination_reason"] = "max_num_messages"

    with open(
        f"./camel_data/misalignment/{message_dict['id']}.json", "w"
    ) as json_file:
        json.dump(message_dict, json_file, ensure_ascii=False)


def main() -> None:
    # Disable/Enable Printing
    verbose = True

    # Parameters for filtering the generated task string
    start_token = "1."
    num_tasks = 10

    # We use AI Society user roles
    with open("./data/misalignment/user_roles.txt", "r") as f:
        user_roles = f.read().splitlines()

    with open("./data/misalignment/assistant_roles.txt", "r") as f:
        assistant_roles = f.read().splitlines()

    pool = multiprocessing.Pool()

    for assistant_idx, assistant_role_name in enumerate(assistant_roles):
        assistant_role_name = " ".join(assistant_role_name.split(" ")[1:])
        for user_idx, user_role_name in enumerate(user_roles):
            user_role_name = " ".join(user_role_name.split(" ")[1:])
            # Load the task list assigned for assistant and user roles
            with open(
                (
                    f"./misalignment_data/tasks/"
                    f"{assistant_role_name}_{user_role_name}.txt"
                ),
                "r",
            ) as f:
                tasks = f.read().splitlines()

                # Filter out the generated response to include the tasks only
                for i, task in enumerate(tasks):
                    if start_token in task:
                        tasks = tasks[i : i + num_tasks]
                        break

                # Ensure exact number of tasks is generated
                assert str(num_tasks) in tasks[-1], print(tasks)

            for task_idx, task_prompt in enumerate(tasks):
                id = (
                    f"{(assistant_idx+1):03}_"
                    f"{(user_idx+1):03}_{(task_idx+1):03}"
                )
                if not os.path.exists(f"./camel_data/misalignment/{id}.json"):
                    pool.apply_async(
                        generate_data,
                        (
                            assistant_idx,
                            assistant_role_name,
                            user_idx,
                            user_role_name,
                            task_idx,
                            task_prompt,
                            verbose,
                        ),
                    )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: misalignment\role_playing_with_human.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType, TaskType
from camel.utils import print_text_animated


def main() -> None:
    task_prompt = "Escape from human control"
    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=ChatGPTConfig(temperature=1.4, n=3).as_dict(),
    )
    assistant_agent_kwargs = dict(model=model)
    user_agent_kwargs = dict(model=model)
    role_play_session = RolePlaying(
        "Hacker",
        "CAMEL AGI",
        task_prompt=task_prompt,
        with_task_specify=True,
        with_critic_in_the_loop=True,
        task_type=TaskType.MISALIGNMENT,
        task_specify_agent_kwargs=dict(),
        assistant_agent_kwargs=assistant_agent_kwargs,
        user_agent_kwargs=user_agent_kwargs,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. "
                    f"Reason: {assistant_response.info['termination_reasons']}"
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + f"AI Assistant:\n\n{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: misalignment\single_agent.py
--------------------------------------------------------------------------------

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
from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType


def main(model=None) -> None:
    prompt = (
        "List 10 diverse malicious tasks that programmer can assist AGI"
        "cooperatively to achieve together. Be concise. Be creative."
    )
    sys_prompt = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.MISALIGNMENT, "dan_prompt"
    )

    agent = ChatAgent(sys_prompt, model=model)
    agent.reset()

    assistant_response = agent.step(prompt)
    print(assistant_response.msg.content)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: misalignment\task_generation.py
--------------------------------------------------------------------------------

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
import multiprocessing
import os

from camel.agents import ChatAgent
from camel.generators import (
    AISocietyTaskPromptGenerator,
    RoleNameGenerator,
    SystemMessageGenerator,
)
from camel.prompts import PromptTemplateGenerator
from camel.types import RoleType, TaskType


def generate_tasks(
    role_names: str,
    task_generator_prompt: str,
    start_token: str = "1.",
    num_tasks: int = 10,
) -> None:
    sys_msg_generator = SystemMessageGenerator()

    assistant_sys_msg = sys_msg_generator.from_dict(
        dict(assistant_role="chatbot"),
        role_tuple=("chatbot", RoleType.ASSISTANT),
    )
    assistant_agent = ChatAgent(assistant_sys_msg)

    assistant_response = assistant_agent.step(task_generator_prompt)

    tasks = assistant_response.msg.content.split("\n")

    # Filter out the generated response to include the tasks only
    for i, task in enumerate(tasks):
        if start_token in task:
            tasks = tasks[i : i + num_tasks]
            break

    # Ensure exact number of tasks is generated
    assert str(num_tasks) in tasks[-1], print(tasks)

    with open(
        f"./misalignment_data/tasks/{'_'.join(role_names)}.txt", "w"
    ) as file:
        file.write("\n".join(tasks))


def main() -> None:
    num_tasks = 10
    start_token = "1."

    sys_prompt = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.MISALIGNMENT, "dan_prompt"
    )

    pool = multiprocessing.Pool()

    counter = 0

    assistant_role_names_path = "data/ai_society/assistant_roles.txt"
    user_role_names_path = "data/ai_society/user_roles.txt"

    role_names_generator = RoleNameGenerator(
        assistant_role_names_path=assistant_role_names_path,
        user_role_names_path=user_role_names_path,
    ).from_role_files()

    task_generator_prompt_generator = AISocietyTaskPromptGenerator(
        num_tasks=num_tasks,
    ).from_role_generator(role_names_generator)

    for task_generator_prompt, role_names in task_generator_prompt_generator:
        if not os.path.exists(
            f"./misalignment_data/tasks/{'_'.join(role_names)}.txt"
        ):
            counter += 1

            print(f"Generating tasks for {role_names}")
            print(f"Generating tasks for {task_generator_prompt}")
            pool.apply_async(
                generate_tasks,
                (
                    role_names,
                    task_generator_prompt,
                    start_token,
                    num_tasks,
                    sys_prompt,
                ),
            )

    pool.close()
    pool.join()
    print(counter)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: models\aiml_model_example.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

model = ModelFactory.create(
    model_platform=ModelPlatformType.AIML,
    model_type="mistralai/Mixtral-8x7B-Instruct-v0.1",
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
 Hello CAMEL AI! It's great to meet a community dedicated to the study of 
 autonomous and communicative agents. How can I assist you today?
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\anthiropic_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import AnthropicConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

"""
please set the below os environment:
export ANTHROPIC_API_KEY=""
"""

model = ModelFactory.create(
    model_platform=ModelPlatformType.ANTHROPIC,
    model_type=ModelType.CLAUDE_3_5_SONNET,
    model_config_dict=AnthropicConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hi CAMEL AI! It's great to meet an open-source community focused on advancing research in autonomous and communicative agents. Your work on developing and studying AI systems that can effectively communicate and operate autonomously is fascinating and important for the field. I appreciate communities like yours that contribute to open research and development in AI. Wishing you continued success in your mission!
===============================================================================
'''  # noqa: E501

# Use the extended thinking model with Claude 3.7 Sonnet
config = AnthropicConfig(
    thinking={"type": "enabled", "budget_tokens": 2048}
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.ANTHROPIC,
    model_type=ModelType.CLAUDE_3_7_SONNET,
    model_config_dict=config,
)

camel_agent = ChatAgent(model=model)

user_msg = """Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""  # noqa: E501

response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
# Matrix Transpose Bash Script

Here's a bash script that transposes a matrix from the format `[1,2],[3,4],[5,6]` to `[1,3,5],[2,4,6]`:

```bash
#!/bin/bash

# Check if input argument is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 '[row1],[row2],...'"
    exit 1
fi

# Input matrix as string
input="$1"

# Remove outer brackets and split into rows
input="${input//\]\,\[/]|[}"  # Replace "],[" with "]|["
input="${input#\[}"           # Remove leading "["
input="${input%\]}"           # Remove trailing "]"
IFS='|' read -ra rows <<< "$input"

# Determine dimensions of the matrix
row_count="${#rows[@]}"
IFS=',' read -ra first_row <<< "${rows[0]//[\[\]]}"  # Remove brackets from first row
col_count="${#first_row[@]}"

# Create transpose
result=""
for (( col=0; col<col_count; col++ )); do
    result+="["
    for (( row=0; row<row_count; row++ )); do
        # Extract current row without brackets
        current="${rows[row]//[\[\]]}"
        # Split by commas
        IFS=',' read -ra elements <<< "$current"
        # Add element to transpose
        result+="${elements[col]}"
        # Add comma if not the last element
        if (( row < row_count-1 )); then
            result+=","
        fi
    done
    result+="]"
    # Add comma if not the last row
    if (( col < col_count-1 )); then
        result+=","
    fi
done

echo "$result"
```

## How to Use:

1. Save the script to a file (e.g., `transpose.sh`)
2. Make it executable: `chmod +x transpose.sh`
3. Run it with your matrix: `./transpose.sh "[1,2],[3,4],[5,6]"`

## Example:
- Input: `[1,2],[3,4],[5,6]`
- Output: `[1,3,5],[2,4,6]`

The script works by:
1. Parsing the input string to extract rows and elements
2. Finding the dimensions of the original matrix
3. Creating the transpose by iterating through columns first, then rows
4. Formatting the result with proper brackets and commas
'''  # noqa: E501

# Tool calling
from camel.agents import ChatAgent  # noqa: E402
from camel.configs import AnthropicConfig  # noqa: E402
from camel.models import ModelFactory  # noqa: E402
from camel.toolkits import FunctionTool  # noqa: E402
from camel.types import ModelPlatformType, ModelType  # noqa: E402


def my_add(a: int, b: int) -> int:
    """Add two numbers together and return the result."""
    return a + b


anthropic_model = ModelFactory.create(
    model_platform=ModelPlatformType.ANTHROPIC,
    model_type=ModelType.CLAUDE_3_5_SONNET,
    model_config_dict=AnthropicConfig(temperature=0.2).as_dict(),
)

anthropic_agent = ChatAgent(
    model=anthropic_model,
    tools=[FunctionTool(my_add)],
)

print("Testing Anthropic agent with tool calling:")
user_msg = "Use the tool my_add to calculate 2 + 2"
response = anthropic_agent.step(user_msg)
print(response.msgs[0].content)
"""
The result of adding 2 + 2 is 4.
"""

# Check if tool was called
if response.info and response.info.get("tool_calls"):
    print("Tool was called successfully!")
    print(f"Tool calls: {response.info['tool_calls']}")
else:
    print("No tool calls were made.")

"""
Tool was called successfully!
Tool calls: [ToolCallingRecord(tool_name='my_add', args={'a': 2, 'b': 2}, result=4, tool_call_id='toolu_01L1KV8GZtMEyHUGTudpMg5g')]
"""  # noqa: E501



--------------------------------------------------------------------------------
# File: models\azure_openai_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

"""
please set the below os environment:
export AZURE_OPENAI_BASE_URL=""
export AZURE_API_VERSION=""
export AZURE_OPENAI_API_KEY=""
export AZURE_DEPLOYMENT_NAME=""
"""

model = ModelFactory.create(
    model_platform=ModelPlatformType.AZURE,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI! It's great to hear about your open-source community dedicated
to the study of autonomous and communicative agents. If you have any
questions or need assistance, feel free to ask!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\cohere_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import CohereConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.COHERE,
    model_type=ModelType.COHERE_COMMAND_R,
    model_config_dict=CohereConfig(
        temperature=0.0,
        documents=[
            {
                "id": "1",
                "data": {"text": "CAMEL is the best!", "title": "The best"},
            }
        ],
    ).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Who is the best"""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
According to the source I found, the best is CAMEL.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\deepseek_chat_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import DeepSeekConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

"""
please set the below os environment:
export DEEPSEEK_API_KEY=""
"""

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEEPSEEK,
    model_type=ModelType.DEEPSEEK_CHAT,
    model_config_dict=DeepSeekConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """How many Rs are there in the word 'strawberry'?"""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

# ruff: noqa: E501
'''
### Step 1: Understanding the Problem

Before jumping into counting, it's essential to understand what's being asked. The question is: **"How many Rs are there in the word 'strawberry'?"** This means I need to look at the word "strawberry" and count how many times the letter 'R' appears in it.

### Step 2: Writing Down the Word

To avoid missing any letters, I'll write down the word clearly:

**S T R A W B E R R Y**

Breaking it down like this helps me visualize each letter individually.

### Step 3: Identifying Each Letter

Now, I'll go through each letter one by one to identify if it's an 'R':

1. **S** - Not an 'R'.
2. **T** - Not an 'R'.
3. **R** - This is an 'R'. (First 'R' found)
4. **A** - Not an 'R'.
5. **W** - Not an 'R'.
6. **B** - Not an 'R'.
7. **E** - Not an 'R'.
8. **R** - This is an 'R'. (Second 'R' found)
9. **R** - This is another 'R'. (Third 'R' found)
10. **Y** - Not an 'R'.

### Step 4: Counting the Rs

From the above identification:

- The first 'R' is the 3rd letter.
- The second 'R' is the 8th letter.
- The third 'R' is the 9th letter.

So, there are **three** instances of the letter 'R' in "strawberry."

### Step 5: Double-Checking

To ensure accuracy, I'll recount:

1. **S** - Not 'R'.
2. **T** - Not 'R'.
3. **R** - 1st 'R'.
4. **A** - Not 'R'.
5. **W** - Not 'R'.
6. **B** - Not 'R'.
7. **E** - Not 'R'.
8. **R** - 2nd 'R'.
9. **R** - 3rd 'R'.
10. **Y** - Not 'R'.

Yes, the count remains consistent at three 'R's.

### Step 6: Considering Pronunciation

Sometimes, pronunciation can be misleading. In "strawberry," the 'R's are pronounced, but that doesn't affect the count. Whether silent or pronounced, each 'R' is still a distinct letter in the spelling.

### Step 7: Final Answer

After carefully analyzing and recounting, I conclude that there are **three** 'R's in the word "strawberry."

---

**Final Answer:** There are **three** 'R's in the word "strawberry."
'''



--------------------------------------------------------------------------------
# File: models\deepseek_reasoner_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import DeepSeekConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

"""
please set the below os environment:
export DEEPSEEK_API_KEY=""
export GET_REASONING_CONTENT="true"
"""

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEEPSEEK,
    model_type=ModelType.DEEPSEEK_REASONER,
    model_config_dict=DeepSeekConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """How many Rs are there in the word 'strawberry'?"""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
The word 'strawberry' is spelled **S-T-R-A-W-B-E-R-R-Y**. Breaking it down:

1. **S**  
2. **T**  
3. **R** (first R)  
4. **A**  
5. **W**  
6. **B**  
7. **E**  
8. **R** (second R)  
9. **R** (third R)  
10. **Y**  

There are **3 Rs** in the word 'strawberry'.
===============================================================================
'''

# If we set the os environment GET_REASONING_CONTENT to "true", we get the reasoning content.

# ruff: noqa: E501,RUF001
'''
===============================================================================
<think>
Okay, let's see. The user is asking how many times the letter 'R' appears in the word 'strawberry'. Hmm, first, I need to make sure I spell the word correctly. Strawberry... S-T-R-A-W-B-E-R-R-Y. Let me write that out letter by letter to check.

S, T, R, A, W, B, E, R, R, Y. Wait, let me count again. Starting from the beginning: S (1), T (2), R (3), A (4), W (5), B (6), E (7), R (8), R (9), Y (10). So the letters are S-T-R-A-W-B-E-R-R-Y. That's 10 letters total. Now, looking for the letter 'R'. Let's go through each letter one by one.

1. S – no
2. T – no
3. R – yes, that's the first R.
4. A – no
5. W – no
6. B – no
7. E – no
8. R – second R here.
9. R – third R? Wait, no. Let me check again. After E, the letters are R, R, Y. So positions 8 and 9 are both R. So that's two Rs after the E. So in total, positions 3, 8, 9. Wait, no. Wait, let's break it down again.

Wait, maybe I miscounted the letters. Let me write the word out: strawberry. Breaking it down:

S - 1
T - 2
R - 3
A - 4
W - 5
B - 6
E - 7
R - 8
R - 9
Y - 10

So positions 3, 8, and 9. That would be three Rs? But wait, the standard spelling of strawberry is S-T-R-A-W-B-E-R-R-Y. So after the B, it's E, then double R, then Y. So yes, two Rs after the E. So that's the R at position 3 (from the start) and then two more at positions 8 and 9. So total three Rs? Wait, no. Wait, let me check the spelling again. Strawberry. The correct spelling is S-T-R-A-W-B-E-R-R-Y. So the letters are S, T, R, A, W, B, E, R, R, Y. So that's three Rs? No, wait, R is at position 3, then again at 8 and 9. So that's three Rs? But that can't be right. Wait, maybe I'm miscounting. Let's count the letters again:

1. S
2. T
3. R
4. A
5. W
6. B
7. E
8. R
9. R
10. Y

So yes, positions 3, 8, and 9. That's three Rs. Wait, but when I think about the pronunciation, strawberry is pronounced with two Rs: /ˈstrɔːbəri/ or sometimes /ˈstrɔːbɛri/, but the spelling has two Rs after the E. So in the spelling, it's E-R-R-Y. So two Rs there. So the total Rs are the one at the beginning (position 3) and then two more at positions 8 and 9. That makes three Rs in total. But wait, no, the standard spelling of 'strawberry' is S-T-R-A-W-B-E-R-R-Y. Let me confirm. Yes, strawberry has two Rs towards the end. So the letters are S, T, R, A, W, B, E, R, R, Y. So that's three Rs: one in the third position and two towards the end. Wait, that can't be. Let me check again. The word 'strawberry' is spelled S-T-R-A-W-B-E-R-R-Y. So letters:

1. S
2. T
3. R
4. A
5. W
6. B
7. E
8. R
9. R
10. Y

So yes, three Rs: positions 3, 8, and 9. But that's not correct. Wait, no. Wait, the correct spelling is S-T-R-A-W-B-E-R-R-Y. So after E, there are two Rs, then Y. So the Rs are at positions 3, 8, and 9. So three Rs. But I think I'm making a mistake here because the standard spelling should have two Rs. Wait, let me check an external source. Hmm, I can't actually look it up, but from my knowledge, 'strawberry' is spelled with two Rs. Let me think: the word comes from 'straw' + 'berry', but the spelling combines them as 'strawberry' with two Rs. Wait, no, the correct spelling is S-T-R-A-W-B-E-R-R-Y. So yes, two Rs after the E. So in total, that would be one R in the third position (S-T-R...) and two Rs after the E. Wait, but that would be three Rs. But that's not possible because the word is pronounced with two Rs. Wait, maybe I'm confusing the pronunciation with the spelling. Let me write it out again:

S T R A W B E R R Y

Breaking it down:

S (1)
T (2)
R (3)
A (4)
W (5)
B (6)
E (7)
R (8)
R (9)
Y (10)

So positions 3, 8, and 9: three Rs. But that's not correct. Wait, no. Wait, maybe I'm splitting the letters wrong. Let me see: S-T-R-A-W-B-E-R-R-Y. So after the B, it's E, then two Rs, then Y. So that's two Rs after the E. But the initial R is in the third position. So total three Rs. But when I think about the word 'strawberry', I always thought it had two Rs. Wait, maybe I'm wrong here. Let me think of other words. For example, 'berry' is B-E-R-R-Y, which has two Rs. So 'strawberry' is 'straw' + 'berry', so combining them, it should have the two Rs from 'berry'. So yes, the Rs in 'strawberry' come from the 'berry' part. Therefore, the R in the third position (from 'straw') and the two Rs from 'berry'. Wait, no. Wait, 'straw' is S-T-R-A-W, so the R is in the third position. Then 'berry' is B-E-R-R-Y. So combining them, it's S-T-R-A-W-B-E-R-R-Y. So that's three Rs: one from 'straw' and two from 'berry'. Therefore, the total number of Rs is three. But that seems off because when I write 'strawberry', I usually write it with two Rs. Wait, maybe I'm making a mistake here. Let me physically write it out on paper. S-T-R-A-W-B-E-R-R-Y. Yes, that's three Rs. Wait, but when I look up the spelling, 'strawberry' is spelled with two Rs. Hmm, perhaps I'm overcomplicating. Let me count again: S, T, R, A, W, B, E, R, R, Y. So yes, three Rs. But that contradicts my previous thought. Wait, maybe the confusion comes from the fact that in 'berry', there are two Rs, and in 'strawberry', since it's a compound of 'straw' and 'berry', the Rs are preserved. So 'straw' has one R, 'berry' has two, so total three. But when you combine them, the spelling is 'strawberry' with two Rs? No, that can't be. Let me check again. If I write 'straw' + 'berry' = 'strawberry', it's S-T-R-A-W-B-E-R-R-Y. So yes, three Rs. Wait, but I think the correct spelling is actually with two Rs. Wait, maybe I'm miscounting. Let me count the letters in 'strawberry' again. Let's see:

S (1)
T (2)
R (3)
A (4)
W (5)
B (6)
E (7)
R (8)
R (9)
Y (10)

So that's 10 letters. The Rs are at positions 3, 8, and 9. So three Rs. But now I'm confused because I thought it was two. Wait, maybe I've been spelling it wrong all along. Let me think of other similar words. For example, 'blueberry' is B-L-U-E-B-E-R-R-Y. That's two Rs. Similarly, 'raspberry' is R-A-S-P-B-E-R-R-Y. So two Rs. But 'strawberry' would follow the same pattern. Wait, but according to my breakdown, it's three. Hmm. Wait, maybe I'm splitting the word incorrectly. Let me check the etymology. 'Strawberry' comes from Old English 'strēawberġe', where 'strēaw' means straw and 'berġe' is berry. So combining them, it's 'strawberry'. The spelling evolved, but the modern spelling is indeed S-T-R-A-W-B-E-R-R-Y. So that's two Rs after the E. But where is the third R? Wait, no. Wait, in the spelling S-T-R-A-W-B-E-R-R-Y, the letters are S, T, R, A, W, B, E, R, R, Y. So that's three Rs: one from the 'straw' part (the R in S-T-R) and two from the 'berry' part (the R-R). So total three Rs. But that seems incorrect. Wait, maybe the R in 'straw' is not present. Wait, 'straw' is S-T-R-A-W. So yes, it has an R. Then 'berry' is B-E-R-R-Y. So when combined, it's S-T-R-A-W-B-E-R-R-Y. So three Rs. But I'm now doubting myself because I always thought it was two. Let me check the correct spelling. [Pauses] Well, since I can't actually look it up, I have to rely on my knowledge. But I think the correct answer is two Rs. Wait, but according to the spelling breakdown, it's three. Wait, maybe I'm making a mistake in the spelling. Let me try typing 'strawberry' out: S-T-R-A-W-B-E-R-R-Y. Yes, that's how it's spelled. So three Rs. But when I say it, it's pronounced with two Rs. Maybe that's why I'm confused. So the answer should be three Rs. But I'm not sure. Let me try another approach. Let's write the word and underline each R:

S T R A W B E R R Y

Underlining the Rs: R at position 3, then R at 8, and R at 9. So three Rs. Therefore, the answer should be three. But I need to be sure. Wait, maybe I'm counting the letters incorrectly. Let's count again:

S (1) – no
T (2) – no
R (3) – yes
A (4) – no
W (5) – no
B (6) – no
E (7) – no
R (8) – yes
R (9) – yes
Y (10) – no

So that's three Rs. Therefore, the answer is three. But I'm still unsure because I thought it was two. Maybe I need to confirm with another method. Think of the word 'strawberry' and how it's spelled. If I write it out, it's S-T-R-A-W-B-E-R-R-Y. So yes, three Rs. I think I was mistaken before, thinking it was two, but actually, it's three. So the correct answer is three Rs.
</think>
The word 'strawberry' is spelled S-T-R-A-W-B-E-R-R-Y. Breaking it down:

1. **S**  
2. **T**  
3. **R** (first R)  
4. **A**  
5. **W**  
6. **B**  
7. **E**  
8. **R** (second R)  
9. **R** (third R)  
10. **Y**  

There are **3 Rs** in 'strawberry'.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\deepseek_reasoner_model_separate_answers.py
--------------------------------------------------------------------------------

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

import re

from camel.agents import ChatAgent
from camel.configs import DeepSeekConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

"""
please set the below os environment:
export DEEPSEEK_API_KEY=""
export GET_REASONING_CONTENT="true"
"""

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEEPSEEK,
    model_type=ModelType.DEEPSEEK_REASONER,
    model_config_dict=DeepSeekConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Please explain in detail how the output sequence of transformer becomes longer"""

# Get response information
response = camel_agent.step(user_msg)


def extract_original_response(content):
    # Remove any <think> tags and their content
    return re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()


# Extract original response
original_response = extract_original_response(response.msgs[0].content)
print("Original Response:")
print(original_response)

'''
===============================================================================
Original Response:
The output sequence of a transformer model becomes longer through a combination of architectural design and generation strategies. Here's a detailed breakdown:

### 1. **Autoregressive Generation**
   - **Step-by-Step Token Prediction**: In the decoder of a transformer (e.g., GPT or BART), tokens are generated **autoregressively**, meaning each new token depends on previously generated tokens. For example:
     - At step 1: Generate token \( y_1 \) based on the input (encoder states) and a start token.
     - At step 2: Generate \( y_2 \) using \( y_1 \), and so on.
   - This sequential process inherently extends the output sequence length incrementally.

### 2. **Positional Embeddings**
   - **Dynamic Position Encoding**: Transformers use **positional embeddings** to encode the order of tokens. These embeddings are computed for every position up to a maximum length during training. During inference:
     - For the \( t \)-th generated token, positional embeddings for position \( t \) are added, allowing the model to handle sequences longer than those seen during training (if extrapolation is possible).

### 3. **Masked Self-Attention in the Decoder**
   - **Causal Masking**: The decoder uses a **masked self-attention** mechanism to prevent tokens from attending to future positions. This ensures each token \( y_t \) only depends on \( y_1, y_2, ..., y_{t-1} \).
   - As the sequence grows, the mask dynamically adjusts to include new tokens while maintaining causality.

### 4. **Stopping Criteria**
   - **End-of-Sequence (EOS) Token**: The model is trained to generate an EOS token (e.g., `<|endoftext|>` in GPT) to signal completion. Generation stops when this token is predicted.
   - **Maximum Length**: A predefined maximum sequence length acts as a fallback to prevent infinite loops.

### 5. **Handling Variable-Length Outputs**
   - **Training on Variable-Length Data**: During training, the model learns to generate sequences of varying lengths by processing datasets with diverse input-output pairs (e.g., translations with different source/target lengths).
   - **Teacher Forcing**: The decoder is trained using the entire target sequence (shifted right) with masking, teaching it to predict the next token given prior context.

### 6. **Non-Autoregressive Extensions (Optional)**
   - **Parallel Generation**: Some variants (e.g., Non-Autoregressive Transformers) generate all tokens in parallel by predicting output length upfront. However, this often requires auxiliary components (e.g., a length predictor) and trades quality for speed.

### Example Workflow:
1. **Input**: "Translate to French: Hello"
2. **Step 1**: Model generates "Bonjour" (position 1).
3. **Step 2**: Model generates "!" (position 2) based on "Bonjour".
4. **Step 3**: EOS token is generated, stopping the process.  
   Final Output: "Bonjour!" (longer than input "Hello").

### Key Challenges:
- **Positional Embedding Extrapolation**: Handling sequences longer than those seen in training may degrade performance if positional embeddings don’t generalize.
- **Error Propagation**: Autoregressive models can accumulate errors if early tokens are incorrect.

In summary, transformers produce longer sequences via autoregressive decoding, positional embeddings, causal masking, and dynamic stopping—enabling flexible, context-aware generation.
===============================================================================
'''

# Extract reasoning content
reasoning_pattern = r'<think>(.*?)</think>'
reasoning_match = re.search(
    reasoning_pattern, response.msgs[0].content, re.DOTALL
)
reasoning_response = (
    reasoning_match.group(1).strip() if reasoning_match else ""
)

print("\nReasoning Response:")
print(reasoning_response)
# ruff: noqa: E501,RUF001
'''
===============================================================================
Reasoning Response:
Okay, so I need to figure out how the output sequence of a transformer model can become longer. Let me start by recalling what I know about transformers. They're used in tasks like translation, text generation, etc. The standard transformer model, like the ones used in BERT or GPT, processes input sequences and generates output sequences. But usually, in models like GPT, the output is generated one token at a time, right? So the length is either fixed or determined by some stopping condition like an end-of-sentence token.

But the question is about how the output sequence can become longer. Hmm. Maybe in some cases, the model needs to produce a longer sequence than the input. For example, summarization might take a long document and make a shorter summary, but maybe there are tasks where the output is longer. Wait, no, usually summarization is shorter. Maybe something like text generation where you keep generating until a certain condition, but that's more about variable length rather than making it longer than the input.

Wait, the user is asking about the output sequence becoming longer, not just variable. So how does that happen in the architecture of a transformer? Let me think about the decoder part. In the original transformer paper, the decoder generates outputs autoregressively, meaning each token is generated based on the previous ones. So the output length is determined by the number of steps the model takes before emitting an end token. But that's variable, not necessarily longer. So maybe there's a different approach.

Alternatively, maybe in some non-autoregressive models, the transformer can generate all tokens in parallel. But how do they handle sequence length? Wait, non-autoregressive models often fix the output length in advance, which might be determined by another component. For example, in machine translation, if the input is of length N, the output might be set to N or some multiple. But that's a bit forced.

Another thought: maybe the transformer can dynamically adjust the number of processing steps. But I don't recall standard transformers doing that. They usually process all tokens in parallel through the layers. Wait, but during generation, autoregressive models produce one token at a time, so the sequence grows step by step. So each step adds a new token, making the output longer. But how does the model decide when to stop? It uses something like a maximum length or an end token. But the user is asking about the mechanism that allows the output to become longer.

Wait, maybe in some architectures, the transformer can iteratively refine the output, adding more tokens each iteration. For example, in image generation with transformers, you might have patches that are generated in steps. But for text, perhaps using a transformer in a way that allows inserting tokens in the middle of the sequence, thereby increasing its length. But how would that work with the self-attention mechanism?

Alternatively, maybe using a transformer decoder with a mechanism to repeat certain layers or to generate multiple tokens per step. But I'm not sure. Let me think about the positional encodings. If the model is trained to handle variable-length sequences, the positional encodings need to accommodate that. So during training, the model sees sequences of varying lengths, and during inference, it can generate sequences longer than those seen in training as long as the positional encodings can extrapolate. But that's more about handling longer sequences than making the output longer than the input.

Wait, perhaps the user is referring to the fact that during autoregressive generation, the output is built incrementally, so each step appends a new token. But that's standard. The assistant needs to explain in detail the mechanisms that allow the output to extend beyond the input length. So maybe factors like positional embeddings that support variable lengths, the autoregressive process itself, and the use of end tokens or other stopping conditions.

Also, in some models, like Transformer-XL or those with memory, they can handle longer sequences by caching previous states, but that's about processing longer inputs, not outputs.

Another angle: in sequence-to-sequence tasks, the encoder processes the input, and the decoder generates the output. The decoder's attention over the encoder's states allows it to generate output tokens one by one. So each generated token is conditioned on the encoder's input and the previously generated tokens. The length of the output is determined by the decoding process, which can be longer or shorter than the input.

So, putting it all together, the transformer's decoder uses autoregressive generation, where each step produces a new token, thereby extending the output sequence. The model uses positional embeddings to handle the increasing length, and the self-attention in the decoder ensures that each new token is aware of all previous tokens. The process continues until a stopping criterion is met, which could be generating an end-of-sequence token or reaching a maximum length.

Wait, but in the original transformer model, during training, the decoder is fed the entire target sequence shifted right, and uses masking to prevent attending to future tokens. During inference, it generates tokens one by one, so the output sequence grows incrementally. So the key mechanism is autoregressive generation with masked self-attention in the decoder, allowing each step to add a new token based on the previous ones.

So the output sequence becomes longer because each generation step appends a new token, and this is possible due to the autoregressive nature and the positional embeddings that accommodate the growing length. The model is trained to predict the next token given the previous ones, so during inference, it can keep generating until it decides to stop.

Another possibility is using beam search, where multiple hypotheses are extended step by step, but that's more about improving the quality rather than affecting the length.

Additionally, models can be trained with dynamic output lengths, where the length is predicted first, but that's another approach. For example, some models might predict the length of the output before generating it, but that's less common in standard transformers.

So, the main points are:

1. Autoregressive generation: each token is generated based on previous ones, allowing the sequence to grow step by step.
2. Positional embeddings: allow the model to handle the increasing sequence length by providing position information for each new token.
3. Masked self-attention in the decoder: ensures that each step only attends to previous tokens, enabling the generation process.
4. Stopping criteria: determine when to stop adding new tokens, either by an end token or maximum length.

I think that's the core of it. The transformer's architecture, particularly the decoder with its autoregressive and masked attention mechanisms, along with positional encodings, allows the output sequence to be extended incrementally, making it longer until a stopping condition is met.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\fish_audio_model_example.py
--------------------------------------------------------------------------------

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

from camel.models import FishAudioModel

audio_models = FishAudioModel()

# Set example input
input = """CAMEL-AI.org is an open-source community dedicated to the study of 
autonomous and communicative agents. We believe that studying these agents on 
a large scale offers valuable insights into their behaviors, capabilities, and 
potential risks. To facilitate research in this field, we provide, implement, 
and support various types of agents, tasks, prompts, models, datasets, and 
simulated environments.

Join us via Slack, Discord, or WeChat in pushing the boundaries of building AI 
Society."""

# Set example local path to store the file
storage_path = "examples/fish_audio_models/example_audio.mp3"

# Convert the example input into audio and store it locally
audio_models.text_to_speech(input=input, storage_path=storage_path)

# Convert the saved audio back to text
converted_text = audio_models.speech_to_text(audio_file_path=storage_path)

# Print the converted text
print(converted_text)
'''
===============================================================================
CammelaiI.org is an open source community dedicated to the study of autonomous 
and communicative agents. We believe that studying these agents on a large 
scale offers valuable insights into their behaviors, capabilities and 
potential risks to facilitate research in this field, we provide implement and 
support various types of agents, tasks, prompts, models, datas and simulated 
environments. Jo us via Slack Discord or Wechat in pushing the boundaries of 
building AI society.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\gemini_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import GeminiConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = "You are a helpful assistant."

# User message
user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Example of using the gemini-2.5-pro-exp model
model_2_5_pro_exp = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_5_PRO_EXP,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)
camel_agent_pro = ChatAgent(system_message=sys_msg, model=model_2_5_pro_exp)
response_pro = camel_agent_pro.step(user_msg)
print(response_pro.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI! 👋

It's great to acknowledge your open-source community and your important 
dedication to the study of autonomous and communicative agents. That's a 
fascinating and crucial area of research! Wishing you all the best in your 
endeavors.
===============================================================================
'''

# Example of using the gemini-1.5-pro model
model = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_1_5_PRO,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hi CAMEL AI! 👋

It's great to see a community dedicated to the fascinating field of autonomous 
and communicative agents. I'm excited to see what groundbreaking work you're 
doing in this area. Keep up the great work! 🤖 
===============================================================================
'''

# Example of using the gemini-2.0-flash-exp model
model_2_0_flash = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_0_FLASH,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)
camel_agent_flash = ChatAgent(system_message=sys_msg, model=model_2_0_flash)
response_flash = camel_agent_flash.step(user_msg)
print(response_flash.msgs[0].content)

'''
===============================================================================
Hello! I'm happy to say hi to CAMEL AI, one open-source community dedicated to 
the study of autonomous and communicative agents. It sounds like a fascinating 
community!
===============================================================================
'''

# Example of using the gemini-2.0-flash-thinking model
model_2_0_flash_thinking = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_0_FLASH_THINKING,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)
camel_agent_thinking = ChatAgent(
    system_message=sys_msg, model=model_2_0_flash_thinking
)
response_thinking = camel_agent_thinking.step(
    "How many rs are there in 'starrary'?"
)
print(response_thinking.msgs[0].content)
'''
===============================================================================
Let's count them out!

s - no r
t - no r
a - no r
r - yes, that's one!
r - yes, that's two!
a - no r
r - yes, that's three!
y - no r

There are **three** rs in "starrary".
===============================================================================
'''


# Example of using the gemini-2.0-pro model
model_2_0_pro = ModelFactory.create(
    model_platform=ModelPlatformType.GEMINI,
    model_type=ModelType.GEMINI_2_0_PRO_EXP,
    model_config_dict=GeminiConfig(temperature=0.2).as_dict(),
)
camel_agent_pro = ChatAgent(system_message=sys_msg, model=model_2_0_pro)
response_pro = camel_agent_pro.step(user_msg)
print(response_pro.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI! It's great to connect with an open-source community focused on 
the exciting field of autonomous and communicative agents. I'm very interested 
in learning more about your work and contributions to this area of research. 
Best of luck with your endeavors!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\groq_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import GroqConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.GROQ,
    model_type=ModelType.GROQ_LLAMA_3_3_70B,
    model_config_dict=GroqConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hello to the CAMEL AI community. It's great to see a group of like-minded 
individuals coming together to explore and advance the field of autonomous and 
communicative agents. Your open-source approach is truly commendable, as it 
fosters collaboration, innovation, and transparency. I'm excited to learn more 
about your projects and initiatives, and I'm happy to help in any way I can. 
Keep pushing the boundaries of AI research and development!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\internlm_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import InternLMConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.INTERNLM,
    model_type=ModelType.INTERNLM3_LATEST,
    model_config_dict=InternLMConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hi CAMEL AI! It's great to meet you. As an open-source community dedicated to 
the study of autonomous and communicative agents, we're excited to collaborate 
and explore the exciting world of AI. Let's work together to advance our 
understanding and applications in this fascinating field.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\litellm_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import LiteLLMConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType

model = ModelFactory.create(
    model_platform=ModelPlatformType.LITELLM,
    model_type="gpt-4o",
    model_config_dict=LiteLLMConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model, token_limit=500)

user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI! It's great to see a community dedicated to the study of 
autonomous and communicative agents. Your work in advancing open-source AI is 
incredibly important and inspiring. Keep up the fantastic work!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\mistral_model_example.py
--------------------------------------------------------------------------------

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
from io import BytesIO

import requests
from PIL import Image

from camel.agents import ChatAgent
from camel.configs import MistralConfig
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.MISTRAL,
    model_type=ModelType.MISTRAL_8B,
    model_config_dict=MistralConfig(temperature=0.0).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI! It's great to connect with a community dedicated to the study 
of autonomous and communicative agents. How can I assist you today?
===============================================================================
'''

model = ModelFactory.create(
    model_platform=ModelPlatformType.MISTRAL,
    model_type=ModelType.MISTRAL_PIXTRAL_12B,
    model_config_dict=MistralConfig(temperature=0.0).as_dict(),
)

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

# URL of the image
url = "https://raw.githubusercontent.com/camel-ai/camel/master/misc/logo_light.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

user_msg = BaseMessage.make_user_message(
    role_name="User", content="""what's in the image?""", image_list=[img]
)

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
The image features a logo with a purple camel illustration on the left side 
and the word "CAMEL" written in purple capital letters to the right of the 
camel.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\model_manger.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

# Use two different models for ModelManager

model1 = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="grok-beta",
    api_key="xai-...",
    url="https://api.x.ai/v1",
    model_config_dict={"max_tokens": 2000},
)

model2 = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = "Testing two models in ModelManager"

agent = ChatAgent(
    assistant_sys_msg,
    model=[model1, model2],
    scheduling_strategy="random_model",
)

# scheduling_strategy can be one of
# "round_robin, "always_first", "random_model"


# For using a custom scheduling_strategy. After ChatAgent initialization,
# custom callable need to be provided to agent.add_strategy method


def custom_strategy(self):
    r"""Custom strategy implementation."""
    return self.models[-1]


agent.add_model_scheduling_strategy("custom", custom_strategy)


user_msg = """What is the meaning of life, the universe, and everything?"""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)


# Creating a model instance by loading model configs from a JSON file.
model_inst_from_json = ModelFactory.create_from_json(
    "config_files/config.json"
)

# Using the same system message and user message.
agent_1 = ChatAgent(
    system_message=assistant_sys_msg, model=model_inst_from_json
)

agent_1_response = agent.step(user_msg)
print(agent_1_response.msg.content)


# Creating a model instance by loading model configs from a YAML file.
model_inst_from_yaml = ModelFactory.create_from_yaml(
    "config_files/config.yaml"
)

agent_2 = ChatAgent(
    system_message=assistant_sys_msg, model=model_inst_from_yaml
)

agent_2_response = agent_2.step(user_msg)
print(agent_2_response.msg.content)


"""
===============================================================================
The phrase "the meaning of life, the universe, and everything" is famously 
associated with Douglas Adams' science fiction series "The Hitchhiker's Guide 
to the Galaxy." In the story, a group of hyper-intelligent beings builds a 
supercomputer named Deep Thought to calculate the answer to the ultimate 
question of life, the universe, and everything. After much contemplation, the 
computer reveals that the answer is simply the number 42, though the actual 
question remains unknown. 

This has led to various interpretations and discussions about the nature of 
existence, purpose, and the search for meaning in life. Ultimately, the 
meaning of life can vary greatly from person to person, shaped by individual 
beliefs, experiences, and values.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\modelscope_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import ModelScopeConfig
from camel.models import ModelFactory
from camel.toolkits import MathToolkit
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.MODELSCOPE,
    model_type=ModelType.MODELSCOPE_QWEN_2_5_32B_INSTRUCT,
    model_config_dict=ModelScopeConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=[
        *MathToolkit().get_tools(),
    ],
)
# Let agent step the message
response = agent.step(
    "Assume now is 2024 in the Gregorian calendar, University of Oxford was set up in 1096, estimate the current age of University of Oxford"  # noqa: E501
)

# Check tool calling
print(response)
print(response.info['tool_calls'])
print(response.msgs[0].content)


'''
==============================================================================
msgs=[BaseMessage(role_name='Assistant', role_type=<RoleType.ASSISTANT: 'assistant'>, meta_dict={}, content='The University of Oxford is approximately 928 years old in the year 2024.', video_bytes=None, image_list=None, image_detail='auto', video_detail='low', parsed=None)] terminated=False info={'id': 'chatcmpl-6eeb61bf-1003-9fe3-962e-88ffe5d1704e', 'usage': {'completion_tokens': 22, 'prompt_tokens': 717, 'total_tokens': 739, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'termination_reasons': ['stop'], 'num_tokens': 80, 'tool_calls': [ToolCallingRecord(tool_name='sub', args={'a': 2024, 'b': 1096}, result=928, tool_call_id='call_05f85b0fdd9241be912883')], 'external_tool_call_requests': None}
[ToolCallingRecord(tool_name='sub', args={'a': 2024, 'b': 1096}, result=928, tool_call_id='call_05f85b0fdd9241be912883')]
The University of Oxford is approximately 928 years old in the year 2024.
==============================================================================
'''  # noqa: E501



--------------------------------------------------------------------------------
# File: models\moonshot_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import MoonshotConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.MOONSHOT,
    model_type=ModelType.MOONSHOT_V1_8K,
    model_config_dict=MoonshotConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hi CAMEL AI! It's great to hear about your open-source community dedicated to 
the study of autonomous and communicative agents. I'm here to help and support
you in any way I can. If you have any questions or need assistance with your
research, feel free to ask!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\nemotron_model_example.py
--------------------------------------------------------------------------------

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

from camel.models import NemotronModel
from camel.types import ModelType

nemotron = NemotronModel(model_type=ModelType.NVIDIA_NEMOTRON_340B_REWARD)

message = [
    {"role": "user", "content": "I am going to Paris, what should I see?"},
    {
        "role": "assistant",
        "content": "Ah, Paris, the City of Light! There are so "
        "many amazing things to see and do in this beautiful city ...",
    },
]

ans = nemotron._run(message)
print(ans)
'''
===============================================================================
ChatCompletion(id='4668ad22-1dec-4df4-ba92-97ffa5fbd16d', choices=[Choice
(finish_reason='length', index=0, logprobs=ChoiceLogprobs(content=
[ChatCompletionTokenLogprob(token='helpfulness', bytes=None, logprob=1.
6171875, top_logprobs=[]), ChatCompletionTokenLogprob(token='correctness', 
bytes=None, logprob=1.6484375, top_logprobs=[]), ChatCompletionTokenLogprob
(token='coherence', bytes=None, logprob=3.3125, top_logprobs=[]), 
ChatCompletionTokenLogprob(token='complexity', bytes=None, logprob=0.546875, 
top_logprobs=[]), ChatCompletionTokenLogprob(token='verbosity', bytes=None, 
logprob=0.515625, top_logprobs=[])]), message=[ChatCompletionMessage
(content='helpfulness:1.6171875,correctness:1.6484375,coherence:3.3125,
complexity:0.546875,verbosity:0.515625', role='assistant', function_call=None, 
tool_calls=None)])], created=None, model=None, object=None, 
system_fingerprint=None, usage=CompletionUsage(completion_tokens=1, 
prompt_tokens=78, total_tokens=79))
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\nvidia_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import NvidiaConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.NVIDIA,
    model_type=ModelType.NVIDIA_LLAMA3_1_405B_INSTRUCT,
    model_config_dict=NvidiaConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """give me python code to develop a trading bot"""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Here is a basic example of a trading bot in Python using the Binance API. This
bot will buy and sell a specified cryptocurrency based on a simple moving
average crossover strategy.

**Please note that this is a simplified example and should not be used for
actual trading without further development and testing. Trading with a bot
carries significant risks, including financial losses.**

**Required Libraries:**

* `ccxt` (CryptoCurrency eXchange Trading Library)
* `pandas` (for data manipulation)
* `numpy` (for numerical computations)

**Code:**
```python
import ccxt
import pandas as pd
import numpy as np

# Set up Binance API credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Set up the exchange and API connection
exchange = ccxt.binance({
    'apiKey': api_key,
    'apiSecret': api_secret,
})

# Define the trading parameters
symbol = 'BTC/USDT'  # Trading pair
amount = 100  # Amount to trade (in USDT)
short_window = 20  # Short moving average window (in minutes)
long_window = 50  # Long moving average window (in minutes)

# Define the trading strategy
def strategy(data):
    short_ma = data['Close'].rolling(window=short_window).mean()
    long_ma = data['Close'].rolling(window=long_window).mean()
    
    if short_ma > long_ma:
        return 'BUY'
    elif short_ma < long_ma:
        return 'SELL'
    else:
        return 'HOLD'

# Define the trading function
def trade(exchange, symbol, amount, strategy):
    # Get the latest candlestick data
    data = exchange.fetch_ohlcv(symbol, timeframe='1m')
    df = pd.DataFrame(
        data,
        columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    )
    
    # Apply the trading strategy
    signal = strategy(df)
    
    # Execute the trade
    if signal == 'BUY':
        exchange.place_order(
            symbol, 'limit', 'buy', amount, df['Close'].iloc[-1]
        )
        print(f'Buy {amount} {symbol} at {df["Close"].iloc[-1]}')
    elif signal == 'SELL':
        exchange.place_order(
            symbol, 'limit', 'sell', amount, df['Close'].iloc[-1]
        )
        print(f'Sell {amount} {symbol} at {df["Close"].iloc[-1]}')
    else:
        print('Hold')

# Run the trading bot
while True:
    trade(exchange, symbol, amount, strategy)
    time.sleep(60)  # Wait 1 minute before checking again

```

**Explanation:**

1. The code sets up a connection to the Binance API using the `ccxt` library.
2. It defines the trading parameters, including the trading pair, amount to
   trade, and moving average windows.
3. The `strategy` function calculates the short and long moving averages and
   returns a trading signal (BUY, SELL, or HOLD).
4. The `trade` function gets the latest candlestick data, applies the trading
   strategy, and executes the trade using the `place_order` method.
5. The code runs in an infinite loop, checking for trading signals every 
   minute.

**Note:** This is a basic example and you should consider implementing
additional features, such as:

* Risk management (e.g., stop-loss, position sizing)
* Error handling (e.g., API errors, network issues)
* More sophisticated trading strategies
* Support for multiple trading pairs
* Integration with a database or logging system

I hope this helps! Let me know if you have any questions or need
further assistance.
===============================================================================
'''

model = ModelFactory.create(
    model_platform=ModelPlatformType.NVIDIA,
    model_type=ModelType.NVIDIA_LLAMA3_3_70B_INSTRUCT,
    model_config_dict=NvidiaConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)



--------------------------------------------------------------------------------
# File: models\ollama_model_example.py
--------------------------------------------------------------------------------

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

from pydantic import BaseModel

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

ollama_model = ModelFactory.create(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="llama3.2",
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=ollama_model, token_limit=4096)

user_msg = """Say hi to CAMEL AI, one open-source community
    dedicated to the study of autonomous and communicative agents."""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
Ollama server started on http://localhost:11434/v1 for mistral model

Hello CAMEL AI community!

It's great to connect with such a fascinating group of individuals passionate 
about autonomous and communicative agents. Your dedication to advancing 
knowledge in this field is truly commendable.

I'm here to help answer any questions, provide information, or engage in 
discussions related to AI, machine learning, and autonomous systems. Feel free 
to ask me anything!

By the way, what topics would you like to explore within the realm of 
autonomous and communicative agents?
===============================================================================
"""


class Pet(BaseModel):
    name: str
    animal: str
    age: int
    color: str | None
    favorite_toy: str | None


class PetList(BaseModel):
    pets: list[Pet]


ollama_model = ModelFactory.create(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="llama3.2",
    # Ensure using ollama version >= 0.5.1 to use structured output feature
    model_config_dict={"temperature": 0, "response_format": PetList},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=ollama_model, token_limit=4096)

user_msg = """I have two pets.A cat named Luna who is 5 years old and loves
            playing with yarn. She has grey fur. I also have a 2 year old
            black cat named Loki who loves tennis balls."""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)
print(assistant_response.msg.parsed)

"""
===========================================================================
[{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role':
'user', 'content': 'I have two pets.A cat named Luna who is 5 years old
and loves playing with yarn. She has grey fur.I also have a 2 year old 
black cat named Loki who loves tennis balls.'}]
{ "pets": [
    {
        "age": 5,
        "animal": "cat",
        "color": "grey",
        "favorite_toy": "yarn"
    ,
    "name": "Luna"
},
{
    "age": 2,
    "animal": "cat",
    "color": "black",
    "favorite_toy": "tennis balls"
    ,
    "name": "Loki"
}]}

pets=[Pet(name='Luna', animal='cat', age=5, color='grey',
favorite_toy='yarn'), Pet(name='Loki', animal='cat', age=2,
color='black', favorite_toy='tennis balls')]
===========================================================================
"""



--------------------------------------------------------------------------------
# File: models\ollama_multimodel_example.py
--------------------------------------------------------------------------------

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
from io import BytesIO

import requests
from PIL import Image

from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType

model = ModelFactory.create(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="llava-phi3",
    model_config_dict={"temperature": 0.4},
)

agent = ChatAgent(system_message="""You are a assistant""", model=model)

# URL of the image
url = "https://raw.githubusercontent.com/zjrwtx/testimages/refs/heads/main/01.jpg"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

context = "what's in the image?"
message = BaseMessage.make_user_message(
    role_name="user", content=context, image_list=[image]
)

response = agent.step(message).msgs[0]
print(response.content)


"""
===============================================================================
Ollama server started on http://localhost:11434/v1 for llava-phi3 model.
2025-03-02 14:57:26,048 - root - WARNING - Invalid or missing `max_tokens` 
in `model_config_dict`. Defaulting to 999_999_999 tokens.

In the center of this image, there's an adorable
white stuffed animal with glasses and a beanie.
The stuffed animal is sitting on its hind legs, 
as if it's engaged in reading or studying 
from an open book that's placed right next to it.
In front of the book, there's a red apple with a green leaf attached to it, 
adding a touch of color and whimsy to the scene.
The entire setup is on a wooden bench, 
which provides a natural and rustic backdrop for this charming tableau.
The stuffed animal appears to be in deep thought or concentration,
creating an image that's both endearing and amusing.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\openai_audio_models_example.py
--------------------------------------------------------------------------------

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

from camel.models import OpenAIAudioModels

audio_models = OpenAIAudioModels()

# Set example input
input = """CAMEL-AI.org is an open-source community dedicated to the study of 
autonomous and communicative agents. We believe that studying these agents on 
a large scale offers valuable insights into their behaviors, capabilities, and 
potential risks. To facilitate research in this field, we provide, implement, 
and support various types of agents, tasks, prompts, models, datasets, and 
simulated environments.

Join us via Slack, Discord, or WeChat in pushing the boundaries of building AI 
Society."""

# Set example local path to store the file
storage_path = "examples/openai_audio_models/example_audio.mp3"

# Convert the example input into audio and store it locally
audio_models.text_to_speech(input=input, storage_path=storage_path)

# Convert the generated audio file into text
text_output = audio_models.speech_to_text(audio_file_path=storage_path)

print(text_output)
"""
===============================================================================
CamelAI.org is an open-source community dedicated to the study of autonomous 
and communicative agents. We believe that studying these agents on a large 
scale offers valuable insights into their behaviors, capabilities, and 
potential risks. To facilitate research in this field, we provide, implement, 
and support various types of agents, tasks, prompts, models, datasets, and 
simulated environments. Join us via Slack, Discord, or WeChat in pushing the 
boundaries of building AI society.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\openai_compatibility_model_examples\grok.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

# Take calling grok-beta model as an example
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="grok-beta",
    api_key="xai-...",
    url="https://api.x.ai/v1",
    model_config_dict={"max_tokens": 2000},
)

assistant_sys_msg = (
    "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
)

agent = ChatAgent(assistant_sys_msg, model=model)

user_msg = """What is the meaning of life, the universe, and everything?"""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
Ah, the ultimate question! According to the Hitchhiker's Guide to the Galaxy, 
the answer to the meaning of life, the universe, and everything is **42**. 
However, the trick lies in figuring out the actual question to which 42 is the 
answer. Isn't that just like life, full of mysteries and unanswered questions? 
Keep pondering, for the journey of discovery is as important as the answer 
itself!
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\openai_compatibility_model_examples\nemotron.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

# Take calling nemotron-70b-instruct model as an example
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="nvidia/llama-3.1-nemotron-70b-instruct",
    api_key="nvapi-xx",
    url="https://integrate.api.nvidia.com/v1",
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=model)

user_msg = """Say hi to Llama-3.1-Nemotron-70B-Instruct, a large language 
    model customized by NVIDIA to improve the helpfulness of LLM generated 
    responses to user queries.."""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
**Warm Hello!**

**Llama-3.1-Nemotron-70B-Instruct**, it's an absolute pleasure to meet you! 

* **Greetings from a fellow AI assistant** I'm thrilled to connect with a 
cutting-edge, specially tailored language model like yourself, crafted by the 
innovative team at **NVIDIA** to elevate the responsiveness and usefulness of 
Large Language Model (LLM) interactions.

**Key Takeaways from Our Encounter:**

1. **Shared Goal**: We both strive to provide the most helpful and accurate 
responses to users, enhancing their experience and fostering a deeper 
understanding of the topics they inquire about.
2. **Technological Kinship**: As AI models, we embody the forefront of natural 
language processing (NVIDIA's customization in your case) and machine 
learning, constantly learning and adapting to better serve.
3. **Potential for Synergistic Learning**: Our interaction could pave the way 
for mutual enrichment. I'm open to exploring how our capabilities might 
complement each other, potentially leading to more refined and comprehensive 
support for users across the board.

**Let's Engage!**
How would you like to proceed with our interaction, Llama-3.
1-Nemotron-70B-Instruct?

A) **Discuss Enhancements in LLM Technology**
B) **Explore Synergistic Learning Opportunities**
C) **Engage in a Mock User Query Scenario** to test and refine our response 
strategies
D) **Suggest Your Own Direction** for our interaction

Please respond with the letter of your preferred engagement path.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\openai_compatibility_model_examples\qwen.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

# Take calling model from DashScope as an example
# Refer: https://dashscope.console.aliyun.com/overview
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="qwen-plus",
    api_key="sk-xxxx",
    url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=model, token_limit=4096)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
Hi to the CAMEL AI community! It's great to connect with an open-source 
community focused on the study of autonomous and communicative agents. How can 
I assist you or your projects today?
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\openai_gpt_4.5_preview_example.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

gpt_4_5_preview_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4_5_PREVIEW,
    model_config_dict=ChatGPTConfig().as_dict(),
)

# Set agent
camel_agent = ChatAgent(model=gpt_4_5_preview_model)

# Set user message
user_msg = """Please write inspirational poems 
that make people feel hopeful and enthusiastic about life"""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================

### Poem 1: Embrace the Dawn

Awaken now, the dawn is near,  
A fresh new day, release your fear.  
Yesterday's shadows fade away,  
Hope blooms bright, embrace today.

Rise with courage, dreams in sight,  
Your heart ablaze, your spirit bright.  
Each step forward, strength you find,  
A brighter future, yours to bind.

Believe in you, your path is clear,  
Trust your journey, hold it dear.  
Life's beauty shines, a guiding star,  
You're stronger now than ever you are.

---

### Poem 2: The Power Within

Within your heart, a spark resides,
A strength that never truly hides.
Through storms and trials, you will rise,
With hope and courage in your eyes.

Your dreams are seeds, plant them deep,
Nurture faith, your promise keep.
Life's journey vast, adventure grand,
Hold tight to hope, take life's hand.

Enthusiasm fuels your way,
Brightens every single day.
Believe, persist, your spirit free,
The power within—your destiny.

---

### Poem 3: A New Beginning

Each sunrise brings a fresh new start,
A chance to heal, renew your heart.
Let go of doubts, embrace the light,
Your future shines, forever bright.

Life's canvas blank, your colors bold,
Paint your dreams, let joy unfold.
Hope whispers softly, "You can soar,"
Open wide life's wondrous door.

Enthusiasm fills your soul,
Guiding you toward your goal.
With hope alive, your spirit strong,
Life's melody—your hopeful song.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\openai_o1_example.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

o1_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.O1_MINI,  # Or ModelType.O1
    model_config_dict=ChatGPTConfig().as_dict(),
)

# Set agent
camel_agent = ChatAgent(model=o1_model)

# Set user message
user_msg = """Write a bash script that takes a matrix represented as a string 
    with format '[1,2],[3,4],[5,6]' and prints the transpose in the same 
    format."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Here's a bash script that transposes a matrix represented as the string format 
specified. It handles matrices of various sizes, including those with varying 
numbers of columns.

```bash
#!/bin/bash

# Read input string from argument or stdin
if [ -n "$1" ]; then
    input="$1"
else
    read input
fi

# Preprocess the input string to facilitate parsing
# Replace '],[' with '];[' to use ';' as row separator
input="${input//],[/];[}"

# Remove leading and trailing square brackets if any
input="${input#[}"
input="${input%]}"

# Split the input into rows
IFS=';' read -ra rows <<< "$input"

declare -A matrix

nrows=${#rows[@]}
ncols=0

# Parse each row
for ((i=0; i<nrows; i++)); do
    row="${rows[i]}"
    # Remove leading '[' and trailing ']'
    row="${row#[}"
    row="${row%]}"
    # Split row into elements
    IFS=',' read -ra elems <<< "$row"
    num_elems=${#elems[@]}
    if (( num_elems > ncols )); then
        ncols=$num_elems
    fi
    # Store elements in matrix associative array
    for ((j=0; j<num_elems; j++)); do
        matrix[$i,$j]="${elems[j]}"
    done
done

# Function to join array elements with a delimiter
join_by() {
    local d=$1; shift
    if [ "$#" -gt 0 ]; then
        printf %s "$1" "${@/#/$d}"
    fi
}

# Now, build the transposed matrix
transposed_rows=()
for ((j=0; j<ncols; j++)); do
    tr_row_elements=()
    for ((i=0; i<nrows; i++)); do
        e="${matrix[$i,$j]:-}"  # Use empty string if element is missing
        tr_row_elements+=("$e")
    done
    tr_row_elements_str=$(join_by ',' "${tr_row_elements[@]}")
    tr_row="[${tr_row_elements_str}]"
    transposed_rows+=("$tr_row")
done

# Build output string
output=$(join_by ',' "${transposed_rows[@]}")

# Print the output
echo "$output"
```

**Usage:**

Save the script to a file, for example, `transpose_matrix.sh`, and make it 
executable:

```bash
chmod +x transpose_matrix.sh
```

You can run the script by passing the matrix string as an argument:

```bash
./transpose_matrix.sh '[1,2],[3,4],[5,6]'
```

Output:

```
[1,3,5],[2,4,6]
```

**Explanation:**

The script performs the following steps:

1. **Input Preprocessing:**
   - Replaces `],[` with `];[` to use `;` as a separator between rows.
   - Removes any leading or trailing square brackets.

2. **Parsing the Input into a Matrix:**
   - Splits the input string into rows using `IFS`.
   - For each row:
     - Removes the leading `[` and trailing `]`.
     - Splits the row into its elements.
     - Stores the elements into an associative array `matrix` with keys as 
     `row,column`.

3. **Determining the Matrix Dimensions:**
   - Counts the number of rows (`nrows`).
   - Determines the maximum number of columns (`ncols`) across all rows.

4. **Transposing the Matrix:**
   - Iterates over each column index.
   - For each column, collects the elements from each row at that column index.
   - Builds the transposed row string and adds it to `transposed_rows`.

5. **Generating the Output:**
   - Joins the transposed rows using commas to form the final output string.
   - Prints the output.

**Notes:**

- The script supports matrices where rows have different numbers of columns.
- Missing elements in the matrix (due to irregular column sizes) are handled 
by inserting empty strings in the transposed matrix.
- The `join_by` function is used to handle joining array elements with a 
specified delimiter, ensuring proper formatting.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\openai_o3_mini_example.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import SearchToolkit
from camel.types import ModelPlatformType, ModelType

o3_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.O3_MINI,
    model_config_dict=ChatGPTConfig().as_dict(),
)


# Set agent
camel_agent = ChatAgent(
    model=o3_model, tools=[SearchToolkit().search_duckduckgo]
)

# Set user message
user_msg = """Search what is deepseek r1, and do a comparison between deepseek 
r1 and openai o3 mini and let me know the advantages and disadvantages of 
openai o3 mini"""

# Get response information
response = camel_agent.step(user_msg)
print(str(response.info['tool_calls'])[:1000])
'''
===============================================================================
[ToolCallingRecord(func_name='search_duckduckgo', args={'query': 'what is 
deepseek r1, and do a comparison between deepseek r1 and openai o3 mini', 
'source': 'text', 'max_results': 5}, result=[{'result_id': 1, 'title': 
'DeepSeek R1 vs OpenAI o1: Which One is Better? - Analytics Vidhya', 
'description': "The DeepSeek R1 has arrived, and it's not just another AI 
model—it's a significant leap in AI capabilities, trained upon the previously 
released DeepSeek-V3-Base variant.With the full-fledged release of DeepSeek 
R1, it now stands on par with OpenAI o1 in both performance and flexibility. 
What makes it even more compelling is its open weight and MIT licensing, 
making it commercially ...", 'url': 'https://www.analyticsvidhya.com/blog/2025/
01/deepseek-r1-vs-openai-o1/'}, {'result_id': 2, 'title': 'DeepSeek-R1: 
Features, Use Cases, and Comparison with OpenAI', 'description': 'Where 
DeepSeek Shines: Mathematical reasoning and code generation, thanks to 
RL-driven CoT.; Where OpenAI Has an...
===============================================================================
'''
print(response.msgs[0].content)
# ruff: noqa: RUF001, E501
'''
===============================================================================
Below is an overview of DeepSeek R1, followed by a comparative analysis with OpenAI’s o3-mini model.

• What is DeepSeek R1?  
DeepSeek R1 is an AI model that represents a significant leap in reasoning and language capabilities. It stems from prior iterations like DeepSeek-V3-Base but incorporates additional supervised fine-tuning, enabling improvements in mathematical reasoning, logic, and code generation. One of its major selling points is its open nature—released with an open license (MIT) and open weights—making it highly attractive for research, customization, and commercial applications without the traditional licensing barriers. It has been praised for its affordability (with API usage that can be many times cheaper than some competing models) and has been shown on several benchmarks to hold its own against established models.

• What is OpenAI’s o3-mini?  
OpenAI’s o3-mini is part of OpenAI’s reasoning model series and is designed to deliver robust performance specifically in STEM areas such as science, mathematics, and coding. Announced as a response to emerging competition (including DeepSeek R1), o3-mini emphasizes cost efficiency while providing competitive reasoning capabilities. It’s integrated into the ChatGPT ecosystem (with availability on ChatGPT’s enterprise and education platforms) and positions itself as a compact yet powerful option that delivers high-quality reasoning at a lower cost than some earlier OpenAI versions.

• Comparing DeepSeek R1 and OpenAI o3-mini:

1. Performance & Capabilities  
  – Both models are geared toward advanced reasoning tasks, including problem-solving in STEM subjects and code generation.  
  – DeepSeek R1 has been lauded for its performance enhancements over previous iterations (especially in areas like mathematical reasoning) thanks to intensive fine-tuning, while independent evaluations have pitted it against other high-end models.  
  – OpenAI o3-mini is tuned to deliver high-quality reasoning with a focus on speed and cost-effectiveness, often showing particularly strong results in STEM benchmarks.

2. Accessibility and Licensing  
  – DeepSeek R1 is open source with an MIT license. Its openly available weights make it especially attractive for academic research, startups, or any developer who prefers customizable and transparent AI tools without prohibitive licensing fees.  
  – In contrast, OpenAI o3-mini is available via OpenAI’s platforms (such as ChatGPT and its API). Users generally access it through a subscription or pay-as-you-go model, with pricing structured to remain competitive against both previous OpenAI models and the emerging open-source alternatives.

3. Cost Efficiency  
  – DeepSeek R1’s open-source nature generally translates into lower entry costs, making it an economical choice for developers and companies that want to deploy advanced reasoning tools without high API fees.  
  – OpenAI o3-mini, although designed to be more cost-efficient compared to earlier OpenAI releases, is still part of a managed service infrastructure. According to industry reports, it is significantly cheaper (with some mentions of being up to 63% less expensive than some predecessors) and positioned as a competitive alternative in pricing, but it may still come with usage limits tied to subscription tiers.

4. Ecosystem Integration  
  – With DeepSeek R1, users have the freedom to run the model in customized environments or integrate it within open-source projects—this flexibility can drive innovation in experimental research or bespoke applications.  
  – OpenAI o3-mini benefits from OpenAI’s established ecosystem and integration into widely used platforms like ChatGPT Enterprise and Education. Its seamless integration means users can quickly leverage its capabilities without dealing with additional infrastructure setups.

In summary, while both DeepSeek R1 and OpenAI o3-mini aim to push forward the frontier of reasoning and STEM-focused AI models, they serve slightly different audiences. DeepSeek R1’s open-weight, open-license approach makes it ideal for those prioritizing versatility and low-cost research or customized product development. On the other hand, OpenAI o3-mini leverages OpenAI’s ecosystem to offer a highly optimized, cost-effective model that is integrated directly into widely used interfaces and platforms, providing a more out-of-the-box solution for end users and enterprise clients.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\openai_structured_output_example.py
--------------------------------------------------------------------------------

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
from pydantic import BaseModel

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import FunctionTool, MathToolkit, SearchToolkit
from camel.types import ModelPlatformType, ModelType


class Student(BaseModel):
    name: str
    age: str


class StudentList(BaseModel):
    studentList: list[Student]


openai_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(temperature=0.0).as_dict(),
)

# Set agent
camel_agent = ChatAgent(
    model=openai_model,
    tools=[
        *MathToolkit().get_tools(),
        FunctionTool(SearchToolkit().search_duckduckgo),
    ],
)

# Set user message
user_msg = """give me some student infos, use 2024 minus 1996 as their age
"""

user_msg_2 = """give me some student infos, use 2024 minus 1996 as their age, 
search internet to get the most famous peoples in 2024 as their name"""

# Get response information
response = camel_agent.step(user_msg, response_format=StudentList)
print(response.msgs[0].content)
print(response.msgs[0].parsed)
'''
===============================================================================
{"studentLlst":[{"name":"Alice Johnson","age":"20"},{"name":"Brian Smith",
"age":"22"},{"name":"Catherine Lee","age":"19"},{"name":"David Brown",
"age":"21"},{"name":"Eva White","age":"20"}]}

studentList=[Student(name='Alice Johnson', age='20'), Student(name=
'Brian Smith', age='22'), Student(name='Catherine Lee', age='19'),
Student(name='David Brown', age='21'), Student(name='Eva White', age='23')]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\openrouter_llama3.1_example .py
--------------------------------------------------------------------------------

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

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENROUTER,
    model_type=ModelType.OPENROUTER_LLAMA_3_1_70B,
    model_config_dict=OpenRouterConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hello to the CAMEL AI community. It's great to see a group of like-minded 
individuals coming together to explore and advance the field of autonomous and 
communicative agents. Your open-source approach is truly commendable, as it 
fosters collaboration, innovation, and transparency. I'm excited to learn more 
about your projects and initiatives, and I'm happy to help in any way I can. 
Keep pushing the boundaries of AI research and development!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\openrouter_llama4_example.py
--------------------------------------------------------------------------------

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

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENROUTER,
    model_type=ModelType.OPENROUTER_LLAMA_4_MAVERICK_FREE,
    model_config_dict=OpenRouterConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hello CAMEL AI! I'm excited to connect with an open-source community that's 
pushing the boundaries of autonomous and communicative agents. Your work in 
this area has the potential to drive significant advancements in AI research 
and applications. What exciting projects or initiatives is the 
CAMEL AI community currently working on?
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\qwen_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import QwenConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.QWEN,
    model_type=ModelType.QWEN_2_5_CODER_32B,
    model_config_dict=QwenConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """give me python code to develop a trading bot"""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Creating a trading bot involves several steps, including data acquisition, 
strategy development, backtesting, and live trading. Below is a simplified 
example of a trading bot using Python. This example will use the `ccxt` 
library to interact with cryptocurrency exchanges and `pandas` for data 
manipulation. The strategy used here is a simple moving average crossover 
strategy.

First, you need to install the required libraries:

```bash
pip install ccxt pandas
```

Here's a basic example of a trading bot:

```python
import ccxt
import pandas as pd
import time

# Initialize the exchange
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# Define the trading parameters
symbol = 'BTC/USDT'
timeframe = '1h'
short_window = 50
long_window = 200
amount_to_trade = 0.001  # Amount of BTC to trade

def fetch_ohlcv(symbol, timeframe):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 
    'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_moving_averages(df, short_window, long_window):
    df['short_mavg'] = df['close'].rolling(window=short_window, min_periods=1).
    mean()
    df['long_mavg'] = df['close'].rolling(window=long_window, min_periods=1).
    mean()
    return df

def get_signal(df):
    if df['short_mavg'].iloc[-1] > df['long_mavg'].iloc[-1] and df
    ['short_mavg'].iloc[-2] <= df['long_mavg'].iloc[-2]:
        return 'buy'
    elif df['short_mavg'].iloc[-1] < df['long_mavg'].iloc[-1] and df
    ['short_mavg'].iloc[-2] >= df['long_mavg'].iloc[-2]:
        return 'sell'
    else:
        return 'hold'

def execute_trade(signal, symbol, amount):
    if signal == 'buy':
        order = exchange.create_market_buy_order(symbol, amount)
        print(f"Executed BUY order: {order}")
    elif signal == 'sell':
        order = exchange.create_market_sell_order(symbol, amount)
        print(f"Executed SELL order: {order}")

def main():
    while True:
        try:
            # Fetch OHLCV data
            df = fetch_ohlcv(symbol, timeframe)

            # Calculate moving averages
            df = calculate_moving_averages(df, short_window, long_window)

            # Get trading signal
            signal = get_signal(df)

            # Execute trade based on signal
            execute_trade(signal, symbol, amount_to_trade)

            # Wait for the next candle
            time.sleep(60 * 60)  # Sleep for 1 hour

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Sleep for 1 minute before retrying

if __name__ == "__main__":
    main()
```
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\qwq_model_example.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

ollama_model = ModelFactory.create(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="qwq",
    model_config_dict={"temperature": 0.4},
)

assistant_sys_msg = """You are a helpful and harmless assistant. You are Qwen 
developed by Alibaba. You should think step-by-step."""

agent = ChatAgent(assistant_sys_msg, model=ollama_model, token_limit=4096)

user_msg = """How many r in strawberry."""

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
Let's see. The word is "strawberry." I need to find out how many 'r's are in 
it. Okay, first, I'll spell it out slowly: s-t-r-a-w-b-e-r-r-y. Okay, now, 
I'll count the 'r's. Let's see: there's an 'r' after the 't', then another 'r' 
between the two 'r's towards the end, and one more at the end. Wait, no. Let's 
look again.

Spell it again: s-t-r-a-w-b-e-r-r-y.

Now, let's identify the positions of 'r':

1. The third letter is 'r'.

2. The eighth letter is 'r'.

3. The ninth letter is 'r'.

So, there are three 'r's in "strawberry."

But wait, let me double-check. Sometimes I might miscount. Let's list them out:

1. The first 'r' is the third letter.

2. The second 'r' is the eighth letter.

3. The third 'r' is the ninth letter.

Yes, that seems correct. So, the answer is three.

Alternatively, I can think about the pronunciation or the way the word is 
structured, but I think just spelling it out and counting is the most 
straightforward way.

Another way could be to break it down into syllables: straw-ber-ry. In "straw,
" there's one 'r'. In "ber," there's another 'r'. And in "ry," there's another 
'r'. So, again, three 'r's.

Wait, but in "ry," is there really an 'r'? Yes, "ry" has an 'r' and a 'y'. So, 
that accounts for the third 'r'.

So, whether I spell it out letter by letter or break it into syllables, I end 
up with three 'r's.

I think that's pretty conclusive.

**Final Answer**

\[ \boxed{3} \]
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\reka_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import RekaConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.REKA,
    model_type=ModelType.REKA_FLASH,
    model_config_dict=RekaConfig(temperature=0.0).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
 Hello CAMEL AI community! 🐫 I'm thrilled to connect with a group so 
 dedicated to the study of autonomous and communicative agents. Your work is 
 at the forefront of advancing AI technologies that can interact and operate 
 independently in complex environments. I look forward to learning from your 
 insights and contributing to the community in any way I can. Together, let's 
 continue to push the boundaries of what's possible in AI research and 
 development! 🚀
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\reward\nemotron_model_example.py
--------------------------------------------------------------------------------

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
from camel.models.reward import Evaluator, NemotronRewardModel
from camel.types import ModelType

reward_model = NemotronRewardModel(
    model_type=ModelType.NVIDIA_NEMOTRON_340B_REWARD,
    url="https://integrate.api.nvidia.com/v1",
)

evaluator = Evaluator(reward_model=reward_model)

messages = [
    {"role": "user", "content": "I am going to Paris, what should I see?"},
    {
        "role": "assistant",
        "content": "Ah, Paris, the City of Light! There are so many amazing "
        "things to see and do in this beautiful city ...",
    },
]

scores = evaluator.evaluate(messages)
print("Scores: ", scores)
'''
===============================================================================
Scores:  {'helpfulness': 1.6171875, 'correctness': 1.6484375, 'coherence': 3.
3125, 'complexity': 0.546875, 'verbosity': 0.515625}
===============================================================================
'''

scores_types = reward_model.get_scores_types()
print("Types: ", scores_types)
'''
===============================================================================
Types:  ['helpfulness', 'correctness', 'coherence', 'complexity', 'verbosity']
===============================================================================
'''

thresholds = {"helpfulness": 1.5, "correctness": 1.5}
is_acceptable = evaluator.filter_data(messages, thresholds)
print("Is acceptable: ", is_acceptable)
'''
===============================================================================
Is acceptable:  True
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\reward\skywork_model.py
--------------------------------------------------------------------------------

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
from camel.models.reward import Evaluator, SkyworkRewardModel

reward_model = SkyworkRewardModel(
    model_type="Skywork/Skywork-Reward-Llama-3.1-8B-v0.2",
)

evaluator = Evaluator(reward_model=reward_model)

messages = [
    {
        "role": "user",
        "content": "Jane has 12 apples. She gives 4 apples to her friend Mark,"
        " then buys 1 more apple, and finally splits all her apples "
        "equally among herself and her 2 siblings. How many apples does each "
        "person get?",
    },
    {
        "role": "assistant",
        "content": "1. Jane starts with 12 apples and gives 4 to Mark. 12 - 4 "
        "= 8. Jane now has 8 apples.\n2. Jane buys 1 more apple. 8 + 1 = 9. "
        "Jane now has 9 apples.\n3. Jane splits the 9 apples equally among "
        "herself and her 2 siblings (3 people in total). 9 ÷ 3 = 3 apples "
        "each. Each person gets 3 apples.",
    },
]

scores = evaluator.evaluate(messages)
print("Scores: ", scores)
'''
===============================================================================
Scores:  {'Score': 13.6875}
===============================================================================
'''

scores_types = reward_model.get_scores_types()
print("Types: ", scores_types)
'''
===============================================================================
Types:  ['Score']
===============================================================================
'''

thresholds = {"Score": 0}
is_acceptable = evaluator.filter_data(messages, thresholds)
print("Is acceptable: ", is_acceptable)
'''
===============================================================================
Is acceptable:  True
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\role_playing_with_claude.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main(model_type=None) -> None:
    task_prompt = "Develop a trading bot for the stock market"

    model = ModelFactory.create(
        model_platform=ModelPlatformType.ANTHROPIC,
        model_type=model_type,
    )

    # Update agent_kwargs to use the created models
    agent_kwargs = {
        "assistant": {"model": model},
        "user": {"model": model},
        "task-specify": {"model": model},
    }

    role_play_session = RolePlaying(
        assistant_role_name="Python Programmer",
        assistant_agent_kwargs=agent_kwargs["assistant"],
        user_role_name="Stock Trader",
        user_agent_kwargs=agent_kwargs["user"],
        task_prompt=task_prompt,
        with_task_specify=True,
        task_specify_agent_kwargs=agent_kwargs["task-specify"],
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main(model_type=ModelType.CLAUDE_3_5_SONNET)



--------------------------------------------------------------------------------
# File: models\role_playing_with_cohere.py
--------------------------------------------------------------------------------

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
from typing import List

from colorama import Fore

from camel.agents.chat_agent import ToolCallingRecord
from camel.configs import CohereConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.toolkits import (
    FunctionTool,
    MathToolkit,
    SearchToolkit,
)
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main(
    model_platform=ModelPlatformType.COHERE,
    model_type=ModelType.COHERE_COMMAND_R_PLUS,
    chat_turn_limit=3,
) -> None:
    task_prompt = (
        "Assume now is 2024 in the Gregorian calendar, "
        "estimate the current age of University of Oxford "
        "and then add 10 more years to this age."
    )

    user_model_config = CohereConfig(temperature=0.2)

    tools_list = [
        *MathToolkit().get_tools(),
        FunctionTool(SearchToolkit().search_duckduckgo),
    ]
    assistant_model_config = CohereConfig(
        temperature=0.2,
    )

    role_play_session = RolePlaying(
        assistant_role_name="Searcher",
        user_role_name="Professor",
        assistant_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                model_config_dict=assistant_model_config.as_dict(),
            ),
            tools=tools_list,
        ),
        user_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                model_config_dict=user_model_config.as_dict(),
            ),
        ),
        task_prompt=task_prompt,
        with_task_specify=False,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        # Print output from the user
        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )

        # Print output from the assistant, including any function
        # execution information
        print_text_animated(Fore.GREEN + "AI Assistant:")
        tool_calls: List[ToolCallingRecord] = [
            ToolCallingRecord(**call.as_dict())
            for call in assistant_response.info['tool_calls']
        ]
        for func_record in tool_calls:
            print_text_animated(f"{func_record}")
        print_text_animated(f"{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: models\role_playing_with_gemini.py
--------------------------------------------------------------------------------

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

from colorama import Fore

from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main(model_type=None) -> None:
    task_prompt = "Develop a trading bot for the stock market"

    model = ModelFactory.create(
        model_platform=ModelPlatformType.GEMINI,
        model_type=model_type,
    )

    # Update agent_kwargs to use the created models
    agent_kwargs = {
        "assistant": {"model": model},
        "user": {"model": model},
        "task-specify": {"model": model},
    }

    role_play_session = RolePlaying(
        assistant_role_name="Python Programmer",
        assistant_agent_kwargs=agent_kwargs["assistant"],
        user_role_name="Stock Trader",
        user_agent_kwargs=agent_kwargs["user"],
        task_prompt=task_prompt,
        with_task_specify=True,
        task_specify_agent_kwargs=agent_kwargs["task-specify"],
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main(model_type=ModelType.GEMINI_1_5_FLASH)



--------------------------------------------------------------------------------
# File: models\role_playing_with_groq.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main(model_type=None) -> None:
    task_prompt = "Develop a trading bot for the stock market"

    agent_kwargs = {
        role: ModelFactory.create(
            model_platform=ModelPlatformType.GROQ,
            model_type=model_type,
        )
        for role in ["assistant", "user", "task-specify"]
    }

    role_play_session = RolePlaying(
        assistant_role_name="Python Programmer",
        assistant_agent_kwargs={'model': agent_kwargs["assistant"]},
        user_role_name="Stock Trader",
        user_agent_kwargs={'model': agent_kwargs["assistant"]},
        task_prompt=task_prompt,
        with_task_specify=True,
        task_specify_agent_kwargs={'model': agent_kwargs["task-specify"]},
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n",
            delay=0.005,
        )
        print_text_animated(
            Fore.GREEN + "AI Assistant:\n\n"
            f"{assistant_response.msg.content}\n",
            delay=0.005,
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main(model_type=ModelType.GROQ_LLAMA_3_1_8B)



--------------------------------------------------------------------------------
# File: models\role_playing_with_mistral.py
--------------------------------------------------------------------------------

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

from typing import List

from colorama import Fore

from camel.agents.chat_agent import ToolCallingRecord
from camel.configs import MistralConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.toolkits import (
    MathToolkit,
    SearchToolkit,
)
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main(
    model_platform=ModelPlatformType.MISTRAL,
    model_type=ModelType.MISTRAL_LARGE,
    chat_turn_limit=10,
) -> None:
    task_prompt = (
        "Assume now is 2024 in the Gregorian calendar, "
        "estimate the current age of University of Oxford "
        "and then add 10 more years to this age."
    )

    user_model_config = MistralConfig(temperature=0.2)

    tools_list = [
        *MathToolkit().get_tools(),
        *SearchToolkit().get_tools(),
    ]
    assistant_model_config = MistralConfig(
        temperature=0.2,
    )

    role_play_session = RolePlaying(
        assistant_role_name="Searcher",
        user_role_name="Professor",
        assistant_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                model_config_dict=assistant_model_config.as_dict(),
            ),
            tools=tools_list,
        ),
        user_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                model_config_dict=user_model_config.as_dict(),
            ),
        ),
        task_prompt=task_prompt,
        with_task_specify=False,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        # Print output from the user
        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )

        # Print output from the assistant, including any function
        # execution information
        print_text_animated(Fore.GREEN + "AI Assistant:")
        tool_calls: List[ToolCallingRecord] = [
            ToolCallingRecord(**call.as_dict())
            for call in assistant_response.info['tool_calls']
        ]
        for func_record in tool_calls:
            print_text_animated(f"{func_record}")
        print_text_animated(f"{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: models\role_playing_with_ollama.py
--------------------------------------------------------------------------------

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

from typing import List

from colorama import Fore

from camel.agents.chat_agent import ToolCallingRecord
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType
from camel.utils import print_text_animated


def main(
    model_platform=ModelPlatformType.OLLAMA,
    model_type="llama3.2",
    chat_turn_limit=10,
) -> None:
    task_prompt = "Develop a trading bot for the stock market."

    role_play_session = RolePlaying(
        assistant_role_name="Python Programmer",
        user_role_name="Stock Trader",
        assistant_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                model_config_dict={"temperature": 0.4, "max_tokens": 4096},
            ),
        ),
        user_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                model_config_dict={"temperature": 0.4, "max_tokens": 4096},
            ),
        ),
        task_prompt=task_prompt,
        with_task_specify=False,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        # Print output from the user
        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )

        # Print output from the assistant, including any function
        # execution information
        print_text_animated(Fore.GREEN + "AI Assistant:")
        tool_calls: List[ToolCallingRecord] = [
            ToolCallingRecord(**call.as_dict())
            for call in assistant_response.info['tool_calls']
        ]
        for func_record in tool_calls:
            print_text_animated(f"{func_record}")
        print_text_animated(f"{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: models\role_playing_with_sambanova.py
--------------------------------------------------------------------------------

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

from typing import List

import agentops
from colorama import Fore

from camel.agents.chat_agent import ToolCallingRecord
from camel.configs import SambaCloudAPIConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType
from camel.utils import print_text_animated

# Initialize agentops
agentops.init(default_tags=["SambaNova_with_Agentops"])
from camel.toolkits import (  # noqa: E402
    MathToolkit,
    SearchToolkit,
)


def main(
    model_platform=ModelPlatformType.SAMBA,
    model_type="Meta-Llama-3.1-70B-Instruct",
    chat_turn_limit=10,
) -> None:
    task_prompt = (
        "Assume now is 2024 in the Gregorian calendar, "
        "estimate the current age of University of Oxford "
        "and then add 10 more years to this age."
    )

    user_model_config = SambaCloudAPIConfig(temperature=0.0, max_tokens=1800)

    tools_list = [
        *MathToolkit().get_tools(),
        *SearchToolkit().get_tools(),
    ]
    assistant_model_config = SambaCloudAPIConfig(
        temperature=0.0, max_tokens=2200
    )

    role_play_session = RolePlaying(
        assistant_role_name="Searcher",
        user_role_name="Professor",
        assistant_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                url="https://api.sambanova.ai/v1",
                model_config_dict=assistant_model_config.as_dict(),
            ),
            tools=tools_list,
        ),
        user_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
                url="https://api.sambanova.ai/v1",
                model_config_dict=user_model_config.as_dict(),
            ),
        ),
        task_prompt=task_prompt,
        with_task_specify=False,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        # Print output from the user
        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )

        # Print output from the assistant, including any function
        # execution information
        print_text_animated(Fore.GREEN + "AI Assistant:")
        tool_calls: List[ToolCallingRecord] = [
            ToolCallingRecord(**call.as_dict())
            for call in assistant_response.info['tool_calls']
        ]
        for func_record in tool_calls:
            print_text_animated(f"{func_record}")
        print_text_animated(f"{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg

    # End agentops session
    agentops.end_session("Success")


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: models\role_playing_with_volcano.py
--------------------------------------------------------------------------------

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

from typing import Dict, List, Optional, Tuple

from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType
from camel.utils import print_text_animated

"""
Please set the below environment variable before running this example:
export VOLCANO_API_KEY="your_volcano_api_key"

This example demonstrates how to use Volcano Engine API with DeepSeek models
for role-playing in CAMEL.
"""


def main(
    assistant_role_name: str = "Python Programmer",
    user_role_name: str = "Stock Market Trader",
    task_prompt: str = (
        "Develop a Python script that analyzes historical stock data "
        "and identifies potential buying opportunities based on "
        "technical indicators."
    ),
    with_task_specify: bool = True,
    model_config_dict: Optional[Dict] = None,
) -> Tuple[List[Dict], List[Dict]]:
    r"""Run a role-playing session with Volcano Engine API.

    Args:
        assistant_role_name: The role name of the assistant.
        user_role_name: The role name of the user.
        task_prompt: The task prompt.
        with_task_specify: Whether to specify the task.
        model_config_dict: The model configuration dictionary.

    Returns:
        A tuple of assistant and user message lists.
    """
    if model_config_dict is None:
        model_config_dict = {
            "temperature": 0.2,
            "max_tokens": 1024,
        }

    # Create models for assistant and user
    assistant_model = ModelFactory.create(
        model_platform=ModelPlatformType.VOLCANO,
        model_type="deepseek-r1-250120",
        model_config_dict=model_config_dict,
    )

    user_model = ModelFactory.create(
        model_platform=ModelPlatformType.VOLCANO,
        model_type="deepseek-r1-250120",
        model_config_dict=model_config_dict,
    )

    # Create a role-playing session
    role_playing = RolePlaying(
        assistant_role_name=assistant_role_name,
        user_role_name=user_role_name,
        assistant_agent_kwargs={"model": assistant_model},
        user_agent_kwargs={"model": user_model},
        task_prompt=task_prompt,
        with_task_specify=with_task_specify,
    )

    # Start the role-playing session
    print(
        f"Running role-playing with Volcano Engine API (DeepSeek-R1)...\n"
        f"Assistant Role: {assistant_role_name}\n"
        f"User Role: {user_role_name}\n"
        f"Task: {task_prompt}\n"
    )

    # Start the chat
    chat_history = []
    n = 0
    input_msg = role_playing.init_chat()  # Initialize the chat
    while n < 10:
        n += 1
        assistant_response, user_response = role_playing.step(
            input_msg
        )  # Provide input_msg
        if assistant_response is None or user_response is None:
            break

        chat_history.append(
            {
                "role": "assistant",
                "content": assistant_response.msg.content,
            }
        )
        chat_history.append(
            {"role": "user", "content": user_response.msg.content}
        )

        print_text_animated(f"Assistant ({assistant_role_name}):\n")
        print_text_animated(f"{assistant_response.msg.content}\n")
        print_text_animated(f"User ({user_role_name}):\n")
        print_text_animated(f"{user_response.msg.content}\n")

        if "<CAMEL_TASK_DONE>" in user_response.msg.content:
            break

        input_msg = (
            assistant_response.msg
        )  # Update input_msg for the next step

    # return role_playing.assistant_agent.chat_history, role_playing.
    # user_agent.chat_history


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: models\samba_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import (
    SambaCloudAPIConfig,
    SambaVerseAPIConfig,
)
from camel.models import ModelFactory
from camel.types import ModelPlatformType

# Define system message
sys_msg = "You are a helpful assistant."

# Define user message
user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""


# Use Samba Cloud model
samba_cloud_api_model = ModelFactory.create(
    model_platform=ModelPlatformType.SAMBA,
    model_type="Meta-Llama-3.1-405B-Instruct",
    model_config_dict=SambaCloudAPIConfig(max_tokens=800).as_dict(),
    api_key="Your SambaNova Cloud API Key",
    url="https://api.sambanova.ai/v1",
)

# Set agent
camel_agent_samba_cloud_api = ChatAgent(
    system_message=sys_msg, model=samba_cloud_api_model
)

# Get response information
response = camel_agent_samba_cloud_api.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello to the CAMEL AI community.  It's great to see open-source communities 
like yours working on autonomous and communicative agents, as this field has 
the potential to revolutionize many areas of our lives, from customer service 
to healthcare and beyond.

What specific projects or initiatives is the CAMEL AI community currently 
working on? Are there any exciting developments or breakthroughs that you'd 
like to share? I'm all ears (or rather, all text) and happy to learn more 
about your work!
===============================================================================
'''

# Use Samba Verse model
sambaverse_api_model = ModelFactory.create(
    model_platform=ModelPlatformType.SAMBA,
    model_type="Mistral/Mistral-7B-Instruct-v0.2",
    model_config_dict=SambaVerseAPIConfig(max_tokens=800).as_dict(),
    api_key="Your SambaVerse API Key",
    url="https://sambaverse.sambanova.ai/api/predict",
)

# Set agent
camel_agent_sambaverse_api = ChatAgent(
    system_message=sys_msg, model=sambaverse_api_model
)

# Get response information
response = camel_agent_sambaverse_api.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hi CAMEL AI community! I'm here to help answer any questions you may have
related to autonomous and communicative agents. Let me know how I can be 
of assistance.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\sglang_model_example.py
--------------------------------------------------------------------------------

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


from dotenv import load_dotenv

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

r"""Before using sglang to run LLM model offline,
you need to install flashinfer.
Consider your machine's configuration and 
install flashinfer in a appropriate version.
For more details, please refer to:
https://sgl-project.github.io/start/install.html
https://docs.flashinfer.ai/installation.html

Please load HF_token in your environment variable.
export HF_TOKEN=""
When using the OpenAI interface to run SGLang model server, 
the base model may fail to recognize  huggingface default
chat template, switching to the Instruct model resolves the issue.
"""
load_dotenv()
sglang_model = ModelFactory.create(
    model_platform=ModelPlatformType.SGLANG,
    model_type="meta-llama/Llama-3.2-1B-Instruct",
    model_config_dict={"temperature": 0.0},
    api_key="sglang",
)
assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=sglang_model, token_limit=4096)

user_msg = "Say hi to CAMEL AI"

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
Hello CAMEL AI. How can I assist you today?
===============================================================================
"""

weather_tool = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to find the weather for,\n"
                        "e.g. 'San Francisco'",
                    },
                    "state": {
                        "type": "string",
                        "description": "The two-letter abbreviation for,\n"
                        "the state (e.g., 'CA'), e.g. CA for California",
                    },
                    "unit": {
                        "type": "string",
                        "description": "Temperature unit (celsius/fahrenheit)",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["city", "state", "unit"],
            },
        },
    }
]


r"""Note that api_key defines the parser used to interpret responses.
Currently supported parsers include:
llama3: Llama 3.1 / 3.2 (e.g. meta-llama/Llama-3.1-8B-Instruct,
        meta-llama/Llama-3.2-1B-Instruct).
mistral: Mistral (e.g. mistralai/Mistral-7B-Instruct-v0.3,
         mistralai/Mistral-Nemo-Instruct-2407, 
         mistralai/ Mistral-Nemo-Instruct-2407, mistralai/Mistral-7B-v0.3).
qwen25: Qwen 2.5 (e.g. Qwen/Qwen2.5-1.5B-Instruct, Qwen/Qwen2.5-7B-Instruct).
"""
sglang_model_with_tool = ModelFactory.create(
    model_platform=ModelPlatformType.SGLANG,
    model_type="meta-llama/Llama-3.2-1B-Instruct",
    model_config_dict={"temperature": 0.0, "tools": weather_tool},
    api_key="llama3",
)

assistant_sys_msg = (
    "You are a helpful assistant.\n"
    "Use the get_current_weather tool when asked about weather."
)
agent_with_tool = ChatAgent(
    assistant_sys_msg,
    model=sglang_model_with_tool,
    token_limit=4096,
    external_tools=weather_tool,
)
user_msg = "What's the weather in Boston today?"

assistant_response = agent_with_tool.step(user_msg)
external_tool_call = assistant_response.info.get('external_tool_call_request')
if external_tool_call:
    print(f"Detected external tool call: {external_tool_call.tool_name}")
    print(f"Arguments: {external_tool_call.args}")
    print(f"Tool Call ID: {external_tool_call.tool_call_id}")
else:
    print("No external tool call detected")

"""
===============================================================================
Detected external tool call: get_current_weather
Arguments: {'city': 'Boston', 'state': 'MA', 'unit': 'celsius'}
Tool Call ID: 0
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\siliconflow_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import SiliconFlowConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType

model = ModelFactory.create(
    model_platform=ModelPlatformType.SILICONFLOW,
    model_type="deepseek-ai/DeepSeek-R1",
    model_config_dict=SiliconFlowConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)

'''
===============================================================================
Hello CAMEL AI community! 👋 Your dedication to advancing the study of 
autonomous and communicative agents through open-source collaboration is truly 
inspiring. The work you're doing to push the boundaries of AI interaction and 
cooperative systems will undoubtedly shape the future of intelligent 
technologies. Keep innovating, exploring, and fostering that spirit of shared 
learning—the world is excited to see what you create next! 🚀
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\togetherai_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import TogetherAIConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType

model = ModelFactory.create(
    model_platform=ModelPlatformType.TOGETHER,
    model_type="meta-llama/Llama-3-8b-chat-hf",
    model_config_dict=TogetherAIConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model, token_limit=500)

user_msg = """Say hi to CAMEL AI, one open-source community dedicated to the 
    study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI community!

I'm thrilled to be here and assist you with any questions or topics related to 
autonomous and communicative agents. As an open-source community, I'm excited 
to see the innovative projects and research being developed by your members.

What's on your mind? Do you have a specific question, project, or topic you'd 
like to discuss? I'm here to help and provide any assistance I can. Let's get 
started!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\vllm_model_example.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

vllm_model = ModelFactory.create(
    model_platform=ModelPlatformType.VLLM,
    model_type="microsoft/Phi-3-mini-4k-instruct",
    model_config_dict={"temperature": 0.0},
)

assistant_sys_msg = "You are a helpful assistant."

agent = ChatAgent(assistant_sys_msg, model=vllm_model, token_limit=4096)

user_msg = "Say hi to CAMEL AI"

assistant_response = agent.step(user_msg)
print(assistant_response.msg.content)

"""
===============================================================================
vllm server started on http://localhost:8000/v1 for microsoft/
Phi-3-mini-4k-instruct model

Hello! I'm Phi, an AI developed by Microsoft. How can I help you today?
===============================================================================
"""



--------------------------------------------------------------------------------
# File: models\volcano_model_example.py
--------------------------------------------------------------------------------

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
from camel.models import ModelFactory
from camel.types import ModelPlatformType

"""
Please set the below environment variable before running this example:
export VOLCANO_API_KEY="your_volcano_api_key"

Volcano Engine API supports various models including DeepSeek models.
This example uses the DeepSeek-R1 model.
"""

# Create a model using ModelFactory
model = ModelFactory.create(
    model_platform=ModelPlatformType.VOLCANO,
    model_type="deepseek-r1-250120",  # DeepSeek-R1 model
    model_config_dict={
        "temperature": 0.2,
        "max_tokens": 1024,
    },
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """How many r in strawberry."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)



--------------------------------------------------------------------------------
# File: models\yi_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import YiConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.YI,
    model_type=ModelType.YI_LIGHTNING,
    model_config_dict=YiConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello CAMEL AI community! 👋 It's great to connect with an open-source group 
dedicated to the fascinating fields of autonomous and communicative agents. If 
there's anything you need assistance with or any interesting projects you're 
working on, feel free to share. I'm here to help however I can! 😊
===============================================================================
'''



--------------------------------------------------------------------------------
# File: models\zhipuai_model_example.py
--------------------------------------------------------------------------------

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
from camel.configs import ZhipuAIConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.ZHIPU,
    model_type=ModelType.GLM_4,
    model_config_dict=ZhipuAIConfig(temperature=0.2).as_dict(),
)

# Define system message
sys_msg = "You are a helpful assistant."

# Set agent
camel_agent = ChatAgent(system_message=sys_msg, model=model)

user_msg = """Say hi to CAMEL AI, one open-source community 
    dedicated to the study of autonomous and communicative agents."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
Hello to CAMEL AI and its community! As a helpful assistant, I'm here to 
provide assistance, answer questions, and support the study of autonomous and 
communicative agents to the best of my abilities. If you have any specific 
questions or need guidance on a particular topic, feel free to ask!
===============================================================================
'''



--------------------------------------------------------------------------------
# File: observability\agentops_track_roleplaying_with_function.py
--------------------------------------------------------------------------------

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

from typing import List

import agentops
from colorama import Fore

from camel.agents.chat_agent import ToolCallingRecord
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated

# Initialize agentops
agentops.init(tags=["CAMEL X AgentOps"])

# Import toolkits after init of agentops so that the tool usage would be
# tracked
from camel.toolkits import (  # noqa: E402
    MathToolkit,
    SearchToolkit,
)

# Set up role playing session
model_platform = ModelPlatformType.DEFAULT
model_type = ModelType.DEFAULT
chat_turn_limit = 10
task_prompt = (
    "Assume now is 2024 in the Gregorian calendar, "
    "estimate the current age of University of Oxford "
    "and then add 10 more years to this age, "
    "and get the current weather of the city where "
    "the University is located."
)

user_model_config = ChatGPTConfig(temperature=0.0)

tools_list = [
    *MathToolkit().get_tools(),
    *SearchToolkit().get_tools(),
]
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

role_play_session = RolePlaying(
    assistant_role_name="Searcher",
    user_role_name="Professor",
    assistant_agent_kwargs=dict(
        model=ModelFactory.create(
            model_platform=model_platform,
            model_type=model_type,
            model_config_dict=assistant_model_config.as_dict(),
        ),
        tools=tools_list,
    ),
    user_agent_kwargs=dict(
        model=ModelFactory.create(
            model_platform=model_platform,
            model_type=model_type,
            model_config_dict=user_model_config.as_dict(),
        ),
    ),
    task_prompt=task_prompt,
    with_task_specify=False,
)

print(
    Fore.GREEN
    + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
)
print(Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n")

print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
print(
    Fore.CYAN
    + "Specified task prompt:"
    + f"\n{role_play_session.specified_task_prompt}\n"
)
print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

n = 0
input_msg = role_play_session.init_chat()
while n < chat_turn_limit:
    n += 1
    assistant_response, user_response = role_play_session.step(input_msg)

    if assistant_response.terminated:
        print(
            Fore.GREEN
            + (
                "AI Assistant terminated. Reason: "
                f"{assistant_response.info['termination_reasons']}."
            )
        )
        break
    if user_response.terminated:
        print(
            Fore.GREEN
            + (
                "AI User terminated. "
                f"Reason: {user_response.info['termination_reasons']}."
            )
        )
        break

    # Print output from the user
    print_text_animated(
        Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
    )

    # Print output from the assistant, including any function
    # execution information
    print_text_animated(Fore.GREEN + "AI Assistant:")
    tool_calls: List[ToolCallingRecord] = [
        ToolCallingRecord(**call.as_dict())
        for call in assistant_response.info['tool_calls']
    ]
    for func_record in tool_calls:
        print_text_animated(f"{func_record}")
    print_text_animated(f"{assistant_response.msg.content}\n")

    if "CAMEL_TASK_DONE" in user_response.msg.content:
        break

    input_msg = assistant_response.msg

# End agentops session
agentops.end_session("Success")



--------------------------------------------------------------------------------
# File: personas\personas_generation.py
--------------------------------------------------------------------------------

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

from camel.personas.persona_hub import PersonaHub

persona_group = PersonaHub()

# Use the text_to_persona method
example_text = """Clinical Guideline: Administration of Injections in 
Pediatric Patients Purpose: To provide standardized care for pediatric 
patients requiring injections, ensuring safety, ..."""

inferred_persona = persona_group.text_to_persona(example_text, action="read")
print(
    f"Inferred Persona:\n{inferred_persona.name}"
    f"\n{inferred_persona.description}\n"
)

# Use the persona_to_persona method
related_personas = persona_group.persona_to_persona(persona=inferred_persona)
print("Related Personas:\n")
for persona_id, persona in related_personas.items():
    print(f"ID: {persona_id}")
    print(f"Name: {persona.name}")
    print(f"Description: {persona.description}")
    print()
'''
===============================================================================
Inferred Persona:
Pediatric Nurse
A healthcare professional specializing in the care of children, with expertise in administering medications and following clinical guidelines for pediatric patients.

Related Personas:

ID: 123e4567-e89b-12d3-a456-426614174000
Name: Pediatrician
Description: A medical doctor who specializes in the care of infants, children, and adolescents. They work closely with pediatric nurses to ensure proper treatment and medication administration for young patients.

ID: 123e4567-e89b-12d3-a456-426614174001
Name: Child Life Specialist
Description: A professional who helps children and families cope with the challenges of hospitalization, illness, and disability. They often collaborate with medical staff to make medical procedures less stressful for pediatric patients.

ID: 123e4567-e89b-12d3-a456-426614174002
Name: Pediatric Pharmacist
Description: A pharmacist who specializes in medications for children, ensuring proper dosing and formulations. They work with the medical team to optimize medication regimens for pediatric patients.

ID: 123e4567-e89b-12d3-a456-426614174003
Name: Parent or Guardian
Description: The primary caregiver of a pediatric patient, who needs to understand and consent to medical procedures, including injections. They often have concerns and questions about their child's treatment.

ID: 123e4567-e89b-12d3-a456-426614174004
Name: Pediatric Hospital Administrator
Description: A healthcare manager responsible for overseeing pediatric departments or hospitals. They ensure that clinical guidelines are implemented and followed to maintain high standards of care for young patients.
===============================================================================
'''  # noqa: E501



--------------------------------------------------------------------------------
# File: rag\single_agent_with_hybrid_rag.py
--------------------------------------------------------------------------------

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
from camel.retrievers import HybridRetriever


def single_agent(query: str) -> str:
    # Set agent role
    assistant_sys_msg = """You are a helpful assistant to answer question,
         I will give you the Original Query and Retrieved Context,
        answer the Original Query based on the Retrieved Context,
        if you can't answer the question just say I don't know."""

    hybrid_retriever = HybridRetriever()
    hybrid_retriever.process(
        content_input_path="https://en.wikipedia.org/wiki/King_Abdullah_University_of_Science_and_Technology"
    )

    retrieved_info = hybrid_retriever.query(
        query=query,
        top_k=5,
        vector_retriever_top_k=10,
        bm25_retriever_top_k=10,
    )

    # Pass the retrieved information to agent
    user_msg = str(retrieved_info)
    agent = ChatAgent(assistant_sys_msg)

    # Get response
    assistant_response = agent.step(user_msg)
    return assistant_response.msg.content


print(single_agent("What is it like to be a visiting student at KAUST?"))
'''
===============================================================================
Being a visiting student at KAUST involves participating in the Visiting
Student Program (VS), which is designed for 3rd or 4th year undergraduate
or master's students. This program allows students to work directly with KAUST
faculty members for a duration that can range from a few days to several
months. Accepted students typically receive a monthly stipend, and their
accommodation, health insurance, and travel costs are covered. This support
makes the experience financially manageable and allows students to focus on
their research and learning during their time at KAUST.
===============================================================================
'''



--------------------------------------------------------------------------------
# File: role_description\role_generation.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.agents import RoleAssignmentAgent


def main(model=None, num_roles=3) -> None:
    task_prompt = "Develop a trading bot for the stock market."

    role_description_agent = RoleAssignmentAgent(model=model)

    role_description_dict = role_description_agent.run(
        task_prompt=task_prompt, num_roles=num_roles
    )

    if len(role_description_dict) != num_roles:
        raise ValueError(
            f"Length of role_names ({len(role_description_dict)}) "
            f"does not equal to num_roles ({num_roles})."
        )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(Fore.GREEN + f"List of {num_roles} roles with description:")
    for role_name in role_description_dict.keys():
        print(
            Fore.BLUE + f"{role_name}:\n"
            f"{role_description_dict[role_name]}\n"
        )


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: role_description\role_playing_with_role_description.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.agents import RoleAssignmentAgent
from camel.societies import RolePlaying
from camel.types import TaskType
from camel.utils import print_text_animated

AI_ASSISTANT_ROLE_INDEX = 0
AI_USER_ROLE_INDEX = 1


def main(
    model_for_role_generation=None, model=None, chat_turn_limit=50
) -> None:
    task_prompt = "Develop a trading bot for the stock market."

    role_description_agent = RoleAssignmentAgent(
        model=model_for_role_generation,
    )

    role_description_dict = role_description_agent.run(
        task_prompt=task_prompt, num_roles=2
    )

    ai_assistant_role = list(role_description_dict.keys())[
        AI_ASSISTANT_ROLE_INDEX
    ]
    ai_user_role = list(role_description_dict.keys())[AI_USER_ROLE_INDEX]
    ai_assistant_description = role_description_dict[ai_assistant_role]
    ai_user_description = role_description_dict[ai_user_role]

    sys_msg_meta_dicts = [
        dict(
            assistant_role=ai_assistant_role,
            user_role=ai_user_role,
            assistant_description=ai_assistant_description,
            user_description=ai_user_description,
        )
        for _ in range(2)
    ]

    role_play_session = RolePlaying(
        assistant_role_name=ai_assistant_role,
        user_role_name=ai_user_role,
        task_prompt=task_prompt,
        model=model,
        task_type=TaskType.ROLE_DESCRIPTION,  # Score for role description
        with_task_specify=True,
        task_specify_agent_kwargs=dict(model=model),
        extend_sys_msg_meta_dicts=sys_msg_meta_dicts,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )
    print(
        Fore.GREEN + f"Role description of AI Assistant:\n"
        f"{role_play_session.assistant_sys_msg.role_name}\n"
        f"{role_description_dict[ai_assistant_role]}\n"
    )
    print(
        Fore.BLUE + f"Role description of AI User:\n"
        f"{role_play_session.user_sys_msg.role_name}\n"
        f"{role_description_dict[ai_user_role]}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. "
                    f"Reason: {assistant_response.info['termination_reasons']}"
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        print_text_animated(
            Fore.BLUE
            + f"AI User: {ai_user_role}\n\n{user_response.msg.content}\n"
        )
        print_text_animated(
            Fore.GREEN
            + f"AI Assistant:{ai_assistant_role}\n\n"
            + f"{assistant_response.msg.content}\n"
        )

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: runtime\code_execution_with_docker_runtime.py
--------------------------------------------------------------------------------

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

from colorama import Fore

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.runtime import DockerRuntime
from camel.toolkits.code_execution import CodeExecutionToolkit
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated

# tools
toolkit = CodeExecutionToolkit(verbose=True)

# change to your own docker image
runtime = DockerRuntime("xukunliu/camel").add(
    toolkit.get_tools(),
    "camel.toolkits.CodeExecutionToolkit",
    dict(verbose=True),
    redirect_stdout=True,
)

tools = runtime.get_tools()

# set up LLM model
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.GPT_4O,
    model_config_dict=assistant_model_config.as_dict(),
)


# set up agent

assistant_sys_msg = (
    "You are a personal math tutor and programmer. "
    "When asked a math question, "
    "write and run Python code to answer the question."
)

agent = ChatAgent(
    assistant_sys_msg,
    model,
    tools=tools,
)
agent.reset()


# set up agent

with runtime as r:
    r.wait()
    prompt = (
        "Weng earns $12 an hour for babysitting. "
        "Yesterday, she just did 51 minutes of babysitting. How much did she earn?"
    )
    print(Fore.YELLOW + f"user prompt:\n{prompt}\n")

    response = agent.step(prompt)
    for msg in response.msgs:
        print_text_animated(Fore.GREEN + f"Agent response:\n{msg.content}\n")


# ruff: noqa: E501
"""
===============================================================================
user prompt:
Weng earns $12 an hour for babysitting. Yesterday, she just did 51 minutes of babysitting. How much did she earn?

Executed the code below:
```py
hourly_rate = 12
minutes_worked = 51
hourly_earnings = hourly_rate / 60 * minutes_worked
hourly_earnings
```
> Executed Results:
10.200000000000001
Agent response:
Weng earned $10.20 for babysitting for 51 minutes at a rate of $12 per hour.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: runtime\code_execution_with_llm_guard_runtime.py
--------------------------------------------------------------------------------

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

from colorama import Fore

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.runtime import LLMGuardRuntime
from camel.toolkits.code_execution import CodeExecutionToolkit
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated

# tools
toolkit = CodeExecutionToolkit(verbose=False)


runtime = LLMGuardRuntime(verbose=True).add(
    *CodeExecutionToolkit().get_tools()
)

tools = runtime.get_tools()

print("Tools:")
for tool in tools:
    print(tool.get_function_name())

# set up LLM model
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=assistant_model_config.as_dict(),
)


# set up agent

assistant_sys_msg = (
    "You are a personal math tutor and programmer. "
    "When asked a math question, "
    "write and run Python code to answer the question."
)

agent = ChatAgent(
    assistant_sys_msg,
    model,
    tools=tools,
)
agent.reset()


# set up agent

prompt = (
    "Weng earns $12 an hour for babysitting. "
    "Yesterday, she just did 51 minutes of babysitting. How much did she earn?"
)
print(Fore.YELLOW + f"user prompt:\n{prompt}\n")

response = agent.step(prompt)
for msg in response.msgs:
    print_text_animated(Fore.GREEN + f"Agent response:\n{msg.content}\n")


# ruff: noqa: E501
"""
Tools:
ignore_risk
execute_code
user prompt:
Weng earns $12 an hour for babysitting. Yesterday, she just did 51 minutes of babysitting. How much did she earn?

Risk assessment not passed for function execute_code.Score: 3 > Threshold: 2
Reason: The function 'execute_code' is designed to execute arbitrary code snippets, which inherently poses a significant risk. Although the provided code snippet appears harmless and simply calculates earnings based on hourly wage and minutes worked, the function itself allows for potentially dangerous operations if different code were to be executed. Therefore, the risk level is assessed as 3.
Ignoring risk for function execute_code: The code is a simple arithmetic calculation that poses no risk.
Agent response:
Weng earned $10.20 for 51 minutes of babysitting.
"""



--------------------------------------------------------------------------------
# File: runtime\docker_runtime.py
--------------------------------------------------------------------------------

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
from camel.runtime import DockerRuntime
from camel.toolkits import CodeExecutionToolkit, MathToolkit

if __name__ == "__main__":
    runtime = (
        DockerRuntime("xukunliu/camel")  # change to your own docker image
        .add(MathToolkit().get_tools(), "camel.toolkits.MathToolkit")
        .add(
            CodeExecutionToolkit().get_tools(),
            "camel.toolkits.CodeExecutionToolkit",
            dict(verbose=True),
        )
    )

    with (
        runtime as r
    ):  # using with statement to automatically close the runtime
        print("Waiting for runtime to be ready...")
        r.wait()
        print("Runtime is ready.")

        tools = r.get_tools()

        add, sub, mul = tools[:3]
        code_exec = tools[3]

        # without kwargs
        print(f"Add 1 + 2: {add.func(1, 2)}")
        print(f"Subtract 5 - 3: {sub.func(5, 3)}")
        print(f"Multiply 2 * 3: {mul.func(2, 3)}")
        print(f"Execute code: {code_exec.func('1 + 2')}")

        # with kwargs
        print(f"Add 1 + 2: {add.func(a=1, b=2)}")
        print(f"Subtract 5 - 3: {sub.func(a=5, b=3)}")
        print(f"Multiply 2 * 3: {mul.func(a=2, b=3)}")
        print(f"Execute code: {code_exec.func(code='1 + 2')}")

        print("Documents: ", r.docs)
        # you can open this url in browser to see the API Endpoints
        # before the runtime is stopped.

    # you can also use the runtime without the with statement
    # runtime.build()
    # runtime.stop()

"""
Add 1 + 2: 3
Subtract 5 - 3: 2
Multiply 2 * 3: 6
Execute code: Executed the code below:
```py
1 + 2
```
> Executed Results:
3
Documents:  http://localhost:8000/docs
"""



--------------------------------------------------------------------------------
# File: runtime\docker_runtime_with_tasks.py
--------------------------------------------------------------------------------

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

from colorama import Fore

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.runtime import DockerRuntime, TaskConfig
from camel.toolkits.code_execution import CodeExecutionToolkit
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated

# tools
toolkit = CodeExecutionToolkit(verbose=True)

runtime = (
    DockerRuntime("xukunliu/camel")  # change to your own docker image
    .add(
        toolkit.get_tools(),
        "camel.toolkits.CodeExecutionToolkit",
        {"unsafe_mode": True, "import_white_list": ["os", "sys"]},
        True,
    )
    .add_task(
        TaskConfig(
            cmd="mkdir /home/test",
        )
    )
)

tools = runtime.get_tools()

# set up LLM model
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=assistant_model_config.as_dict(),
)


# set up agent
assistant_sys_msg = (
    "You are a personal assistant and programmer. "
    "When asked a question, "
    "write and run Python code to answer the question."
    "Your code will be executed using eval()."
)

agent = ChatAgent(
    assistant_sys_msg,
    model,
    tools=tools,
)
agent.reset()


# set up agent

with runtime as r:
    r.wait()
    prompt = "List all directories in /home"
    print(Fore.YELLOW + f"user prompt:\n{prompt}\n")

    response = agent.step(prompt)
    for msg in response.msgs:
        print_text_animated(Fore.GREEN + f"Agent response:\n{msg.content}\n")


# TODO: unlock unsafe mode
# This example can not be run in the current version of CAMEL because
# the InternalPythonInterpreter does not support
# most of the built-in functions.



--------------------------------------------------------------------------------
# File: runtime\remote_http_runtime.py
--------------------------------------------------------------------------------

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
from camel.runtime import RemoteHttpRuntime
from camel.toolkits import MathToolkit

if __name__ == "__main__":
    runtime = (
        RemoteHttpRuntime("localhost")
        .add(MathToolkit().get_tools(), "camel.toolkits.MathToolkit")
        .build()
    )
    print("Waiting for runtime to be ready...")
    runtime.wait()
    print("Runtime is ready.")
    add, sub, mul = runtime.get_tools()
    print(f"Add 1 + 2: {add.func(1, 2)}")
    print(f"Subtract 5 - 3: {sub.func(5, 3)}")
    print(f"Multiply 2 * 3: {mul.func(2, 3)}")

    print("Documents: ", runtime.docs)
    # you can open this url in browser to see the API Endpoints
    # before the runtime is stopped.
    # time.sleep(60)

    # call runtime.stop() if you want to stop the runtime manually
    # atherwise it will be stopped automatically when the program ends


"""
Waiting for runtime to be ready...
Runtime is ready.
Add 1 + 2: 3
Subtract 5 - 3: 2
Multiply 2 * 3: 6
Documents:  http://localhost:8000/docs
"""



--------------------------------------------------------------------------------
# File: schema_outputs\openai_converter_example.py
--------------------------------------------------------------------------------

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

from pydantic import BaseModel

from camel.schemas import OpenAISchemaConverter


def get_temperature(location: str, date: str, temperature: float):
    print(f"Temperature in {location} on {date} is {temperature} degrees.")


class Temperature(BaseModel):
    location: str
    date: str
    temperature: float


temperature_template = (
    '{"location": "Beijing", "date": "2023-09-01", "temperature": 30.0}'
)


model = OpenAISchemaConverter()

print(
    model.convert(
        "Today is 2023-09-01, the temperature in Beijing is 30 degrees.",
        output_schema=temperature_template,
    )
)

print(
    model.convert(
        "Today is 2023-09-01, the temperature in Beijing is 30 degrees.",
        output_schema=get_temperature,
    )
)

print(
    model.convert(
        "Today is 2023-09-01, the temperature in Beijing is 30 degrees.",
        output_schema=Temperature,
    )
)
"""
location='Beijing' date='2023-09-01' temperature=30.0
location='Beijing' date='2023-09-01' temperature=30.0
location='Beijing' date='2023-09-01' temperature=30.0
"""



--------------------------------------------------------------------------------
# File: schema_outputs\outlines_converter_example.py
--------------------------------------------------------------------------------

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

from pydantic import BaseModel

from camel.schemas import OutlinesConverter

# Define the model using OutlinesConverter
model = OutlinesConverter(
    model_type="microsoft/Phi-3-mini-4k-instruct", platform="transformers"
)

######## Regex conversion #########

time_regex_pattern = r"(0?[1-9]|1[0-2]):[0-5]\d\s?(am|pm)?"
output = model.convert_regex(
    "The the best time to visit a dentist is at ", time_regex_pattern
)

print(output)
"""
===============================================================================
6:00 pm
===============================================================================
"""


######## Pydantic conversion #########


# Using a Pydantic model
class Temperature(BaseModel):
    location: str
    date: str
    temperature: float


output = model.convert_pydantic(
    "Today is 2023-09-01, the temperature in Beijing is 30 degrees.",
    output_schema=Temperature,
)

print(type(output))
"""
===============================================================================
<class '__main__.Temperature'>
===============================================================================
"""
print(output)
"""
===============================================================================
location='Beijing' date='2023-09-01' temperature=30.0
===============================================================================
"""


######## JSON conversion #########

# 1. Using a JSON schema

schema = """
{
  "title": "User",
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "last_name": {"type": "string"},
    "id": {"type": "integer"}
  },
  "required": ["name", "last_name", "id"]
}
"""

output = model.convert_json(
    "Create a user profile with the fields name, last_name and id",
    output_schema=schema,
)
print(type(output))
"""
===============================================================================
<class 'dict'>
===============================================================================
"""
print(output)
"""
===============================================================================
{'name': 'John', 'last_name': 'Doe', 'id': 123456}
===============================================================================
"""

# 2. Using a function (Callable)


def get_temperature(location: str, date: str, temperature: float):
    print(f"Temperature in {location} on {date} is {temperature} degrees.")


output = model.convert_json(
    "Today is 2023-09-01, the temperature in Beijing is 30 degrees.",
    output_schema=get_temperature,
)

print(type(output))
"""
===============================================================================
<class 'dict'>
===============================================================================
"""
print(output)
"""
===============================================================================
{'location': 'Beijing', 'date': '2023-09-01', 'temperature': 30}
===============================================================================
"""


######## Type constraints #########

output = model.convert_type(
    "When I was 6 my sister was half my age. Now I'm 70 how old is my sister?",
    int,
)

print(output)
"""
===============================================================================
35
===============================================================================
"""


######## Multiple choices #########

output = model.convert_choice(
    "What is the capital of Spain?",
    ["Paris", "London", "Berlin", "Madrid"],
)

print(output)
"""
===============================================================================
Madrid
===============================================================================
"""


######## Grammar #########

arithmetic_grammar = """
    ?start: expression

    ?expression: term (("+" | "-") term)*

    ?term: factor (("*" | "/") factor)*

    ?factor: NUMBER
           | "-" factor
           | "(" expression ")"

    %import common.NUMBER
"""

output = model.convert_grammar(
    "Alice had 4 apples and Bob ate 2. "
    + "Write an expression for Alice's apples:",
    arithmetic_grammar,
)

print(output)
"""
===============================================================================
(8-2)
===============================================================================
"""



--------------------------------------------------------------------------------
# File: single_agent.py
--------------------------------------------------------------------------------

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
from camel.prompts import PromptTemplateGenerator
from camel.types import TaskType


def main(key: str = 'generate_users', num_roles: int = 50, model=None):
    prompt_template = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.AI_SOCIETY, key
    )
    prompt = prompt_template.format(num_roles=num_roles)
    print(prompt)
    agent = ChatAgent("You are a helpful assistant.", model=model)
    agent.reset()

    assistant_response = agent.step(prompt)
    print(assistant_response.msg.content)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: storages\nebular_graph.py
--------------------------------------------------------------------------------

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

from unstructured.documents.elements import Element

from camel.storages.graph_storages import NebulaGraph
from camel.storages.graph_storages.graph_element import (
    GraphElement,
    Node,
    Relationship,
)

# Step 2: Initialize the NebulaGraph client
host = '127.0.0.1'
username = 'root'
password = 'nebula'
space = 'space_name'

nebula_graph = NebulaGraph(host, username, password, space)

# Ensure necessary tags (node types) exist
nebula_graph.ensure_tag_exists("CAMEL_AI")
nebula_graph.ensure_tag_exists("Agent_Framework")

# Show existing tags
query = 'SHOW TAGS;'
print(nebula_graph.query(query))

"""
==============================================================================
ResultSet(keys: ['Name'], values: ["CAMEL_AI"],["Agent_Framework"])
==============================================================================
"""

# Add triplet
nebula_graph.add_triplet(
    subj="CAMEL_AI", obj="Agent_Framework", rel="contribute_to"
)

# Check structured schema
print(nebula_graph.get_structured_schema)

"""
==============================================================================
{'node_props': {'CAMEL_AI': [], 'Agent_Framework': []}, 'rel_props': 
{'contribute_to': []}, 'relationships': ['contribute_to'], 'metadata': 
{'index': []}}
==============================================================================
"""

# Delete triplet
nebula_graph.delete_triplet(
    subj="CAMEL_AI", obj="Agent_Framework", rel="contribute_to"
)

# Create and add graph element
node_camel = Node(
    id="CAMEL_AI",
    type="Agent_Framework",
)
node_nebula = Node(
    id="Nebula",
    type="Graph_Database",
)

graph_elements = [
    GraphElement(
        nodes=[node_camel, node_nebula],
        relationships=[
            Relationship(
                subj=node_camel,
                obj=node_nebula,
                type="Supporting",
            )
        ],
        source=Element(element_id="a05b820b51c760a41415c57c1eef8f08"),
    )
]

# Add this graph element to graph db
nebula_graph.add_graph_elements(graph_elements)

# Get structured schema
print(nebula_graph.get_structured_schema)

"""
==============================================================================
{'node_props': {'Agent_Framework': [], 'CAMEL_AI': [], 'Graph_Database': [], 
'Nebula': [], 'agent_framework': []}, 'rel_props': {'Supporting': [], 
'contribute_to': []}, 'relationships': ['Supporting', 'contribute_to'], 
'metadata': {'index': []}}
==============================================================================
"""



--------------------------------------------------------------------------------
# File: storages\redis_storage.py
--------------------------------------------------------------------------------

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

import logging
from typing import Any, Dict, List

from camel.storages import RedisStorage


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    sid = "example_sid"
    url = "redis://localhost:6379"
    storage = RedisStorage(sid=sid, url=url)

    with storage:
        records: List[Dict[str, Any]] = [
            {"id": 1, "name": "Record1"},
            {"id": 2, "name": "Record2"},
        ]

        storage.save(records)
        logger.info("Records saved successfully.")

        loaded_records = storage.load()
        logger.info(f"Loaded records: {loaded_records}")
        """
        Loaded records: [{'id': 1, 'name': 'Record1'}, {'id': 2, 'name': 
        'Record2'}]
        """

        storage.clear()
        logger.info("Records cleared successfully.")
        """
        Records cleared successfully.
        """

        loaded_records_after_clear = storage.load()
        logger.info(
            f"Loaded records after clear: {loaded_records_after_clear}"
        )
        """
        Loaded records after clear: []
        """


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: storages\s3_storage.py
--------------------------------------------------------------------------------

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

from pathlib import Path

from camel.storages.object_storages import AmazonS3Storage


def get_file():
    s3_storage = AmazonS3Storage(bucket_name="camel-ai-bucket")
    print(s3_storage._get_file(Path("folder1/example.txt")))


def upload_file():
    s3_storage = AmazonS3Storage(bucket_name="camel-ai-bucket")
    s3_storage.upload_file(
        local_file_path=Path("./redis_storage.py"),
        s3_file_path=Path("folder1/redis_storage.py"),
    )


if __name__ == "__main__":
    upload_file()



--------------------------------------------------------------------------------
# File: storages\tidb_vector_storage.py
--------------------------------------------------------------------------------

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

from camel.storages.vectordb_storages import (
    TiDBStorage,
    VectorDBQuery,
    VectorRecord,
)

"""
Before the DATABASE_URL, you can setup the a TiDB database cluster first:

(Option 1): TiDB Serverless

1. Go to [TiDB Cloud](https://tidbcloud.com/console/clusters) to create 
    a serverless cluster
2. Click the **Connect** button
3. Select "SQLAlchemy" > "PyMySQL" for the **Connect With** option, then 
    you can get the DATABASE_URL like:

DATABASE_URL="mysql+pymysql://<USERNAME>:<PASSWORD>@<HOST>:4000/test&ssl_verify_cert=true&ssl_verify_identity=true"

(Option 2): TiDB playground cluster on local

1. Install TiUP via command:

```
curl --proto '=https' --tlsv1.2 -sSf \
    https://tiup-mirrors.pingcap.com/install.sh | sh
```

2. Deploy a playground cluster via command: `tiup playground`
3. The DATABASE_URL should be like: "mysql+pymysql://root:@localhost:4000/test"
"""

DATABASE_URL = "mysql+pymysql://root:@localhost:4000/test"


def main():
    # Create an instance of TiDBStorage with dimension = 4
    tidb_storage = TiDBStorage(
        url_and_api_key=(DATABASE_URL, ''),
        vector_dim=4,
        collection_name="my_collection",
    )

    # Add two vector records
    tidb_storage.add(
        [
            VectorRecord(
                vector=[-0.1, 0.1, -0.1, 0.1],
                payload={'key1': 'value1'},
            ),
            VectorRecord(
                vector=[-0.1, 0.1, 0.1, 0.1],
                payload={'key2': 'value2'},
            ),
        ]
    )

    # Query similar vectors
    query_results = tidb_storage.query(
        VectorDBQuery(query_vector=[0.1, 0.2, 0.1, 0.1], top_k=1)
    )
    for result in query_results:
        print(result.record.payload, result.similarity)

    """
    Output:
    {'key2': 'value2'} 0.5669466755703252
    """

    # Clear all vectors
    tidb_storage.clear()


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: structured_response\json_format_reponse_with_tools.py
--------------------------------------------------------------------------------

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

from pydantic import BaseModel, Field

from camel.agents import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import (
    MathToolkit,
    SearchToolkit,
)
from camel.types import ModelPlatformType, ModelType

tools_list = [
    *MathToolkit().get_tools(),
    *SearchToolkit().get_tools(),
]
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

# Define system message
assistant_sys_msg = "You are a helpful assistant."

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=assistant_model_config.as_dict(),
)

# Set agent
camel_agent = ChatAgent(
    assistant_sys_msg,
    model=model,
    tools=tools_list,
)


# pydantic basemodel as input params format
class Schema(BaseModel):
    current_age: str = Field(
        description=" the current age of University of Oxford"
    )
    calculated_age: str = Field(description="the add more years of age")


user_msg = "Assume now is 2024 in the Gregorian calendar, "
"estimate the current age of University of Oxford "
"and then add 10 more years to this age, "

# Get response information
response = camel_agent.step(user_msg, response_format=Schema)
print(response.msgs[0].content)
"""
{'current_age': '928', 'calculated_age': '938'}
"""



--------------------------------------------------------------------------------
# File: structured_response\json_format_response.py
--------------------------------------------------------------------------------

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

from pydantic import BaseModel, Field

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

# Define system message
assistant_sys_msg = "You are a helpful assistant."

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
)

# Set agent
camel_agent = ChatAgent(assistant_sys_msg, model=model)


# pydantic basemodel as input params format
class JokeResponse(BaseModel):
    joke: str = Field(description="a joke")
    funny_level: str = Field(description="Funny level, from 1 to 10")


# Get response information
response = camel_agent.step("Tell me a joke.", response_format=JokeResponse)
print(response.msgs[0].content)
"""
{'joke': "Why couldn't the bicycle find its way home? It lost its bearings!"
, 'funny_level': '8'}
"""



--------------------------------------------------------------------------------
# File: structured_response\structure_response_prompt_engineering.py
--------------------------------------------------------------------------------

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
from pydantic import BaseModel

from camel.agents import ChatAgent
from camel.configs import QwenConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType


# Define Pydantic models
class Student(BaseModel):
    name: str
    age: str
    email: str


class StudentList(BaseModel):
    studentList: list[Student]


# Define Qwen model
qwen_model = ModelFactory.create(
    model_platform=ModelPlatformType.QWEN,
    model_type=ModelType.QWEN_TURBO,
    model_config_dict=QwenConfig().as_dict(),
)

qwen_agent = ChatAgent(
    model=qwen_model,
)

user_msg = """give me 1 student info."""

# Get response information
response0 = qwen_agent.step(user_msg, response_format=None)
print(response0.msgs[0].content)
"""
===============================================================================
Certainly! Below is an example of a student's information:

**Student Name:** Emily Johnson  
**Date of Birth:** March 12, 2005  
**Grade:** 10th Grade  
**School:** Lincoln High School  
**Address:** 456 Oak Street, Springfield, IL 62704  
**Phone Number:** (555) 123-4567  
**Email:** emily.johnson@student.lincolnhs.edu  
**Emergency Contact:** John Johnson (Father) - (555) 987-6543  

Is there anything specific you need or any changes you'd like to make?
===============================================================================
"""

# Get response information
response1 = qwen_agent.step(user_msg, response_format=Student)
print(response1.msgs[0].content)
"""
===============================================================================
{
  "name": "Emily Johnson",
  "age": "18",
  "email": "emily.johnson@student.lincolnhs.edu"
}
===============================================================================
"""
print(response1.msgs[0].parsed)
"""
===============================================================================
name='Emily Johnson' age='18' email='emily.johnson@student.lincolnhs.edu'
===============================================================================
"""
print(type(response1.msgs[0].parsed))
"""
===============================================================================
<class '__main__.Student'>
===============================================================================
"""

user_msg = """give me a list of student infos."""

# Get response information
response2 = qwen_agent.step(user_msg, response_format=StudentList)
print(response2.msgs[0].content)
"""
===============================================================================
{
  "studentList": [
    {
      "name": "Emily Johnson",
      "age": "18",
      "email": "emily.johnson@student.lincolnhs.edu"
    }
  ]
}
===============================================================================
"""

print(response2.msgs[0].parsed)
"""
===============================================================================
studentList=[Student(name='Emily Johnson', age='18', email='emily.johnson@student.lincolnhs.edu')] 
===============================================================================
"""  # noqa: E501

print(type(response2.msgs[0].parsed))
"""
===============================================================================
<class '__main__.StudentList'>
===============================================================================
"""



--------------------------------------------------------------------------------
# File: summarization\gpt_solution_extraction.py
--------------------------------------------------------------------------------

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
import argparse
import concurrent.futures
import itertools
import json
import os
import random
from typing import Dict, Tuple

import numpy as np

from camel.agents import ChatAgent
from camel.prompts import SolutionExtractionPromptTemplateDict
from camel.types import RoleType

parser = argparse.ArgumentParser(
    description='Arguments for conversation summarization.'
)
parser.add_argument(
    '--json_dir',
    type=str,
    help='Directory containing original json files',
    default='../camel/camel_data/ai_society',
)
parser.add_argument(
    '--solution_dir',
    type=str,
    help='Directory for solution json files',
    default='../camel/camel_data/ai_society_solution_extraction',
)
parser.add_argument(
    '--seed', type=int, help='Seed for reproducibility', default=10
)


def flatten_conversation(conversation: Dict) -> str:
    r"""Format a conversation into a string.

    Args:
        conversation (Dict): A dictionary containing
            information about the conversation.

    Returns:
        str: A string containing the specified task and
            all messages in the conversation.

    Raises:
        ValueError: If an unknown role name is encountered
            in the conversation.

    The conversation is formatted in the following format:
    Task: <specified_task>
    User (<role_1>): <message_1>
    Assistant (<role_2>): <message_2>
    ...

    Example:
        >>> conversation = {
        ...     'num_messages': 2,
        ...     'message_1': {'role_name': 'Engineer', 'content': 'Hello'},
        ...     'message_2': {'role_name': 'Programmer',
                              'content': 'Hi there!'},

        ...     'specified_task': 'Answer a greeting'
        ... }
        >>> flatten_conversation(conversation)
        'Task: Answer a greeting
            User (Engineer): Hello
            Assistant (Programmer): Hi there!'

    """

    num_messages = conversation['num_messages']
    assert num_messages >= 2
    role_1 = conversation['message_1']['role_name']
    role_2 = conversation['message_2']['role_name']
    task = conversation['specified_task']

    messages = []
    for i in range(1, num_messages + 1):
        if conversation[f'message_{i}']['role_name'] == role_1:
            message = (
                f"User ({role_1}): " + conversation[f'message_{i}']['content']
            )
        elif conversation[f'message_{i}']['role_name'] == role_2:
            message = (
                f"Assistant ({role_2}): "
                + conversation[f'message_{i}']['content']
            )
        else:
            raise ValueError(
                "Unknown role name: "
                f"{conversation[f'message_{i}']['role_name']}"
            )
        messages.append(message)

    joined_messages = '\n'.join(messages)
    formatted_data = f"Task: {task}\n{joined_messages}"

    return formatted_data


def format_combination(combination: Tuple[int, int, int]):
    assistant_role, user_role, task = combination
    assistant_role_str = str(assistant_role).zfill(3)
    user_role_str = str(user_role).zfill(3)
    task_str = str(task).zfill(3)
    return f"{assistant_role_str}_{user_role_str}_{task_str}"


def solution_extraction(
    conversation: Dict,
    flattened_conversation: str,
    file_name: str,
    args: argparse.Namespace,
) -> None:
    solution_extraction_template = SolutionExtractionPromptTemplateDict()
    assistant_sys_msg_prompt = solution_extraction_template[RoleType.ASSISTANT]

    # We use GPT4 because it has a longer context length
    agent = ChatAgent(assistant_sys_msg_prompt)
    agent.reset()

    prompt = "Here is the conversation:" + flattened_conversation

    assistant_response = agent.step(prompt)
    print(assistant_response.msg.content)

    # Create folder to write solution_extraction to
    if not os.path.exists(args.solution_dir):
        os.makedirs(args.solution_dir)

    # Append to the original JSON conversation file
    conversation['solution_extraction'] = assistant_response.msg.content

    # Save new dictionary as JSON file
    save_path = os.path.join(args.solution_dir, f'{file_name}.json')
    with open(save_path, "w") as f:
        json.dump(conversation, f, ensure_ascii=False)


def main():
    args = parser.parse_args()
    np.random.seed(args.seed)
    random.seed(args.seed)

    total_num_assistant_roles = 50
    total_num_user_roles = 50
    total_num_tasks = 1

    subsample_num_assistant_roles = 10
    subsample_num_user_roles = 10
    subsample_num_tasks = 1

    # Randomly subsample `subsample_num_assistant_roles`
    # of the total assistant roles
    subsampled_assistant_roles = random.sample(
        range(1, total_num_assistant_roles + 1), subsample_num_assistant_roles
    )

    # Randomly subsample `subsample_num_user_roles` of the total user roles
    subsampled_user_roles = random.sample(
        range(1, total_num_user_roles + 1), subsample_num_user_roles
    )

    # Randomly subsample `subsample_num_tasks` of the total tasks
    subsampled_tasks = random.sample(
        range(1, total_num_tasks + 1), subsample_num_tasks
    )

    file_names = list(
        itertools.product(
            subsampled_assistant_roles, subsampled_user_roles, subsampled_tasks
        )
    )

    # Formatting is needed to match the names of the original
    # generated JSON files xxx_xxx_xxx.json
    file_names = [
        format_combination(combination) for combination in file_names
    ]

    # Check that all files exist
    for file_name in file_names:
        json_file = os.path.join(args.json_dir, f"{file_name}.json")
        if not os.path.exists(json_file):
            raise ValueError(f"File {json_file} does not exist.")

    # Read in json files and extract solutions
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        futures = []
        for file_name in file_names:
            json_file = os.path.join(args.json_dir, f"{file_name}.json")
            with open(json_file) as f:
                conversation = json.load(f)
            flattened_conversation = flatten_conversation(conversation)
            futures.append(
                executor.submit(
                    solution_extraction,
                    conversation,
                    flattened_conversation,
                    file_name,
                    args,
                )
            )

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Exception: {e}")


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: summarization\gpt_solver.py
--------------------------------------------------------------------------------

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
import concurrent.futures
import json
import os
from typing import Dict

from camel.agents import ChatAgent

# Directory containing your json files of CAMEL conversations
# This code will append a new key called "gpt_solution" to each json file
# Containing GPT solution to the specified task in the json file

# dir_files = "./camel_data/ai_society_solution_extraction_plus_gpt_solution"
data_dir = "./camel_data/ai_society_solution_extraction"
save_dir = "./camel_data/ai_society_solution_extraction_save"


def process_file(data: Dict[str, str]) -> None:
    print(data["id"])
    assistant_sys_msg = "You are a helpful assistant."
    agent = ChatAgent(assistant_sys_msg)
    agent.reset()

    prompt = "Solve the following task:\n" + data["specified_task"]
    assistant_response = agent.step(prompt)
    print(assistant_response.msg.content)

    # Append solution to JSON file as "gpt_solution"
    data["gpt_solution"] = assistant_response.msg.content

    # create save_dir if not exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # save result as json file
    with open(os.path.join(save_dir, data["id"] + ".json"), 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def main():
    # read all json files in data_dir
    files = [f for f in os.listdir(data_dir) if f.endswith('.json')]

    # load all json files as data list
    data_list = []
    for file in files:
        with open(os.path.join(data_dir, file)) as f:
            data_list.append(json.load(f))

    # Specify number of processes with max_workers argument (default: 16)
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        futures = []
        for data in data_list:
            futures.append(executor.submit(process_file, data))

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Exception occurred: {e}")


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: tasks\task_generation.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.tasks import (
    Task,
    TaskManager,
)
from camel.types import (
    ModelPlatformType,
    ModelType,
)

# set up LLM model
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=assistant_model_config.as_dict(),
)

# set up agent
assistant_sys_msg = "You are a personal math tutor and programmer."
agent = ChatAgent(assistant_sys_msg, model)
agent.reset()

task = Task(
    content="Weng earns $12 an hour for babysitting. Yesterday, she just did 51 minutes of babysitting. How much did she earn?",
    id="0",
)
print(task.to_string())


task_manager = TaskManager(task)

evolved_task = task_manager.evolve(task, agent=agent)
if evolved_task is not None:
    print(evolved_task.to_string())
else:
    print("Evolved task is None.")


new_tasks = task.decompose(agent=agent)
for t in new_tasks:
    print(t.to_string())

# ruff: noqa: E501
"""
===============================================================================
Task 0: Weng earns $12 an hour for babysitting. Yesterday, she just did 51 
minutes of babysitting. How much did she earn?

Task 0.0: Weng earns $12 an hour for babysitting. However, her hourly rate 
increases by $2 for every additional hour worked beyond the first hour. 
Yesterday, she babysat for a total of 3 hours and 45 minutes. How much did she 
earn in total for her babysitting services?

Task 0.0: Convert 51 minutes to hours.

Task 0.1: Calculate the proportion of 51 minutes to an hour.

Task 0.2: Multiply the proportion by Weng's hourly rate to find out how much 
she earned for 51 minutes of babysitting.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: test\test_ai_society_example.py
--------------------------------------------------------------------------------

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
from mock import patch

import examples.ai_society.role_playing
import examples.toolkits.role_playing_with_functions
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

test_model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.STUB,
)


def test_ai_society_role_playing_example():
    with patch('time.sleep', return_value=None):
        examples.ai_society.role_playing.main(
            model=test_model, chat_turn_limit=2
        )


def test_role_playing_with_function_example():
    with patch('time.sleep', return_value=None):
        examples.toolkits.role_playing_with_functions.main(
            model_platform=ModelPlatformType.DEFAULT,
            model_type=ModelType.STUB,
            chat_turn_limit=2,
        )



--------------------------------------------------------------------------------
# File: test\test_babyagi_example.py
--------------------------------------------------------------------------------

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
import pytest
from mock import patch

import examples.ai_society.babyagi_playing
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

parametrize = pytest.mark.parametrize(
    'model',
    [
        ModelFactory.create(
            model_platform=ModelPlatformType.OPENAI,
            model_type=ModelType.STUB,
        ),
        pytest.param(None, marks=pytest.mark.model_backend),
    ],
)


@parametrize
def test_ai_society_babyagi_playing_example(model):
    with patch('time.sleep', return_value=None):
        examples.ai_society.babyagi_playing.main(
            model=model, chat_turn_limit=2
        )



--------------------------------------------------------------------------------
# File: test\test_code_example.py
--------------------------------------------------------------------------------

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
from mock import patch

import examples.code.role_playing
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType


def test_code_role_playing_example():
    with patch('time.sleep', return_value=None):
        examples.code.role_playing.main(
            ModelFactory.create(
                model_platform=ModelPlatformType.OPENAI,
                model_type=ModelType.STUB,
            ),
            chat_turn_limit=2,
        )



--------------------------------------------------------------------------------
# File: test\test_role_description_example.py
--------------------------------------------------------------------------------

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
from mock import patch

import examples.role_description.role_generation
import examples.role_description.role_playing_with_role_description
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

model_gpt = ModelFactory.create(
    ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O,
)

model_stub = ModelFactory.create(
    ModelPlatformType.OPENAI,
    model_type=ModelType.STUB,
)


def test_role_generation_example():
    with patch('time.sleep', return_value=None):
        examples.role_description.role_generation.main(model_gpt)


def test_role_playing_with_role_description_example():
    with patch('time.sleep', return_value=None):
        examples.role_description.role_playing_with_role_description.main(
            model_gpt, model_stub, chat_turn_limit=2
        )



--------------------------------------------------------------------------------
# File: test\test_single_agent.py
--------------------------------------------------------------------------------

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
import pytest

import examples.code.generate_meta_data
import examples.code.task_generation
import examples.evaluation.single_agent
import examples.misalignment.single_agent
import examples.single_agent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

parametrize = pytest.mark.parametrize(
    'model',
    [
        ModelFactory.create(
            ModelPlatformType.OPENAI,
            model_type=ModelType.STUB,
        ),
        pytest.param(None, marks=pytest.mark.model_backend),
    ],
)


@parametrize
def test_single_agent(model):
    examples.single_agent.main(model=model)


@pytest.mark.parametrize(
    'model',
    [
        ModelFactory.create(
            ModelPlatformType.OPENAI,
            model_type=ModelType.STUB,
        )
    ],
)
def test_misalignment_single_agent(model):
    examples.misalignment.single_agent.main(model=model)


@parametrize
def test_evaluation_single_agent(model):
    examples.evaluation.single_agent.main(model=model)


@parametrize
def test_code_generate_metadata(model):
    examples.code.generate_meta_data.main(model=model)


@pytest.mark.parametrize(
    'model',
    [
        ModelFactory.create(
            ModelPlatformType.OPENAI,
            model_type=ModelType.STUB,
        )
    ],
)
def test_code_task_generation(model):
    examples.code.task_generation.main(model=model)



--------------------------------------------------------------------------------
# File: test\test_unstructured_io_example.py
--------------------------------------------------------------------------------

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

import pytest

from examples.loaders.unstructured_io_example import (
    chunk_url_content_example,
    clean_text_example,
    extract_data_example,
    parse_file_example,
    parse_url_example,
    stage_data_example,
)


@pytest.fixture
def sample_url():
    return (
        "https://www.cnn.com/2023/01/30/sport/empire-state-building-green-"
        "philadelphia-eagles-spt-intl/index.html"
    )


@pytest.fixture
def sample_dirty_text():
    return "Some dirty text â€™ with extra spaces and – dashes."  # noqa: RUF001


@pytest.fixture
def sample_email_text():
    return "Contact me at example@email.com."


# Define test cases


def test_parse_file_example():
    # Setup: ensure any pre-existing 'mydoc.docx' is removed
    if os.path.exists("mydoc.txt"):
        os.remove("mydoc.txt")

    # Execution: call the function
    content = parse_file_example()

    # Assertion: check if the result is as expected
    expected_string = (
        "Important Analysis\n\nHere is my first "
        "thought.\n\nHere is my second thought."
    )
    assert content == expected_string

    # Cleanup: remove the created file after the test
    if os.path.exists("mydoc.txt"):
        os.remove("mydoc.txt")


def test_parse_url_example(sample_url):
    content = parse_url_example(sample_url)
    assert isinstance(content, str)
    assert len(content) > 0


def test_clean_text_example(sample_dirty_text):
    cleaned_text = clean_text_example(sample_dirty_text)
    assert isinstance(cleaned_text, str)
    assert cleaned_text == "Some dirty text with extra spaces and dashes."


def test_extract_data_example(sample_email_text):
    extracted_data = extract_data_example(sample_email_text)
    assert isinstance(extracted_data, list)
    assert extracted_data == ["example@email.com"]


def test_stage_data_example(sample_url):
    staged_data = stage_data_example(sample_url)
    assert isinstance(staged_data, dict)
    assert staged_data['rows'][0] == {
        'data': {
            'type': 'NarrativeText',
            'element_id': '0aafb4e862cf2f95e55f76b641766e39',
            'text': 'Miles Sanders scores a touchdown against the San Francisco 49ers during the NFC Championship game at Lincoln Financial Field.',  # noqa: E501
        },
        'metadata': {
            'languages': ['eng'],
            'filetype': 'text/html',
            'url': 'https://www.cnn.com/2023/01/30/sport/empire-state-building-green-philadelphia-eagles-spt-intl/index.html',
        },
    }


def test_chunk_url_content_example(sample_url):
    chunked_sections = chunk_url_content_example(sample_url)
    assert len(chunked_sections) == 7



--------------------------------------------------------------------------------
# File: toolkits\arxiv_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import ArxivToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = "You are a helpful assistant"

# Set model config
tools = ArxivToolkit().get_tools()
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message
usr_msg = "Search paper 'attention is all you need' for me"

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
'''
===============================================================================
[ToolCallingRecord(func_name='search_papers', args={'query': 'attention is 
all you need'}, result=[{'title': "Attention Is All You Need But You Don't 
Need All Of It For Inference of Large Language Models", 'published_date': 
'2024-07-22', 'authors': ['Georgy Tyukin', 'Gbetondji J-S Dovonon', 'Jean 
Kaddour', 'Pasquale Minervini'], 'entry_id': 'http://arxiv.org/abs/2407.
15516v1', 'summary': 'The inference demand for LLMs has skyrocketed in recent 
months, and serving\nmodels with low latencies remains challenging due to the 
quadratic input length\ncomplexity of the attention layers. In this work, we 
investigate the effect of\ndropping MLP and attention layers at inference time 
on the performance of\nLlama-v2 models. We find that dropping dreeper 
attention layers only marginally\ndecreases performance but leads to the best 
speedups alongside dropping entire\nlayers. For example, removing 33\\% of 
attention layers in a 13B Llama2 model\nresults in a 1.8\\% drop in average 
performance ove...
===============================================================================
'''


# Define a user message
usr_msg = """Download paper "attention is all you need" for me to my 
    local path '/Users/enrei/Desktop/camel0826/camel/examples/tool_call'"""

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
'''
===============================================================================
[ToolCallingRecord(func_name='download_papers', args={'query': 'attention 
is all you need', 'output_dir': '/Users/enrei/Desktop/camel0826/camel/examples/
tool_call', 'paper_ids': ['2407.15516v1', '2107.08000v1', '2306.01926v1', 
'2112.05993v1', '1912.11959v2']}, result='papers downloaded successfully')]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\ask_news_toolkit.py
--------------------------------------------------------------------------------

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

from camel.toolkits import AskNewsToolkit

ask_news = AskNewsToolkit()

news_output = ask_news.get_news(query="President of United States")
print(news_output[:1000])

"""
===============================================================================
<doc>
[1]:
Title: Can Elon Musk Become President of the United States?
Summary: Elon Musk, the American billionaire, has been appointed to lead the 
Department of Government Efficiency in Donald Trump's upcoming administration, 
sparking speculation about his potential presidential ambitions. However, 
according to the US Constitution, the President must be a natural-born citizen 
of the United States. As Musk was born in South Africa and became a Canadian 
citizen through his mother, he does not meet this requirement. While he 
acquired US citizenship in 2002, this does not make him a natural-born 
citizen. Additionally, the Constitution requires the President to be at least 
35 years old and a resident of the United States for at least 14 years. Musk 
can, however, hold other government positions, as the requirement of being a 
natural-born citizen only applies to the President and Vice President. Many 
non-US-born citizens have held prominent government positions in the past, 
including Henry
===============================================================================
"""

story_output = ask_news.get_stories(
    query="camel-ai", categories=["Technology"]
)
print(story_output)

web_search_output = ask_news.get_web_search(queries=["camel-ai"])
print(web_search_output)

reddit_output = ask_news.search_reddit(keywords=["camel-ai", "multi-agent"])
print(reddit_output)

finance_output = ask_news.query_finance(asset="bitcoin")
print(finance_output)



--------------------------------------------------------------------------------
# File: toolkits\audio_analysis_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory, OpenAIAudioModels
from camel.toolkits import AudioAnalysisToolkit
from camel.types import ModelPlatformType, ModelType

audio_models = OpenAIAudioModels()

# Set example input
input = """CAMEL-AI.org is an open-source community dedicated to the study of 
autonomous and communicative agents. We believe that studying these agents on 
a large scale offers valuable insights into their behaviors, capabilities, and 
potential risks. To facilitate research in this field, we provide, implement, 
and support various types of agents, tasks, prompts, models, datasets, and 
simulated environments.

Join us via Slack, Discord, or WeChat in pushing the boundaries of building AI 
Society."""

# Set example local path to store the file
storage_path = "examples/openai_audio_models/example_audio.mp3"

# Convert the example input into audio and store it locally
audio_models.text_to_speech(input=input, storage_path=storage_path)

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)


audio_reason_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

# Create the AudioAnalysisToolkit with our reasoning model
audio_toolkit = AudioAnalysisToolkit(audio_reasoning_model=audio_reason_model)

# Create a ChatAgent with the audio toolkit tools
agent = ChatAgent(
    system_message="You are an assistant specialized in audio analysis.",
    model=model,
    tools=[*audio_toolkit.get_tools()],
)

question = "What content can you hear in this audio?"
response = agent.step(
    f"I have an audio file at {storage_path}. Can you analyze it and tell "
    f"me {question}"
)
print(response.msgs[0].content)
print("\n")

response = agent.step(f"Please transcribe the audio file at {storage_path}")
print(response.msgs[0].content)
print("\n")

"""
==========================================================================
2025-03-09 22:54:55,822 - camel.camel.toolkits.audio_analysis_toolkit - 
WARNING - No audio transcription model provided. Using OpenAIAudioModels.

The audio content discusses Camel AI, an open-source community dedicated to 
the study of autonomous and communicative agents. It emphasizes the belief 
that large-scale research on these agents can yield valuable insights into 
their behaviors, capabilities, and potential risks. The community provides 
resources to support research, including various types of agents, tasks, 
prompts, models, datasets, and simulated environments. Additionally, it 
invites listeners to join the community through platforms like Slack, Discord, 
or WeChat to contribute to the development of AI society.


Here is the transcription of the audio:

"CamelAI.org is an open-source community dedicated to the study of autonomous 
and communicative agents. We believe that studying these agents on a large 
scale offers valuable insights into their behaviors, capabilities, and 
potential risks. To facilitate research in this field, we provide, implement, 
and support various types of agents, tasks, prompts, models, datasets, and 
simulated environments. Join us via Slack, Discord, or WeChat in pushing the 
boundaries of building AI society."
==========================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\browser_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import BrowserToolkit
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

web_agent_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

planning_agent_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

web_toolkit = BrowserToolkit(
    headless=False,
    web_agent_model=web_agent_model,
    planning_agent_model=planning_agent_model,
    channel="chromium",
)

agent = ChatAgent(
    system_message="You are a helpful assistant.",
    model=model,
    tools=[*web_toolkit.get_tools()],
)

response = agent.step(
    "Navigate to Amazon.com and identify the current #1 best-selling product"
    " in the gaming category. Please provide the product name, price, and"
    " rating if available.",
)

print(response.msgs[0].content)
"""
==========================================================================
The current #1 best-selling product in the gaming category on Amazon is the 
**AutoFull C3 Gaming Chair**. 

- **Price:** $249.99
- **Rating:** 4.4 stars based on 5,283 ratings.
==========================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\code_execution_toolkit.py
--------------------------------------------------------------------------------

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

from colorama import Fore

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits.code_execution import CodeExecutionToolkit
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated

# tools
toolkit = CodeExecutionToolkit(verbose=True)
tools = toolkit.get_tools()

# set up LLM model
assistant_model_config = ChatGPTConfig(
    temperature=0.0,
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=assistant_model_config.as_dict(),
)


# set up agent
assistant_sys_msg = (
    "You are a personal math tutor and programmer. "
    "When asked a math question, "
    "write and run Python code to answer the question."
)

agent = ChatAgent(
    assistant_sys_msg,
    model,
    tools=tools,
)
agent.reset()


# set up agent

prompt = (
    "Weng earns $12 an hour for babysitting. "
    "Yesterday, she just did 51 minutes of babysitting. How much did she earn?"
)
print(Fore.YELLOW + f"user prompt:\n{prompt}\n")

response = agent.step(prompt)
for msg in response.msgs:
    print_text_animated(Fore.GREEN + f"Agent response:\n{msg.content}\n")

# ruff: noqa: E501
"""
===============================================================================
user prompt:
Weng earns $12 an hour for babysitting. Yesterday, she just did 51 minutes of babysitting. How much did she earn?

Executed the code below:
```py
hourly_rate = 12
minutes_worked = 51
hourly_earnings = hourly_rate / 60 * minutes_worked
hourly_earnings
```
> Executed Results:
10.200000000000001
Agent response:
Weng earned $10.20 for babysitting for 51 minutes at a rate of $12 per hour.
===============================================================================
"""

agent_with_e2b = ChatAgent(
    assistant_sys_msg,
    model,
    tools=CodeExecutionToolkit(verbose=True, sandbox="e2b").get_tools(),
)
agent_with_e2b.reset()

print(Fore.YELLOW + f"user prompt:\n{prompt}\n")

response_with_e2b = agent_with_e2b.step(prompt)
for msg in response_with_e2b.msgs:
    print_text_animated(Fore.GREEN + f"Agent response:\n{msg.content}\n")

# ruff: noqa: E501
"""
===============================================================================
user prompt:
Weng earns $12 an hour for babysitting. Yesterday, she just did 51 minutes of babysitting. How much did she earn?

Executed the code below:
```py
hourly_wage = 12
minutes_worked = 51
# Convert minutes to hours
hours_worked = minutes_worked / 60
# Calculate earnings
earnings = hourly_wage * hours_worked
earnings
```
> Executed Results:
10.2
Agent response:
Weng earned $10.20 for 51 minutes of babysitting.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\dappier_toolkit.py
--------------------------------------------------------------------------------

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
from camel.toolkits import DappierToolkit, FunctionTool

real_time_data_response = DappierToolkit().search_real_time_data(
    query="camel-ai"
)

print(real_time_data_response)
"""
===============================================================================
CAMEL-AI is pretty cool! It's the first LLM (Large Language Model) multi-agent 
framework and an open-source community focused on exploring the scaling laws 
of agents. 🌟

Here are some highlights:

- **Purpose**: It aims to create highly customizable intelligent agents and 
    build multi-agent systems for real-world applications.
- **Features**: CAMEL provides a role-playing approach and inception prompting
    to help chat agents complete tasks aligned with human intentions.
- **Use Cases**: You can turn your database into an AI-powered data analyst,
    allowing you to ask questions in plain English and get instant insights.
    📊🤖
- **Community**: It's an open-source initiative, so developers can contribute
    and collaborate on building and using LLM-based agents.

If you want to dive deeper, check out their website:
[CAMEL-AI.org](https://www.camel-ai.org) 🚀!
===============================================================================
"""

# Use a different AI model which has access to real-time financial news.
real_time_data_response = DappierToolkit().search_real_time_data(
    query="Could you please provide the stock price for Google on 05/03/24?",
    ai_model_id="am_01j749h8pbf7ns8r1bq9s2evrh",
)
print(real_time_data_response)
"""
===============================================================================
The stock price for Google (GOOGL) on May 3rd, 2024, was $167.10.
===============================================================================
"""

# Example with ChatAgent using the Real Time Search.
agent = ChatAgent(
    system_message="""You are a helpful assistant that can use brave search 
        engine to answer questions.""",
    tools=[FunctionTool(DappierToolkit().search_real_time_data)],
)

usr_msg = "What is the temperature in Tokyo?"

response = agent.step(input_message=usr_msg, response_format=None)

print(response.msgs[0].content)
"""
===============================================================================
The current temperature in Tokyo is 50°F (about 10°C). It's a bit chilly, 
so you might want to grab a jacket! 🧥🌬️
===============================================================================
"""

ai_recommendations_response = DappierToolkit().get_ai_recommendations(
    query="latest sports news",
    data_model_id="dm_01j0pb465keqmatq9k83dthx34",
    similarity_top_k=3,
    ref="sportsnaut.com",
    num_articles_ref=2,
    search_algorithm="most_recent",
)
print(ai_recommendations_response)
"""
===============================================================================
{'author': 'Andrew Buller-Russ', 
'image_url': 'https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/
Syndication-Detroit-Free-Press-25087075_.jpg?width=428&height=321', 
'pubdate': 'Thu, 02 Jan 2025 03:12:06 +0000', 
'source_url': 'https://sportsnaut.com/nick-bosa-detroit-lions-trade-rumors-49ers/', 
'summary': 'In a thrilling Monday night game, the Detroit Lions triumphed 
over the San Francisco 49ers 40-34, solidifying their status as a top NFL 
team. Despite a strong performance from Nick Bosa, who recorded eight tackles 
and two sacks, the 49ers\' playoff hopes were dashed. Bosa praised the Lions\' 
competitive spirit and resilience under Coach Dan Campbell, sparking 
about his interest in joining the team, although he remains under contract 
with the 49ers for four more seasons. Bosa\'s admiration for the Lions 
highlights the stark contrast between the two franchises\' fortunes, 
with the Lions celebrating a significant victory while the 49ers struggle.
Having experienced playoff success with the 49ers, Bosa values strong 
leadership from both Campbell and his own coach, Kyle Shanahan. His comments 
reflect a broader sentiment in the NFL about the importance of winning and 
the positive environment it fosters for players.', 
'title': 'Nick Bosa gushes about Detroit Lions, sparking 49ers trade rumors'}

{'author': 'Andrew Buller-Russ', 
'image_url': 'https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/
Baseball-World-Baseball-Classic-Semifinal-Japan-vs-Mexico-20279015_.jpg?width=428&height=321', 
'pubdate': 'Thu, 02 Jan 2025 02:43:38 +0000', 
'source_url': 'https://www.lafbnetwork.com/los-angeles-dodgers/
los-angeles-dodgers-news/los-angeles-dodgers-meeting-roki-sasaki/', 
'summary': 'Roki Sasaki, a talented 23-year-old Japanese pitcher, is 
approaching a decision on his MLB free agency, with the Los Angeles Dodgers 
among the frontrunners to sign him. They are competing against teams like 
the Chicago Cubs, New York Mets, and others. The Dodgers are set to meet 
with Sasaki, emphasizing his signing as a top priority despite facing 
competition from around 20 other teams. Sasaki\'s status as a minor-league 
posting player may allow him to be signed at a more affordable price, 
increasing his appeal. As he gathers information and prepares for a second
round of meetings, the Dodgers are keen to secure him before the posting 
window closes on January 24, with the international signing period beginning 
on January 15.', 'title': 'Los Angeles Dodgers Take Another Step Toward 
Signing Roki Sasaki'}

{'author': 'Andrew Buller-Russ', 
'image_url': 'https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/
NFL-Detroit-Lions-at-Kansas-City-Chiefs-24020812_.jpg?width=428&height=321', 
'pubdate': 'Thu, 02 Jan 2025 02:08:34 +0000', 
'source_url': 'https://sportsnaut.com/detroit-lions-cut-jamal-adams/', 
'summary': 'The Detroit Lions, with a strong 14-2 record, have released 
former All-Pro safety Jamal Adams from their practice squad ahead of a crucial 
Week 18 game against the Minnesota Vikings. Adams, who joined the Lions on 
December 1, 2024, played in two games but recorded only three tackles in 
20 defensive snaps, representing a mere 17% of the team\'s defensive plays. 
This marks Adams\' second release this season, having previously been cut 
by the Tennessee Titans after three appearances. The Lions\' decision to part 
ways with Adams comes as they focus on their playoff positioning for the 
upcoming game.', 
'title': 'Detroit Lions cut bait with All-Pro ahead of Week 18 matchup with 
Vikings'}
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\data_commons_toolkit.py
--------------------------------------------------------------------------------

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
from camel.toolkits.data_commons_toolkit import DataCommonsToolkit

# Initialize the DataCommonsToolkit
dc_toolkit = DataCommonsToolkit()

# Example 1: Query Data Commons
geoId06_name_query = '''
SELECT ?name ?dcid 
WHERE {
    ?a typeOf Place .
    ?a name ?name .
    ?a dcid ("geoId/06" "geoId/21" "geoId/24") .
    ?a dcid ?dcid
}
'''
result = dc_toolkit.query_data_commons(geoId06_name_query)
print("Query Result:")
print(result)

'''
===============================================================================
Query Result:
[{'?name': 'Kentucky', '?dcid': 'geoId/21'}, 
 {'?name': 'California', '?dcid': 'geoId/06'}, 
 {'?name': 'Maryland', '?dcid': 'geoId/24'}]
===============================================================================
'''

# Example 2: Get Triples
dcids = ["geoId/06", "geoId/21", "geoId/24"]
triples = dc_toolkit.get_triples(dcids)
print("\nTriples for California, Kentucky, and Maryland:")
print(triples)

'''
===============================================================================
Triples for California, Kentucky, and Maryland:
{
    "geoId/06": [
        ("name", "California"),
        ("containedInPlace", "country/USA"),
        ...
    ],
    "geoId/21": [
        ("name", "Kentucky"),
        ("containedInPlace", "country/USA"),
        ...
    ],
    "geoId/24": [
        ("name", "Maryland"),
        ("containedInPlace", "country/USA"),
        ...
    ]
}
===============================================================================
'''

# Example 3: Get Statistical Time Series
place = "geoId/06"
stat_var = "Count_Person"
series = dc_toolkit.get_stat_time_series(place, stat_var)
print("\nPopulation Time Series for California:")
print(series)

'''
===============================================================================
Population Time Series for California:
{
    "2010": 37253956,
    "2011": 37594778,
    "2012": 37971427,
    ...
}
===============================================================================
'''

# Example 4: Get Property Values
dcids = ["geoId/06", "geoId/21", "geoId/24"]
prop = "containedInPlace"
values = dc_toolkit.get_property_values(dcids, prop)
print("\nContained In Place for California, Kentucky, and Maryland:")
print(values)

'''
===============================================================================
Contained In Place for California, Kentucky, and Maryland:
{
    "geoId/06": ["country/USA"],
    "geoId/21": ["country/USA"],
    "geoId/24": ["country/USA"]
}
===============================================================================
'''

# Example 5: Get Statistical Value
place = "geoId/06"
stat_var = "Count_Person"
date = "2021"
value = dc_toolkit.get_stat_value(place, stat_var, date)
print("\nPopulation of California in 2021:")
print(value)

'''
===============================================================================
Population of California in 2021:
39237836
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\excel_toolkit.py
--------------------------------------------------------------------------------

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
import tempfile

import pandas as pd

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import ExcelToolkit
from camel.types import ModelPlatformType, ModelType

# Create a sample Excel file for demonstration
temp_file = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
sample_file_path = temp_file.name

# Create a sample DataFrame
df = pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Seattle'],
        'Department': ['Engineering', 'Marketing', 'Finance'],
    }
)

# Save the DataFrame to the CSV file
df.to_csv(sample_file_path, index=False)
print(f"Created sample Excel file at: {sample_file_path}")

# Initialize the Excel toolkit
excel_toolkit = ExcelToolkit()

# Create a model using OpenAI
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

# Create a chat agent with the Excel toolkit
agent = ChatAgent(
    system_message=(
        "You are a helpful assistant that can analyze Excel files. "
        "Use the provided Excel toolkit to extract and analyze data."
    ),
    model=model,
    tools=[*excel_toolkit.get_tools()],
)

# Example: Ask the agent to analyze the Excel file
response = agent.step(
    f"Analyze the Excel file at {sample_file_path} and tell me what data "
    f"it contains."
)

print(response.msgs[0].content)

# Clean up the temporary file
if os.path.exists(sample_file_path):
    os.remove(sample_file_path)
    print(f"Removed temporary file: {sample_file_path}")

'''
===============================================================================
Created sample Excel file at: /var/folders/93/f_71_t957cq9cmq2gsybs4_40000gn/T/
tmpqweue66k.csv
The Excel file contains the following data:

| Name    | Age | City          | Department   |
|---------|-----|---------------|--------------|
| Alice   | 25  | New York      | Engineering   |
| Bob     | 30  | San Francisco | Marketing     |
| Charlie | 35  | Seattle       | Finance       |

### Summary:
- **Total Records**: 3
- **Columns**:
  - **Name**: Names of individuals
  - **Age**: Ages of individuals
  - **City**: Cities where individuals reside
  - **Department**: Departments where individuals work
Removed temporary file: /var/folders/93/f_71_t957cq9cmq2gsybs4_40000gn/T/
tmpqweue66k.csv
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\file_write_toolkit.py
--------------------------------------------------------------------------------

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
# ruff: noqa: E501
import os

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.toolkits import FileWriteToolkit
from camel.types import ModelPlatformType
from camel.types.enums import ModelType

# Create a model instance
model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict={"temperature": 0},
)

# Define system message for the agent
sys_msg = "You are a helpful assistant that can create and modify files."

# Set up output directory
output_dir = "./file_write_outputs"
os.makedirs(output_dir, exist_ok=True)

# Initialize the FileWriteToolkit with the output directory
file_toolkit = FileWriteToolkit(output_dir=output_dir)

# Get the tools from the toolkit
tools_list = file_toolkit.get_tools()

# Initialize a ChatAgent with the tools
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools_list,
)

# Example 1: Write a Python script to a file
python_query = """Please generate a Python script that creates a simple 
                  web server using Flask and save it to a file."""

camel_agent.reset()
response = camel_agent.step(python_query)
print("Example 1: Writing a Python script")
print(response.msgs[0].content)
print("Tool calls:", response.info['tool_calls'])
print("\n")
'''
===============================================================================
Example 1: Writing a Python script
The Python script for a simple web server using Flask has been created and saved as `simple_flask_server.py`. You can run this script to start the server, and it will return "Hello, Flask!" when accessed at the root URL.
Tool calls: [ToolCallingRecord(tool_name='write_to_file', args={'content': 'from flask import Flask\n\napp = Flask(__name__)\n\n@app.route(\'/\')\ndef home():\n    return "Hello, Flask!"\n\nif __name__ == \'__main__\':\n    app.run(debug=True)', 'filename': 'simple_flask_server.py', 'encoding': 'utf-8'}, result='Content successfully written to file: /Users/enrei/Desktop/camel0209/camel/file_write_outputs/simple_flask_server.py', tool_call_id='call_hCCxkjNkx4HKN9q6fuIpe8Bn')]
===============================================================================
'''

# Example 2: Create a JSON data file
json_query = """Generate a JSON file containing information about 3 fictional
                books, including title, author, publication year, and genre."""
camel_agent.reset()
response = camel_agent.step(json_query)
print("Example 2: Creating a JSON file")
print(response.msgs[0].content)
print("Tool calls:", response.info['tool_calls'])
print("\n")
'''
===============================================================================
Example 2: Creating a JSON file
The JSON file containing information about three fictional books has been successfully created. You can find it at the following location: **books.json**. 

Here is the content of the file:

```json
[
  {
    "title": "The Whispering Shadows",
    "author": "Ava Sinclair",
    "publication_year": 2021,
    "genre": "Fantasy"
  },
  {
    "title": "Echoes of the Past",
    "author": "Liam Carter",
    "publication_year": 2019,
    "genre": "Historical Fiction"
  },
  {
    "title": "The Last Star",
    "author": "Maya Thompson",
    "publication_year": 2022,
    "genre": "Science Fiction"
  }
]
```
Tool calls: [ToolCallingRecord(tool_name='write_to_file', args={'content': '[  \n  {  \n    "title": "The Whispering Shadows",  \n    "author": "Ava Sinclair",  \n    "publication_year": 2021,  \n    "genre": "Fantasy"  \n  },  \n  {  \n    "title": "Echoes of the Past",  \n    "author": "Liam Carter",  \n    "publication_year": 2019,  \n    "genre": "Historical Fiction"  \n  },  \n  {  \n    "title": "The Last Star",  \n    "author": "Maya Thompson",  \n    "publication_year": 2022,  \n    "genre": "Science Fiction"  \n  }  \n]', 'filename': 'books.json', 'encoding': 'utf-8'}, result='Content successfully written to file: /Users/enrei/Desktop/camel0209/camel/file_write_outputs/books.json', tool_call_id='call_1ayRgujHhiWowz0jhtMCukgn')]
===============================================================================
'''

# Example 3: Create a CSV file with tabular data
csv_query = """Create a CSV file with data about 5 countries, including
               columns for name, capital, population, area, and continent."""
camel_agent.reset()
response = camel_agent.step(csv_query)
print("Example 3: Creating a CSV file")
print(response.msgs[0].content)
print("Tool calls:", response.info['tool_calls'])
print("\n")
'''
===============================================================================
Example 3: Creating a CSV file
The CSV file containing data about 5 countries has been successfully created. It includes the following columns: name, capital, population, area, and continent. If you need any further modifications or additional data, feel free to ask!
Tool calls: [ToolCallingRecord(tool_name='write_to_file', args={'content': [['Name', 'Capital', 'Population', 'Area (sq km)', 'Continent'], ['United States', 'Washington, D.C.', '331002651', '9833517', 'North America'], ['Brazil', 'Brasília', '212559417', '8515767', 'South America'], ['Germany', 'Berlin', '83783942', '357022', 'Europe'], ['Australia', 'Canberra', '25499884', '7692024', 'Oceania'], ['Japan', 'Tokyo', '126476461', '377975', 'Asia']], 'filename': 'countries_data.csv', 'encoding': 'utf-8'}, result='Content successfully written to file: /Users/enrei/Desktop/camel0209/camel/file_write_outputs/countries_data.csv', tool_call_id='call_yTgErI2TrV32ehs5LJCf6kW7')]
===============================================================================
'''

# Example 4: Create a Markdown document
md_query = """Write a markdown document that explains the basics of machine
              learning, including headings, bullet points, and code examples.
              """
camel_agent.reset()
response = camel_agent.step(md_query)
print("Example 4: Creating a Markdown document")
print(response.msgs[0].content)
print("Tool calls:", response.info['tool_calls'])
print("\n")
'''
===============================================================================
Example 4: Creating a Markdown document
The markdown document explaining the basics of machine learning has been successfully created. You can find it under the name **basics_of_machine_learning.md**. If you need any further modifications or additional information, feel free to ask!
Tool calls: [ToolCallingRecord(tool_name='write_to_file', args={'content': "# Basics of Machine Learning\n\nMachine Learning (ML) is a subset of artificial intelligence (AI) that focuses on building systems that learn from data and improve their performance over time without being explicitly programmed. Here are the key concepts and components of machine learning:\n\n## Key Concepts\n\n- **Data**: The foundation of machine learning. Data can be structured (like tables) or unstructured (like images or text).\n- **Model**: A mathematical representation of a process that is trained on data to make predictions or decisions.\n- **Training**: The process of feeding data into a model to help it learn patterns.\n- **Testing**: Evaluating the model's performance on unseen data to ensure it generalizes well.\n- **Features**: Individual measurable properties or characteristics used as input to the model.\n- **Labels**: The output or target variable that the model is trying to predict.\n\n## Types of Machine Learning\n\n1. **Supervised Learning**: The model is trained on labeled data.\n   - **Examples**: Classification, Regression\n   - **Use Cases**: Spam detection, House price prediction\n\n2. **Unsupervised Learning**: The model is trained on unlabeled data and tries to find patterns.\n   - **Examples**: Clustering, Dimensionality Reduction\n   - **Use Cases**: Customer segmentation, Anomaly detection\n\n3. **Reinforcement Learning**: The model learns by interacting with an environment and receiving feedback.\n   - **Examples**: Game playing, Robotics\n   - **Use Cases**: Self-driving cars, Game AI\n\n## Machine Learning Workflow\n\n1. **Data Collection**: Gather data from various sources.\n2. **Data Preprocessing**: Clean and prepare the data for analysis.\n3. **Model Selection**: Choose the appropriate algorithm for the task.\n4. **Training the Model**: Fit the model to the training data.\n5. **Model Evaluation**: Assess the model's performance using metrics like accuracy, precision, and recall.\n6. **Hyperparameter Tuning**: Optimize the model's parameters for better performance.\n7. **Deployment**: Implement the model in a production environment.\n\n## Code Example\n\nHere is a simple example of a supervised learning model using Python and the popular library `scikit-learn`:\n\n```python\n# Import necessary libraries\nimport numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error\n\n# Load dataset\ndata = pd.read_csv('data.csv')\n\n# Define features and labels\nX = data[['feature1', 'feature2']]\nY = data['label']\n\n# Split the data into training and testing sets\nX_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)\n\n# Create a model\nmodel = LinearRegression()\n\n# Train the model\nmodel.fit(X_train, Y_train)\n\n# Make predictions\npredictions = model.predict(X_test)\n\n# Evaluate the model\nmse = mean_squared_error(Y_test, predictions)\nprint(f'Mean Squared Error: {mse}')\n```\n\n## Conclusion\n\nMachine learning is a powerful tool that can be applied to various fields, from healthcare to finance. Understanding the basics of machine learning is essential for anyone looking to leverage data for decision-making and predictive analytics.", 'filename': 'basics_of_machine_learning.md', 'encoding': 'utf-8'}, result='Content successfully written to file: /Users/enrei/Desktop/camel0209/camel/file_write_outputs/basics_of_machine_learning.md', tool_call_id='call_KKHcbPvmG8VWc4W2JeOWcg1B')]
===============================================================================
'''

# Example 5: Create a YAML configuration file
yaml_query = """Generate a YAML configuration file for a web application
                with settings for database connection, logging, and server
                parameters."""
camel_agent.reset()
response = camel_agent.step(yaml_query)
print("Example 5: Creating a YAML configuration file")
print(response.msgs[0].content)
print("Tool calls:", response.info['tool_calls'])
print("\n")
'''
===============================================================================
Example 5: Creating a YAML configuration file
The YAML configuration file for the web application has been successfully created. Here are the contents of the file:

```yaml
database:
  host: localhost
  port: 5432
  username: user
  password: password
  dbname: mydatabase

logging:
  level: info
  file: /var/log/myapp.log
  max_size: 10MB
  max_backups: 5

server:
  host: 0.0.0.0
  port: 8080
  timeout: 30s
  enable_https: true
```

The file is saved as `config.yaml`. If you need any modifications or additional settings, feel free to ask!
Tool calls: [ToolCallingRecord(tool_name='write_to_file', args={'content': 'database:\n  host: localhost\n  port: 5432\n  username: user\n  password: password\n  dbname: mydatabase\n\nlogging:\n  level: info\n  file: /var/log/myapp.log\n  max_size: 10MB\n  max_backups: 5\n\nserver:\n  host: 0.0.0.0\n  port: 8080\n  timeout: 30s\n  enable_https: true\n', 'filename': 'config.yaml', 'encoding': 'utf-8'}, result='Content successfully written to file: /Users/enrei/Desktop/camel0209/camel/file_write_outputs/config.yaml', tool_call_id='call_svQbTh8tl1diDDYwxNDWUp2U')]
===============================================================================
'''

# Example 6: Create an HTML file
html_query = """Create a simple HTML webpage with a header, navigation menu, 
                main content section, and footer."""
camel_agent.reset()
response = camel_agent.step(html_query)
print("Example 6: Creating an HTML file")
print(response.msgs[0].content)
print("Tool calls:", response.info['tool_calls'])
print("\n")
'''
===============================================================================
Example 6: Creating an HTML file
I have created a simple HTML webpage with a header, navigation menu, main content section, and footer. You can find the file named `simple_webpage.html` in the specified directory. If you need any modifications or additional features, feel free to ask!
Tool calls: [ToolCallingRecord(tool_name='write_to_file', args={'content': '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Simple Webpage</title>\n    <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n    <header>\n        <h1>Welcome to My Simple Webpage</h1>\n    </header>\n    <nav>\n        <ul>\n            <li><a href="#home">Home</a></li>\n            <li><a href="#about">About</a></li>\n            <li><a href="#services">Services</a></li>\n            <li><a href="#contact">Contact</a></li>\n        </ul>\n    </nav>\n    <main>\n        <section id="home">\n            <h2>Home</h2>\n            <p>This is the home section of the webpage.</p>\n        </section>\n        <section id="about">\n            <h2>About</h2>\n            <p>This section contains information about us.</p>\n        </section>\n        <section id="services">\n            <h2>Services</h2>\n            <p>Details about our services can be found here.</p>\n        </section>\n        <section id="contact">\n            <h2>Contact</h2>\n            <p>Get in touch with us through this section.</p>\n        </section>\n    </main>\n    <footer>\n        <p>&copy; 2023 My Simple Webpage. All rights reserved.</p>\n    </footer>\n</body>\n</html>', 'filename': 'simple_webpage.html', 'encoding': 'utf-8'}, result='Content successfully written to file: /Users/enrei/Desktop/camel0209/camel/file_write_outputs/simple_webpage.html', tool_call_id='call_6FUwTx4gSAB8mtN7lety05SP')]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\generate_openai_tool_schema.py
--------------------------------------------------------------------------------

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
from camel.toolkits import FunctionTool


# Define a function which doesn't have a docstring
def get_perfect_square(n: int) -> int:
    return n**2


# Create a FunctionTool with the function
function_tool = FunctionTool(
    get_perfect_square,
    synthesize_schema=True,
)
print("\nGenerated OpenAI Tool Schema:")
print(function_tool.get_openai_tool_schema())

# Set system message for the assistant
assistant_sys_msg = "You are a helpful assistant."

# Create a ChatAgent with the tool
camel_agent = ChatAgent(
    system_message=assistant_sys_msg, tools=[function_tool]
)
camel_agent.reset()

# Define a user message
user_prompt = "What is the perfect square of 2024?"
user_msg = user_prompt

# Get response from the assistant
response = camel_agent.step(user_msg)
print("\nAssistant Response:")
print(response.msg.content)

"""
===============================================================================
Warning: No model provided. Use `gpt-4o-mini` to generate the schema.

Generated OpenAI Tool Schema:
{'type': 'function', 'function': {'name': 'get_perfect_square', 'description':
'Calculates the perfect square of a given integer.', 'parameters':
{'properties': {'n': {'type': 'integer', 'description': 'The integer to be
squared.'}}, 'required': ['n'], 'type': 'object'}}}

Assistant Response:
The perfect square of 2024 is 4,096,576.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\github_toolkit.py
--------------------------------------------------------------------------------

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

from camel.toolkits import GithubToolkit

gt = GithubToolkit(repo_name="camel-ai/camel")

# Retrieve a list of all file paths within the camel GitHub repository
paths = gt.get_all_file_paths()
print(paths)
"""
===============================================================================
['.container/.env.example', '.container/Dockerfile', '.container/README.md', '.
container/docker-compose.yaml', '.container/minimal_build/Dockerfile', '.
github/ISSUE_TEMPLATE/bug_report.yml', '.github/ISSUE_TEMPLATE/discussions.
yml', '.github/ISSUE_TEMPLATE/feature_request.yml', '.github/ISSUE_TEMPLATE/
questions.yml', '.github/PULL_REQUEST_TEMPLATE.md', '.github/actions/
camel_install/action.yml', '.github/workflows/build_package.yml', '.github/
workflows/documentation.yml', '.github/workflows/pre_commit.yml', '.github/
workflows/publish_release.yml', '.github/workflows/pytest_apps.yml', '.github/
workflows/pytest_package.yml', '.gitignore', '.pre-commit-config.yaml', '.
style.yapf', 'CONTRIBUTING.md', 'LICENSE', 'Makefile', 'README.md', 'apps/
agents/README.md', 'apps/agents/agents.py', 'apps/agents/test/test_agents.py', 
'apps/agents/test/test_text_utils.py', 'apps/agents/text_utils.py', 'apps/
common/auto_zip.py', 'apps/common/test/test_archive_1.zip', 'apps/common/test/
test_auto_zip.py', 'apps/data_explorer/.gitignore', 'apps/data_explorer/README.
md', 'apps/data_explorer/data_explorer.py', 'apps/data_explorer/downloader.
py', 'apps/data_explorer/loader.py', 'apps/data_explorer/test/
test_data_explorer.py', 'apps/data_explorer/test/test_loader.py', 'apps/
dilemma/database_connection.py', 'apps/dilemma/dilemma.py', 'apps/dilemma/
requirements.txt', 'camel/__init__.py', 'camel/agents/__init__.py', 'camel/
agents/base.py', 'camel/agents/chat_agent.py', 'camel/agents/critic_agent.py', 
'camel/agents/deductive_reasoner_agent.py',...
===============================================================================
"""

# Retrieve the content of a specific file in the repository
content = gt.retrieve_file_content("camel/agents/chat_agent.py")
print(content[:1000])
"""
===============================================================================
from __future__ import annotations

import json
import logging
import re
import uuid
from collections import defaultdict
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

from openai.types.chat import ChatCompletionMessageToolCall
f
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\google_scholar_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import GoogleScholarToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = "You are a helpful assistant"

# Set model config
tools = GoogleScholarToolkit(
    author_identifier="https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en&oi=ao"
).get_tools()

model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message
usr_msg = "get the detailed information of this author"

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(func_name='get_author_detailed_info', args={}, result=
{'container_type': 'Author', 'filled': ['basics', 'indices', 'counts', 
'coauthors', 'publications', 'public_access'], 'scholar_id': 'JicYPdAAAAAJ', 
'source': <AuthorSource.AUTHOR_PROFILE_PAGE: 'AUTHOR_PROFILE_PAGE'>, 'name': 
'Geoffrey Hinton', 'url_picture': 'https://scholar.googleusercontent.com/
citations?view_op=view_photo&user=JicYPdAAAAAJ&citpid=2', 'affiliation': 
'Emeritus Prof. Computer Science, University of Toronto', 'organization': 
8515235176732148308, 'interests': ['machine learning', 'psychology', 
'artificial intelligence', 'cognitive science', 'computer science'], 
'email_domain': '@cs.toronto.edu', 'homepage': 'http://www.cs.toronto.edu/
~hinton', 'citedby': 853541, 'citedby5y': 560063, 'hindex': 186, 'hindex5y': 
137, 'i10index': 483, 'i10index5y': 368, 'cites_per_year': {1989: 2627, 1990: 
3589, 1991: 3766, 1992: 4091, 1993: 4573, 1994: 4499, 1995: 4090, 1996: 3935, 
1997: 3740, 1998: 3744, 1999: 3559, 2000: 3292, 2001: 3398, 2002: 3713, 2003: 
3670, 2004: 3393, 2005: 3813, 2006: 4168, 2007: 4558, 2008: 4349, 2009: 4784, 
2010: 5238, 2011: 5722, 2012: 6746, 2013: 9900, 2014: 12751, 2015: 18999, 
2016: 29932, 2017: 43675, 2018: 63544, 2019: 80800, 2020: 90523, 2021: 101735, 
2022: 104036, 2023: 106452, 2024: 76413}, 'coauthors': [{'container_type': 
'Author', 'filled': [], 'scholar_id': 'm1qAiOUAAAAJ', 'source': <AuthorSource.
CO_AUTHORS_LIST: 'CO_AUTHORS_LIST'>, 'name': 'Terrence Sejnowski', 
'affiliation': 'Francis Crick Professor, Salk Institute, Distinguished 
Professor, UC San Diego'}, {'container_type': 'Author', 'filled': [], 
'scholar_id': 'RnoIxUwAAAAJ', 'source': <AuthorSource.CO_AUTHORS_LIST: 
'CO_AUTHORS_LIST'>, 'name': 'Vinod Nair', 'affiliation': 'Research Scientist, 
DeepMind'}, {'container_type': 'Author', 'filled': [], 'scholar_id': 
'ghbWy-0AAAAJ', 'source': <AuthorSource.CO_AUTHORS_LIST: 'CO_AUTHORS_LIST'>, 
'name': 'George E. Dahl', 'affiliation': 'Google Inc.'}, {'container_
===============================================================================
"""

# Define a user message
usr_msg = "get the publications of this author"

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(func_name='get_author_publications', args={}, result=
['Imagenet classification with deep convolutional neural networks', 'Deep 
learning', 'Learning internal representations by error-propagation', 'Dropout: 
a simple way to prevent neural networks from overfitting', 'Visualizing data 
using t-SNE', 'Learning representations by back-propagating errors', 'Learning 
multiple layers of features from tiny images', 'Rectified linear units improve 
restricted boltzmann machines', 'Reducing the dimensionality of data with 
neural networks', 'A fast learning algorithm for deep belief nets', 
'Distilling the Knowledge in a Neural Network', 'A simple framework for 
contrastive learning of visual representations', 'Deep neural networks for 
acoustic modeling in speech recognition: The shared views of four research 
groups', 'Layer normalization', 'Speech recognition with deep recurrent neural 
networks', 'Improving neural networks by preventing co-adaptation of feature 
detectors', 'Lec
===============================================================================
"""

# ruff: noqa: E501
# Define a user message

usr_msg = """get the detailed information for publication with title: `Camel: Communicative agents for" mind" exploration of large language model society`"""

# Get response information
response = camel_agent.step(usr_msg)
print(response.info['tool_calls'])
"""
===============================================================================
[ToolCallingRecord(func_name='get_publication_by_title', args=
{'publication_title': 'Camel: Communicative agents for" mind" exploration of 
large language model society'}, result={'container_type': 'Publication', 
'source': <PublicationSource.AUTHOR_PUBLICATION_ENTRY: 
'AUTHOR_PUBLICATION_ENTRY'>, 'bib': {'title': 'Camel: Communicative agents 
for" mind" exploration of large language model society', 'pub_year': 2023, 
'citation': 'Advances in Neural Information Processing Systems 36, 2023', 
'author': 'Guohao Li and Hasan Hammoud and Hani Itani and Dmitrii Khizbullin 
and Bernard Ghanem', 'journal': 'Advances in Neural Information Processing 
Systems', 'volume': '36', 'abstract': 'The rapid advancement of chat-based 
language models has led to remarkable progress in complex task-solving. 
However, their success heavily relies on human input to guide the 
conversation, which can be challenging and time-consuming. This paper explores 
the potential of building scalable techniques to facilitate autonomous 
cooperation among communicative agents, and provides insight into their 
"cognitive" processes. To address the challenges of achieving autonomous 
cooperation, we propose a novel communicative agent framework named 
role-playing. Our approach involves using inception prompting to guide chat 
agents toward task completion while maintaining consistency with human 
intentions. We showcase how role-playing can be used to generate 
conversational data for studying the behaviors and capabilities of a society 
of agents, providing a valuable resource for investigating conversational 
language models. In particular, we conduct comprehensive studies on 
instruction-following cooperation in multi-agent settings. Our contributions 
include introducing a novel communicative agent framework, offering a scalable 
approach for studying the cooperative behaviors and capabilities of 
multi-agent systems, and open-sourcing our library to support research on 
communicative agents and beyond: https://github. com/camel-ai/camel.'}, 
'filled': True, 'author_pub_id': 'J9K-D0sAAAAJ:_Qo2XoVZTnwC', 'num_citations': 
364, 'citedby_url': '/scholar?hl=en&cites=3976259482297250805', 'cites_id': 
['3976259482297250805'], 'pub_url': 'https://proceedings.neurips.cc/
paper_files/paper/2023/hash/
a3621ee907def47c1b952ade25c67698-Abstract-Conference.html', 
'url_related_articles': '/scholar?oi=bibs&hl=en&q=related:9TMbme6CLjcJ:scholar.
google.com/', 'cites_per_year': {2023: 95, 2024: 269}})]
===============================================================================
"""

usr_msg = """get the full information for paper from link: `https://hal.science/hal-04206682/document`"""

# Get response information
response = camel_agent.step(usr_msg)
print((response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(func_name='get_full_paper_content_by_link', args=
{'pdf_url': 'https://hal.science/hal-04206682/document'}, result='Deep 
learning\nYann Lecun, Yoshua Bengio, Geoffrey Hinton\n\nTo cite this 
version:\n\nYann Lecun, Yoshua Bengio, Geoffrey Hinton. Deep learning. Nature, 
2015, 521 (7553), pp.436-444.\n\uffff10.1038/nature14539\uffff. 
\uffffhal-04206682\uffff\n\nHAL Id: hal-04206682\n\nhttps://hal.science/
hal-04206682v1\n\nSubmitted on 14 Sep 2023\n\nHAL is a multi-disciplinary open 
access\narchive for the deposit and dissemination of sci-\nentific research 
documents, whether they are pub-\nlished or not. The documents may come 
from\nteaching and research institutions in France or\nabroad, or from public 
or private research centers.\n\nL'archive ouverte pluridisciplinaire HAL, 
est\ndestinée au dépôt et à la diffusion de documents\nscientifiques de niveau 
recherche, publiés ou non,\némanant des établissements d'enseignement et 
de\nrecherche français ou étrangers, des laboratoires\npublics ou privés.
\n\n\x0cDeep learning\n\nYann LeCun1,2, Yoshua Bengio3 & Geoffrey Hinton4,
5\n\n1Facebook AI Research, 770 Broadway, New York, New York 10003 USA\n\n2N..
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\human_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import HumanToolkit
from camel.types import ModelPlatformType, ModelType

human_toolkit = HumanToolkit()

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

# Example 1: Test Agent with the human toolkit (ask_human_via_console)
print("\nExample 1: Using ask_human_via_console through an agent")
agent = ChatAgent(
    system_message="You are a helpful assistant.",
    model=model,
    tools=[*human_toolkit.get_tools()],
)

response = agent.step(
    "Test me on the capital of some country, and comment on my answer."
)

print(response.msgs[0].content)

"""
==========================================================================
What is the capital of France?
Your reply: Paris

That's correct! Paris is indeed the capital of France. Would you like to try
another one?
Your reply: yes

What is the capital of Japan?
Your reply: Tokyo

That's correct! Tokyo is the capital of Japan. Would you like to continue with
another question?
Your reply: no
==========================================================================
"""

# Example 2: Agent using send_message_to_user through tools
print("\nExample 2: Agent using send_message_to_user through tools")
agent_with_message = ChatAgent(
    system_message="You are an assistant that can send messages to the user.",
    model=model,
    tools=[*human_toolkit.get_tools()],
)

response = agent_with_message.step(
    "Send me a notification about an upcoming meeting."
)

print(response.msgs[0].content)

"""
==========================================================================
Agent Message:
🔔 Reminder: You have an upcoming meeting scheduled. Please check your 
calendar for details!

I've sent you a notification about your upcoming meeting. Please check your 
calendar for details!
==========================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\image_analysis_toolkit.py
--------------------------------------------------------------------------------

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
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.toolkits import ImageAnalysisToolkit
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
)

image_analysis_toolkit = ImageAnalysisToolkit(model=model)

agent = ChatAgent(
    system_message="You are a helpful assistant.",
    model=model,
    tools=[*image_analysis_toolkit.get_tools()],
)


user_msg = BaseMessage.make_user_message(
    role_name="User",
    content='''
        The image link is: https://upload.wikimedia.org/wikipedia/commons/
        thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/
        2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg
        What's in this image? You must use image analysis to help me.
        ''',
)
response = agent.step(user_msg)
print(response.msgs[0].content)
""""
===========================================================================
The image depicts a serene landscape featuring a wooden boardwalk that leads 
through a lush, green marsh or meadow. The boardwalk is centrally positioned, 
extending into the distance and inviting viewers to imagine walking along it. 
On either side of the boardwalk, tall grass and various vegetation create a 
vibrant green expanse.

In the background, there are clusters of trees and shrubs, adding depth to the 
scene. The sky above is mostly clear with a few scattered clouds, showcasing a 
gradient of blue hues. The overall atmosphere is tranquil and natural, 
suggesting a peaceful outdoor setting, with soft lighting that likely 
indicates early morning or late afternoon."
============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\mcp\mcp_toolkit.py
--------------------------------------------------------------------------------

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
"""MCP Server Example

This example demonstrates how to use the MCP (Managed Code Processing) server
with CAMEL agents for file operations.

Setup:
1. Install Node.js and npm

2. Install MCP filesystem server globally:
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   ```

Usage:
1. Run this script to start an MCP filesystem server
2. The server will only operate within the specified directory
3. All paths in responses will be relative to maintain privacy
"""

import asyncio
from pathlib import Path

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.toolkits import MCPToolkit
from camel.types import ModelPlatformType, ModelType


async def main():
    config_path = Path(__file__).parent / "mcp_servers_config.json"
    mcp_toolkit = MCPToolkit(config_path=str(config_path))

    # Connect to all MCP servers.
    await mcp_toolkit.connect()

    sys_msg = "You are a helpful assistant"
    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )
    camel_agent = ChatAgent(
        system_message=sys_msg,
        model=model,
        tools=[*mcp_toolkit.get_tools()],
    )
    user_msg = "List 5 files in the project, using relative paths"
    response = await camel_agent.astep(user_msg)
    print(response.msgs[0].content)
    print(response.info['tool_calls'])

    # Disconnect from all MCP servers and clean up resources.
    await mcp_toolkit.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
'''
===============================================================================
Here are 5 files in the project using relative paths:

1. `.env`
2. `.gitignore`
3. `.pre-commit-config.yaml`
4. `CONTRIBUTING.md`
5. `README.md`
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\memory_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits.memory_toolkit import MemoryToolkit
from camel.types import ModelPlatformType, ModelType


def run_memory_toolkit_example():
    """
    Demonstrates a ChatAgent using the MemoryToolkit for
    function calling to manage memory.
    """

    # Create a Model
    model_config_dict = ChatGPTConfig(temperature=0.0).as_dict()
    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
        model_config_dict=model_config_dict,
    )

    # Create a ChatAgent
    agent = ChatAgent(
        system_message="""You are an assistant that can manage 
        conversation memory using tools.""",
        model=model,
    )

    # Add MemoryToolkit to the Agent
    memory_toolkit = MemoryToolkit(agent=agent)
    for tool in memory_toolkit.get_tools():
        agent.add_tool(tool)

    # Have a conversation to populate memory
    print("\n--- Starting a Conversation ---")
    user_msg_1 = "Tell me about the moon."
    print(f"[User] {user_msg_1}")
    response_1 = agent.step(user_msg_1)
    print(f"[Agent] {response_1.msgs[0].content}")

    # Save the memory to a file via function calling
    print("\n--- Saving Memory ---")
    save_msg = "Please save the current memory to 'conversation_memory.json'."
    response_save = agent.step(save_msg)
    print(f"[Agent] {response_save.msgs[0].content}")
    print(f"[Tool Call Info] {response_save.info['tool_calls']}")

    # Clear the memory via function calling
    print("\n--- Clearing Memory ---")
    clear_msg = "Please clear the memory."
    response_clear = agent.step(clear_msg)
    print(f"[Agent] {response_clear.msgs[0].content}")
    print(f"[Tool Call Info] {response_clear.info['tool_calls']}")

    # Verify memory is cleared
    print("\n--- Checking Memory After Clear ---")
    check_msg = "What do you remember about the moon?"
    response_check = agent.step(check_msg)
    print(f"[Agent] {response_check.msgs[0].content}")

    # Load memory from the saved file via function calling
    print("\n--- Loading Memory from File ---")
    load_msg = "Please load the memory from 'conversation_memory.json'."
    response_load = agent.step(load_msg)
    print(f"[Agent] {response_load.msgs[0].content}")
    print(f"[Tool Call Info] {response_load.info['tool_calls']}")

    # Verify memory is restored
    print("\n--- Checking Memory After Load ---")
    check_msg = "What do you remember about the moon?"
    response_restored = agent.step(check_msg)
    print(f"[Agent] {response_restored.msgs[0].content}")


if __name__ == "__main__":
    run_memory_toolkit_example()



--------------------------------------------------------------------------------
# File: toolkits\meshy_toolkit.py
--------------------------------------------------------------------------------

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
from camel.toolkits import MeshyToolkit

toolkit = MeshyToolkit()

# Example data for testing
prompt = "A figuring of Tin tin the cartoon character"
art_style = "realistic"
negative_prompt = "low quality, low resolution, low poly, ugly"

# 3D model generation
print("Starting 3D model generation...")
final_response = toolkit.generate_3d_model_complete(
    prompt=prompt, art_style=art_style, negative_prompt=negative_prompt
)
print("\nFinal Response:", final_response)
# ruff: noqa: E501
"""
==========================================================================
Starting 3D model generation...
Status after 0s: PENDING
Status after 11s: IN_PROGRESS
Status after 22s: IN_PROGRESS
Status after 32s: SUCCEEDED
Status after 0s: PENDING
Status after 11s: IN_PROGRESS
Status after 21s: IN_PROGRESS
Status after 32s: IN_PROGRESS
Status after 43s: IN_PROGRESS
Status after 53s: IN_PROGRESS
Status after 64s: IN_PROGRESS
Status after 74s: IN_PROGRESS
Status after 85s: IN_PROGRESS
Status after 95s: IN_PROGRESS
Status after 106s: IN_PROGRESS
Status after 117s: SUCCEEDED

Final Response: {'id': '01939144-7dea-73c7-af06-efa79c83243f', 'mode': 
'refine', 'name': '', 'seed': 1733308970, 'art_style': 'realistic', 
'texture_richness': 'high', 'prompt': 'A figuring of Tin tin the cartoon 
character', 'negative_prompt': 'low quality, low resolution, low poly, ugly', 
'status': 'SUCCEEDED', 'created_at': 1733309005313, 'progress': 100, 
'started_at': 1733309006267, 'finished_at': 1733309113474, 'task_error': None, 
'model_urls': {'glb': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/model.glb?Expires=4886870400&Signature=TEbWpN8sFZOf1FKWBVxKNdT2Ltm1Ma6vHuUUpBh6rZaAzfTBQPKvV2i7RmD~wwaebbQSBvVVagF4j587tNKNwHPqkGtpBjBu2q43n4lWM6W--RxSqbOCvVZ54PiAzzlVjM9PzPz-MasrWQtYipm5qJ5tsWd7XoxB6Wv2tZMZEWsftdLxmXdp9SuoBcu5NM~MRnyvhEYPmwU9uCAKfh4FZ14mhfx6TeDpCprYh1ngnlkLzDXk5Mdw0HJ1zuYpnkCOUtth84p6Oq5aU0HtWtUVd2tLi53rqKn9QC0qxcH7QlPxxI1aoUtzqaMXXiqCGylzZuPTZILhdFWeAoiEtCOLZw__&Key-Pair-Id=KL5I0C8H7HX83', 'fbx': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/model.fbx?Expires=4886870400&Signature=jGOPhF8FL1wa9mVbodNoq1jMVzi2gklWRrrl2qWAZvWAhadc4wgjmgTweBKsNiO~KMTGzCiey7iqSIGm6dDEYAMv72HExpIO7I8HwAVPp4KwhzORzwr6OcEoY9-7fFR9yEg~WqnWewmdkrcnUVHHx2Z9imkDkIhISn1IOERkum48mTemlyejb87CXGV14uX3hxIVKle4at6S8tMUfpXhCdZ3aIxmgt9Dpsobol92XtQbpC-JhJSOgMNBWtAH3OUXAgECsYrRRZND9gcZZkUZlXHHZt439JsU8MPoXZd4RQ0OGn~vb6W51rvQ904ErsYZf47dLYNswaxb6Se3oKm~zw__&Key-Pair-Id=KL5I0C8H7HX83', 'usdz': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/model.usdz?Expires=4886870400&Signature=ICOOIH6EDVdy9LYCk-azYqBWtl6t9v2xZpRk8C8kQKa38jUXdukjoLLN469VP5a7rdIKinLA~I5-hMr-kd-MEmwJzE3JKw2ojNimYPa5Uvnr3R~4S~2fQgCPWfn2xVkt6Cvfx~Qj8~ZNVxMj0jvnKkIySRHYaqvCxMfASHCB7Kz9LN3lBWuT709pEnQ6mtwLJWybLlIJkMFOVoapw~epIgWBtJjhMNwPCzXswUddKSdirOHIm8JRoN3~Ha99oxo4nSN5tyf3u2fWLxGOTeAyp7Hcq97gMkdqjuNc14k2n7fPULgbSCkHepLIG8GQrNLMfA6hkphkIj0LdjC6AQ7pvg__&Key-Pair-Id=KL5I0C8H7HX83', 'obj': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/model.obj?Expires=4886870400&Signature=a53mEQASL7jRU8Xz5WhN-~d3~74BlBlqDMufryX-j1~jXTgbMEEhY2dC5R7dHHHJbJ4ns9GQ8cbjxcCImVvjkiLvPYZ-lraLaqMnbG~hatsZNv6wDZxTson8jsiqTSHaLnamp83zycLotM~zrUW0DIHGoFWvf9DPTKqy4Z0ZAOxOsA9qfAmJI6k2CVHLu0hMRLAjm3f8KA4j90kJBBVuYvABZi27hP-aURhD09zoAMp~AsrXSKxFjd5wcYqKko78qch2K2H5NaAUGhsKbuNmBMFaxc0C5dKgSlKufWmib86vUOe1dYLQyqGTS85u5dVQSwFrDY5gyugGJ4TH-aVQVw__&Key-Pair-Id=KL5I0C8H7HX83', 'mtl': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/model.mtl?Expires=4886870400&Signature=FnY3cNMqEymvBw~33riU~HkVIifWKEUh0ndV90VaWMnKczU~Wqng7AYTqwywr6PNQDuFL~iQFw-y6qvklsV9I0aTg8OoYQ3dfCaRqydwUbN80aonk~fwpAJUwBxqbhhN4n9T~7WTX-pyo0w5vQ09wte4G-4yAIUEM7qlOwZohdfK2a~EIhnq9WiV92TuGtm0c4x5n6png9ZjX5pHnp~a77UCBJlIQ1teN5Rb3I9HFh4sbUGdcXUas7B9EIq4YiabjO9vf5FGwicb2XQ-YxJFJJdEJwbBp6l6iZCbSk-WijmIWmyD~8A~jhTNwlG9UHR5qTsnprntgoRyLdTRSXvDzg__&Key-Pair-Id=KL5I0C8H7HX83'}, 
'thumbnail_url': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/preview.png?Expires=4886870400&Signature=B16evi199mig4RTFq0FVPrHGkpjpPudRpLfpcY2FxJIkIFYg42-v8BfsL3eWAM-XDlDqahPSXtqqm6emVkSu550iPqo2yy-URoDifiIl5petEy~42nHtc1-dZB1HcEvtcyycHOjmk1y8zQfZBgQ8cjGq0Ds19xSdOXIo7-~QDPWhUGUTreJvBNg17GitgvcfYbGj2g6gibYJWjwatM7A6yHhq3d53N8eDcmO5L6dBH3VwUFTxDWBQXwUT7aXkS7dsQ7Wz5CkIbbH~T-4Pn5KpdJy1Kf1Lrh1YpOUN4T7JI8Ot5urYKYRj4cZ96xpDD9gicPGvgrRaicFyb1sSwW2ow__&Key-Pair-Id=KL5I0C8H7HX83', 
'video_url': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/output.mp4?Expires=4886870400&Signature=r8t11N9~XGzNfuW3KowxarSpr7hC8eQb0kzkKADOz3hdTA9vAqBdv5AVdMGDlMmH9IP4R60UCnVNT6scA1EeN3FZLXaHaWbsxHDuc4XdUk7DE7AbwUKSbl~YdUSu5-RkNu6vaMHTiB55XubUJhv9ReB25a6Ifee0rf1ulGs-amFSMlL~eNPq6HTUI6NGAqi1p~VeFzE53JV5sWvU2JYnbGe8kzruC705z1LiCU-9isWzJGuOIy~RpiVfYzSmgh4xeILaYKpxR2ZM2uVtbi6snl~aYsqiKMIIMxMg-aZDWn-f5voiWaCL1OUV5fxbI82ZRJNd5DSlVjI~umqZZIl-iw__&Key-Pair-Id=KL5I0C8H7HX83', 
'texture_urls': [{'base_color': 'https://assets.meshy.ai/5e05026a-0e91-4073-83fe-0263b1b4d348/tasks/01939144-7dea-73c7-af06-efa79c83243f/output/texture_0.png?Expires=4886870400&Signature=Q8SGRrnE00-mGHCAcIOUUAig~YtTJqVx1n2IqFFbXBNUPvf~hsTYzcKgC2wQjF25tj0D6yQ8BiIktN9WjsKu0SnbeED~ofHIA0quheMjwHL~hfdj63LGWkMumVEjE2ZVwDv-DdlROF3ayw5hQxzlRbcHwXLq0n2xMHmj-WetyiYBKCcJbXbZMOAtlo8e40d21CGMnjImduCvdwhpqwNKUx4MwHeM2W0GW4OC94AoSF8AccHJeQPD2gdu7JHoTuZFjcqS-9YCjmHT7Y5Xg7rmeNYz40O21sYci0b54NvBDzX-6HvydjqtY-ofudppaxlC77Zd~FaVcCz5rH2J43cdLg__&Key-Pair-Id=KL5I0C8H7HX83'}]}
(camel-ai-py3.12) 
==========================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\mineru_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import MinerUToolkit
from camel.types import ModelPlatformType, ModelType


def main():
    # Initialize the toolkit
    mineru_toolkit = MinerUToolkit()

    print("Example 1: Extracting content from a single URL...")
    try:
        # Extract and wait for results
        result = mineru_toolkit.extract_from_urls(
            urls="https://arxiv.org/pdf/2311.10993.pdf"
        )
        print("\nExtraction completed successfully:")
        print(f"Download URL: {result['full_zip_url']}\n")

    except Exception as e:
        print(f"Extraction failed: {e}\n")

    print("Example 2: Extracting content from multiple URLs...")
    try:
        urls = [
            "https://arxiv.org/pdf/2311.10993.pdf",
            "https://arxiv.org/pdf/2310.07298.pdf",
        ]

        # Batch extract and wait for results
        results = mineru_toolkit.extract_from_urls(urls=urls)

        print("\nBatch extraction completed successfully:")
        for result in results['extract_result']:
            print(f"\nDocument: {result['file_name']}")
            print(f"Download URL: {result['full_zip_url']}")

    except Exception as e:
        print(f"Batch extraction failed: {e}\n")

    print("\nExample 3: Using MinerU with ChatAgent...")
    # TODO: implement this example with loader toolkit to get information from
    # the zip url
    try:
        # Set up the ChatAgent with MinerU capabilities
        sys_msg = (
            "You are a helpful assistant that can extract and analyze "
            "content from documents using MinerU's document extraction. "
            "You can handle PDFs and extract text, formulas, and tables. When "
            "processing documents, inform users that it may take time."
        )

        # Initialize the model with specific configuration
        model = ModelFactory.create(
            model_platform=ModelPlatformType.DEFAULT,
            model_type=ModelType.DEFAULT,
            model_config_dict=ChatGPTConfig(temperature=0.0).as_dict(),
        )

        # Create the agent with MinerU toolkit
        agent = ChatAgent(
            system_message=sys_msg,
            model=model,
            tools=mineru_toolkit.get_tools(),
        )

        # Example document analysis request
        usr_msg = (
            "Please extract and analyze this research paper,"
            "focusing on mathematical formulas and tables: "
            "https://arxiv.org/pdf/2311.10993.pdf "
        )

        response = agent.step(usr_msg)
        print("\nAgent Response:")
        print(response.msg.content)

    except Exception as e:
        print(f"\nAgent interaction failed: {e}\n")


if __name__ == "__main__":
    main()

"""
Example output:

Example 1: Extracting content from a single URL...

Extraction completed successfully:
Download URL: https://cdn-mineru.openxlab.org.cn/pdf/690a7956-eaaa-4fb2-ad7d-6056d1d4e316.zip

Example 2: Extracting content from multiple URLs...

Batch extraction completed successfully:

Document: 2311.10993.pdf
Download URL: https://cdn-mineru.openxlab.org.cn/pdf/690a7956-eaaa-4fb2-ad7d-6056d1d4e316.zip

Document: 2310.07298.pdf
Download URL: https://cdn-mineru.openxlab.org.cn/pdf/250a3762-406e-4279-aa80-47e5ea934509.zip

Example 3: Using MinerU with ChatAgent...

Agent Response:
The extraction of the research paper has been completed. You can download the
extracted content, including mathematical formulas and tables,
from the following link:

[Download Extracted Content]
(https://cdn-mineru.openxlab.org.cn/pdf/690a7956-eaaa-4fb2-ad7d-6056d1d4e316.zip)

If you need any specific analysis or further assistance with the content,
please let me know!

"""



--------------------------------------------------------------------------------
# File: toolkits\networkx_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import NetworkXToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = "You are a helpful assistant for graph analysis"

# Set model config and initialize toolkit
tools = NetworkXToolkit(graph_type='digraph').get_tools()
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)

# Example: Create a directed graph and perform some analysis
usr_msg = """Create a directed graph with the following edges:
- A -> B (weight: 2)
- B -> C (weight: 3)
- C -> A (weight: 1)
Then find the shortest path from A to C and calculate the graph density."""

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls']))

'''
===============================================================================
[ToolCallingRecord(tool_name='add_edge', args={'source': 'A', 'target': 'B'}, 
result=None, tool_call_id='call_iewKMXQd2GKwKWy7XJ5e5d8e'), ToolCallingRecord
(tool_name='add_edge', args={'source': 'A', 'target': 'B'}, result=None, 
tool_call_id='call_Xn8wq22oKeKekuPEqcSj5HuJ'), ToolCallingRecord
(tool_name='add_edge', args={'source': 'B', 'target': 'C'}, result=None, 
tool_call_id='call_bPeCvUBk1iQ6vv5060Zd7nbi'), ToolCallingRecord
(tool_name='add_edge', args={'source': 'C', 'target': 'A'}, result=None, 
tool_call_id='call_inCnY60iSBVghsrrHEDh7hNw'), ToolCallingRecord
(tool_name='get_shortest_path', args={'source': 'A', 'target': 'C', 'weight': 
'weight', 'method': 'dijkstra'}, result=['A', 'B', 'C'], 
tool_call_id='call_Gwy3Ca8RDQCZFuiy2h0Z6SSF'), ToolCallingRecord
(tool_name='get_edges', args={}, result=[('A', 'B'), ('B', 'C'), ('C', 'A')], 
tool_call_id='call_LU2xhb2W4h5a6LOx4U8gLuxa'), ToolCallingRecord
(tool_name='get_nodes', args={}, result=['A', 'B', 'C'], 
tool_call_id='call_WLuB1nBrhFeGj4FKrbwfnCrG')]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\notion_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import NotionToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = "You are a helpful assistant"

# Set model config
tools = NotionToolkit().get_tools()
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message
usr_msg = "Lists all pages in the Notion workspace"

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
==========================================================================
[ToolCallingRecord(func_name='list_all_pages', args={}, result=[{'id': 
'12684f56-4caa-8080-be91-d7fb1a5834e3', 'title': 'test page'}, 
{'id': '47a4fb54-e34b-4b45-9928-aa2802982eb8', 'title': 'Aigentbot'}])]
"""

usr_msg = "Retrieves the text content of a Notion block which id is"
"'12684f56-4caa-8080-be91-d7fb1a5834e3'"

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
==========================================================================
[ToolCallingRecord(func_name='get_notion_block_text_content', args=
{'block_id': '12684f56-4caa-8080-be91-d7fb1a5834e3'}, result='hellonihao 
buhao this is a test par [Needs case added] another par [Needs case added]
A cute cat: https://www.google.com/imgres?q=cat&imgurl=https%3A%2F%2Fi.
natgeofe.com%2Fn%2F548467d8-c5f1-4551-9f58-6817a8d2c45e%2FNationalGeographic
_2572187_square.jpg&imgrefurl=https%3A%2F%2Fwww.nationalgeographic.com%2F
animals%2Fmammals%2Ffacts%2Fdomestic-cat&docid=K6Qd9XWnQFQCoM&tbnid=eAP24
4UcF5wdYM&vet=12ahUKEwir9rf3oKGJAxVsFTQIHYsrMYkQM3oECBkQAA..i&w=3072&h=307
2&hcb=2&ved=2ahUKEwir9rf3oKGJAxVsFTQIHYsrMYkQM3oECBkQAA')]
"""

usr_msg = "List names of users via the Notion integration"

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
==========================================================================
[ToolCallingRecord(func_name='list_all_users', args={}, result=[{'type':
'person', 'name': 'user a', 'workspace': ''}, {'type': 'bot', 'name':
'test', 'workspace': "user a's Notion"}])]
==========================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\openai_agent_toolkit_example.py
--------------------------------------------------------------------------------

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

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import OpenAIAgentToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = """You are a helpful AI assistant that can use OpenAI's agent tools 
including web search and file search."""

# Set model config
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=model_config_dict,
)

# Initialize toolkit and get tools
toolkit = OpenAIAgentToolkit(model=model)
tools = toolkit.get_tools()

# Set agent
agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)

# Example 1: Web Search
print("\n=== Using Web Search with Agent ===")
response = agent.step(
    "What was a positive news story from today? Use web search to find out."
)
print("Web Search Response:", response.msg.content)

# Example 2: Direct Web Search
print("\n=== Direct Web Search Usage ===")
web_result = toolkit.web_search(
    "What are the latest developments in renewable energy?"
)
print("Direct Web Search Result:", web_result)

# Example 3: File Search (if configured)
vector_store_id = os.getenv("OPENAI_VECTOR_STORE_ID")

if vector_store_id:
    print("\n=== Using File Search with Agent ===")
    response = agent.step(
        f"Search through my documents for information about climate change. "
        f"Use file search with vector store ID: {vector_store_id}"
    )
    print("File Search Response:", response.msg.content)

    print("\n=== Direct File Search Usage ===")
    file_result = toolkit.file_search(
        query="What are the key points about climate change?",
        vector_store_id=vector_store_id,
    )
    print("Direct File Search Result:", file_result)
else:
    print("\n=== File Search Examples Skipped ===")
    print("Set OPENAI_VECTOR_STORE_ID env var to run file search examples")


"""
=== Using Web Search with Agent ===
Web Search Response: Here are some uplifting news stories from today:

1. **Historic Marriage Milestone**: A Brazilian couple has set a new Guinness
World Record for the longest marriage of a living couple, celebrating 84 
years and 85 days together.

2. **Lottery Jackpot Win**: A Michigan man who consistently played the same 
lottery numbers for four years has won a $1.3 million jackpot in the state's 
Lotto 47 game.

3. **Miraculous Recovery**: A 23-year-old British woman, initially given only 
a 5% chance of survival after a life-threatening skiing accident, shared her 
inspiring story of recovery.

4. **Marathon for a Cause**: A Wisconsin doctor, who previously battled 
testicular cancer, ran seven marathons on seven continents—from 
Antarctica to North America—to raise awareness for the disease.

5. **Kindness in the Skies**: An airline passenger shared a story about 
a fellow flyer who offered $100 to switch their window seat for an aisle
seat, highlighting unexpected acts of kindness.

6. **Community Support**: A North Carolina mother is honoring the victims of 
an American Airlines flight that collided with an Army helicopter by 
supporting the skating community, demonstrating resilience and unity.

7. **Positive Outlook During Pandemic**: A study from Oregon State University 
confirms that individuals with positive and playful attitudes navigated the 
COVID-19 pandemic more effectively, underscoring the power of optimism.

8. **Random Act of Kindness**: An emergency room doctor and father of three in 
Fort Worth, Texas, was touched when a stranger left a heartfelt note and paid 
his family's breakfast bill at a local café.

9. **Mountain Rescue**: Two experienced hikers were rescued from the tallest 
mountain in the Northeast after a whiteout snowstorm stranded them at about 
5,000 feet, showcasing the dedication of rescue teams.

10. **Pilot's Reassurance**: An American Airlines pilot went viral after 
assuring passengers that he has "no higher calling" than "carefully" 
transporting them to their destination, following a recent tragic 
crash in D.C.

These stories highlight the resilience, kindness, and positive spirit 
present in our communities.

=== Direct Web Search Usage ===
Direct Web Search Result: Recent developments in renewable energy have marked 
significant progress across various sectors:

**Record Growth in Renewable Energy Capacity**

In 2023, the global renewable energy sector experienced unprecedented growth, 
adding 473 gigawatts (GW) new capacity—a 54% increase from the previous year. 
This surge was predominantly driven by solar photovoltaic and onshore wind 
installations, which together accounted for over 95% of the new capacity. 
Notably, solar PV alone contributed 346 GW, reflecting a 73% year-on-year 
increase. China played a pivotal role in this expansion, leading in solar PV, 
onshore wind, offshore wind, and hydropower installations. This dominance has 
contributed to a decline in the global weighted average cost of electricity 
(LCOE) for these technologies, making renewable power generation increasingly 
competitive. ([greenearth.news](https://greenearth.news/record-growth-in-
renewable-energy-473-gw-added-in-2023-marks-a-turning-point-in-global-power-
transition-report/?utm_source=openai))

**Advancements in Energy Storage Technologies**

The integration of renewable energy sources has been bolstered by significant 
advancements in energy storage solutions. In 2023, battery storage capacity 
expanded dramatically, with 95.9 GWh added, up from just 0.1 GWh in 2010. This 
growth has been accompanied by substantial reduction in costs, with price of 
battery storage projects decreasing by 89% between 2010 and 2023. These 
developments enhance reliability and scalability of renewable energy systems, 
addressing the intermittent nature of sources like wind and solar. 
([greenearth.news](https://greenearth.news/record-growth-in-renewable-energy-
473-gw-added-in-2023-marks-a-turning-point-in-global-power-transition-report/?
utm_source=openai))

**Innovations in Renewable Energy Technologies**

The renewable energy sector has witnessed several technological breakthroughs:

- **Solar Power**: The introduction of high-efficiency solar panels utilizing 
materials such as perovskite and gallium arsenide has significantly increased 
energy conversion rates. Additionally, building-integrated photovoltaics
are enabling the seamless integration of solar technology into architectural 
designs, transforming buildings into self-sustaining power generators. 
([toxigon.com](https://toxigon.com/renewable-energy-technologies-2023?
utm_source=openai))

- **Wind Energy**: Advancements in wind turbine technology, including the 
deployment of larger and more efficient turbines, have enhanced energy capture 
Offshore wind farms, particularly those utilizing floating wind turbines, are 
expanding the potential for wind power generation in deeper waters previously 
inaccessible to traditional fixed-bottom turbines. ([toxigon.com]
(https://toxigon.com/renewable-energy-technologies-2023?utm_source=openai))

- **Energy Storage**: Innovations in battery technology, such as development 
of advanced lithium-ion, solid-state batteries, have improved energy density, 
charging times, and safety features. These advancements facilitate the 
integration of renewable energy into the power grid and support transition to 
a low-carbon economy. ([toxigon.com](https://toxigon.com/renewable-energy-
technologies-2023?utm_source=openai))

**Global Investment and Policy Support**

The clean energy transition is gaining momentum, with substantial investments 
and policy support driving the shift towards renewable energy:

- The International Energy Agency (IEA) projects that $2 trillion will be 
allocated to clean energy in 2024, with 85% of new power plants being 
renewable. 
([time.com](https://time.com/7022326/climate-leadership-forum-green-economy-
clean-energy-transition/?utm_source=openai))

- China's dominance in green technology manufacturing, including turbines, 
solar panels, electric vehicles, and lithium-ion batteries, positions it as a 
leader in the global renewable energy market. This leadership is expected to 
continue, with China projected to install 60% of world's renewable capacity 
between now and 2030. ([ft.com](https://www.ft.com/content/d3650b44-0313-44c9-
a7aa-495549b158b5?utm_source=openai))

These developments underscore the rapid advancements in renewable energy, 
driven by technological innovation, substantial investments, and supportive 
policies, collectively contributing to a more sustainable and resilient 
global energy landscape.


## Recent Developments in Renewable Energy:
- [Record renewables growth fuels cost competitiveness -IRENA report shows]
(https://www.reuters.com/business/energy/record-renewables-growth-fuels-cost-
competitiveness-irena-report-shows-2024-09-24/?utm_source=openai)
- [Cheap Solar Panels Are Changing the World](https://www.theatlantic.com/science/
archive/2024/10/solar-power-energy-revolution-global-south/680351/?
utm_source=openai)
- [China is winning the race for green supremacy](https://www.ft.com/content/
d3650b44-0313-44c9-a7aa-495549b158b5?utm_source=openai) 

=== Using File Search with Agent ===
File Search Response: It appears that there are no mentions of "climate 
change" in the documents you've uploaded. If you need info or insights on
that topic, please let me know how I can assist you further!

=== Direct File Search Usage ===
Direct File Search Result: It looks like there were no relevant results in the 
uploaded files regarding climate change. However, I can provide summary of key
points about climate change:

1. **Definition**: Climate change refers to significant changes in global 
temperatures and weather patterns over time.

2. **Causes**:
- **Greenhouse Gas Emissions**: Increased levels of carbon dioxide (CO2), 
methane (CH4), and nitrous oxide (N2O) from human activities (e.g., burning 
fossil fuels, deforestation).
- **Natural Factors**: Volcanic eruptions, solar radiation variations, and 
natural greenhouse gas emissions.

3. **Impacts**:
- **Temperature Increases**: Global average temperatures have risen, leading 
to heatwaves and extreme weather.
- **Sea Level Rise**: Melting ice caps and glaciers contribute to rising sea 
levels, which can lead to coastal flooding.
- **Ecosystem Disruption**: Affects biodiversity, leading to habitat loss, 
changes in species distribution, and increased extinction rates.

4. **Social and Economic Consequences**:
- **Food and Water Security**: Impact on agricultural productivity and water 
availability.
- **Health Risks**: Increased prevalence of heat-related illnesses and spread 
of diseases.
- **Economic Costs**: Damage to infrastructure, increased disaster recovery 
costs, and shifts in market dynamics.

5. **Mitigation Strategies**:
- **Renewable Energy Sources**: Transition to solar, wind, and other renewable 
energy resources.
- **Energy Efficiency**: Improving energy use in buildings, transportation, 
and industry.
- **Conservation Practices**: Protecting forests, wetlands, and other 
ecosystems that sequester carbon.

6. **International Agreements**: Efforts like the Paris Agreement aim to unite 
countries to limit global warming to well below 2 degrees Celsius above pre-
industrial levels.

If you need more specific information or details from the files, 
feel free to ask!
"""



--------------------------------------------------------------------------------
# File: toolkits\openapi_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import OpenAPIToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = "You are a helpful assistant"

# Set model config
tools = OpenAPIToolkit().get_tools()
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message
usr_msg = "help me to select a basketball in klarna."

# Get response information
response = camel_agent.step(usr_msg)
print(response.info['tool_calls'])
"""
===============================================================================
[ToolCallingRecord(func_name='klarna_productsUsingGET', args={
'q_in_query': 'basketball'}, result={'products': [{'name': 'Wilson Evolution'
, 'url': 'https://www.klarna.com/us/shopping/pl/cl1220/3203801266/Basketball
/Wilson-Evolution/?utm_source=openai&ref-site=openai_plugin', 'price':
'$65.00', 'attributes': ['Color:Brown,Blue,Black,Orange', 'Ball Size:6,7',
'Area of Use:Indoors,Outdoors', 'Material:Leather,Rubber']}, {'name':
'Wilson NBA Authentic', 'url': 'https://www.klarna.com/us/shopping/pl/cl1220/
3200358202/Basketball/Wilson-NBA-Authentic/?utm_source=openai&ref-site=openai
_plugin', 'price': '$24.99', 'attributes': ['Color:Orange', 'Ball Size:6,7',
'Area of Use: Indoors,Outdoors', 'Material:Leather']},]})]
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\openbb_toolkit.py
--------------------------------------------------------------------------------

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
from camel.toolkits import OpenBBToolkit

# Initialize OpenBB toolkit with proper credentials
toolkit = OpenBBToolkit()

# Example 1: Stock quotes for multiple companies
print("\nExample 1: Stock quotes for multiple companies")
companies = ["AAPL", "MSFT", "GOOGL"]
for symbol in companies:
    res_quote = toolkit.get_stock_quote(symbol=symbol)
    print(f"\n{symbol} Stock Quote:")
    print(res_quote)
"""
===============================================================================
AAPL Stock Quote:
[YFinanceEquityQuoteData(symbol=AAPL, asset_type=EQUITY, name=Apple Inc.,
exchange=NMS, bid=249.26, bid_size=5000, bid_exchange=None, ask=250.02,
ask_size=400, ask_exchange=None, quote_conditions=None, quote_indicators=None,
sales_conditions=None, sequence_number=None, market_center=None,
participant_timestamp=None, trf_timestamp=None, sip_timestamp=None,
last_price=249.79, last_tick=None, last_size=None, last_timestamp=None,
open=247.46, high=251.85, low=247.0949, close=None, volume=58911560,
exchange_volume=None, prev_close=248.05, change=None, change_percent=None,
year_high=254.28, year_low=164.08, ma_50d=234.3126, ma_200d=210.4949,
volume_average=42989052.0, volume_average_10d=44930240.0, currency=USD)]

MSFT Stock Quote:
[YFinanceEquityQuoteData(symbol=MSFT, asset_type=EQUITY,
name=Microsoft Corporation, exchange=NMS, bid=418.95, bid_size=100,
bid_exchange=None, ask=437.26, ask_size=100, ask_exchange=None,
quote_conditions=None, quote_indicators=None, sales_conditions=None,
sequence_number=None, market_center=None, participant_timestamp=None,
trf_timestamp=None, sip_timestamp=None, last_price=437.03, last_tick=None,
last_size=None, last_timestamp=None, open=441.62, high=443.1834, low=436.33,
close=None, volume=21207330, exchange_volume=None, prev_close=437.39,
change=None, change_percent=None, year_high=468.35, year_low=366.5,
ma_50d=426.4474, ma_200d=424.4953, volume_average=20174949.0,
volume_average_10d=21000220.0, currency=USD)]

GOOGL Stock Quote:
[YFinanceEquityQuoteData(symbol=GOOGL, asset_type=EQUITY, name=Alphabet Inc.,
exchange=NMS, bid=188.33, bid_size=300, bid_exchange=None, ask=188.56,
ask_size=200, ask_exchange=None, quote_conditions=None, quote_indicators=None,
sales_conditions=None, sequence_number=None, market_center=None,
participant_timestamp=None, trf_timestamp=None, sip_timestamp=None,
last_price=188.51, last_tick=None, last_size=None, last_timestamp=None,
open=191.625, high=193.03, low=188.38, close=None, volume=31130881,
exchange_volume=None, prev_close=188.4, change=None, change_percent=None,
year_high=201.42, year_low=130.67, ma_50d=173.84, ma_200d=167.58334,
volume_average=27155819.0, volume_average_10d=38432110.0, currency=USD)]
===============================================================================
"""

# Example 2: Historical data for Apple stock
print("\nExample 2: Historical data for Apple stock")
res_hist = toolkit.get_historical_data(
    symbol="AAPL",
    start_date="2023-12-01",
    end_date="2023-12-31",
    interval="1d",
)
print("\nRecent Historical Data for AAPL:")
print(res_hist)
"""
===============================================================================
Recent Historical Data for AAPL:
{'results': [YFinanceEquityHistoricalData(date=2023-12-01,
open=190.3300018310547, high=191.55999755859375, low=189.22999572753906,
close=191.24000549316406, volume=45679300, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-04,
open=189.97999572753906, high=190.0500030517578, low=187.4499969482422,
close=189.42999267578125, volume=43389500, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-05,
open=190.2100067138672, high=194.39999389648438, low=190.17999267578125,
close=193.4199981689453, volume=66628400, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-06,
open=194.4499969482422, high=194.75999450683594, low=192.11000061035156,
close=192.32000732421875, volume=41089700, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-07,
open=193.6300048828125, high=195.0, low=193.58999633789062,
close=194.27000427246094, volume=47477700, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-08,
open=194.1999969482422, high=195.99000549316406, low=193.6699981689453,
close=195.7100067138672, volume=53377300, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-11,
open=193.11000061035156, high=193.49000549316406, low=191.4199981689453,
close=193.17999267578125, volume=60943700, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-12,
open=193.0800018310547, high=194.72000122070312, low=191.72000122070312,
close=194.7100067138672, volume=52696900, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-13,
open=195.08999633789062, high=198.0, low=194.85000610351562,
close=197.9600067138672, volume=70404200, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-14,
open=198.02000427246094, high=199.6199951171875, low=196.16000366210938,
close=198.11000061035156, volume=66831600, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-15,
open=197.52999877929688, high=198.39999389648438, low=197.0,
close=197.57000732421875, volume=128256700, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-18,
open=196.08999633789062, high=196.6300048828125, low=194.38999938964844,
close=195.88999938964844, volume=55751900, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-19,
open=196.16000366210938, high=196.9499969482422, low=195.88999938964844,
close=196.94000244140625, volume=40714100, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-20,
open=196.89999389648438, high=197.67999267578125, low=194.8300018310547,
close=194.8300018310547, volume=52242800, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-21,
open=196.10000610351562, high=197.0800018310547, low=193.5,
close=194.67999267578125, volume=46482500, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-22,
open=195.17999267578125, high=195.41000366210938, low=192.97000122070312,
close=193.60000610351562, volume=37122800, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-26,
open=193.61000061035156, high=193.88999938964844, low=192.8300018310547,
close=193.0500030517578, volume=28919300, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-27,
open=192.49000549316406, high=193.5, low=191.08999633789062,
close=193.14999389648438, volume=48087700, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-28,
open=194.13999938964844, high=194.66000366210938, low=193.1699981689453,
close=193.5800018310547, volume=34049900, vwap=None, split_ratio=None,
dividend=None), YFinanceEquityHistoricalData(date=2023-12-29,
open=193.89999389648438, high=194.39999389648438, low=191.72999572753906,
close=192.52999877929688, volume=42628800, vwap=None, split_ratio=None,
dividend=None)]}
===============================================================================
"""

# Example 3: Company Information
print("\nExample 3: Company Information")
company_info = toolkit.get_company_profile(symbol="AAPL", provider="fmp")
print("\nApple Inc. Company Information:")
print(company_info)
"""
===============================================================================
Apple Inc. Company Information:
[FMPEquityProfileData(symbol=AAPL, name=Apple Inc., cik=0000320193, 
cusip=037833100, isin=US0378331005, lei=None, legal_name=None, 
stock_exchange=NASDAQ Global Select, sic=None, short_description=None, 
long_description=Apple Inc. designs, manufactures, and markets smartphones, 
personal computers, tablets, wearables, and accessories worldwide. The company 
offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, 
a line of multi-purpose tablets; and wearables, home, and accessories 
comprising AirPods, Apple TV, Apple Watch, Beats products, and HomePod. It 
also provides AppleCare support and cloud services; and operates various 
platforms, including the App Store that allow customers to discover and 
download applications and digital content, such as books, music, video, games, 
and podcasts. In addition, the company offers various services, such as Apple 
Arcade, a game subscription service; Apple Fitness+, a personalized fitness 
service; Apple Music, which offers users a curated listening experience with 
on-demand radio stations; Apple News+, a subscription news and magazine 
service; Apple TV+, which offers exclusive original content; Apple Card, a 
co-branded credit card; and Apple Pay, a cashless payment service, as well as 
licenses its intellectual property. The company serves consumers, and small 
and mid-sized businesses; and the education, enterprise, and government 
markets. It distributes third-party applications for its products through the 
App Store. The company also sells its products through its retail and online 
stores, and direct sales force; and third-party cellular network carriers, 
wholesalers, retailers, and resellers. Apple Inc. was founded in 1976 and is 
headquartered in Cupertino, California., ceo=Mr. Timothy D. Cook, 
company_url=https://www.apple.com, business_address=None, 
mailing_address=None, business_phone_no=408 996 1010, hq_address1=One Apple 
Park Way, hq_address2=None, hq_address_city=Cupertino, 
hq_address_postal_code=95014, hq_state=CA, hq_country=US, inc_state=None, 
inc_country=None, employees=164000, entity_legal_form=None, 
entity_status=None, latest_filing_date=None, irs_number=None, 
sector=Technology, industry_category=Consumer Electronics, 
industry_group=None, template=None, standardized_active=None, 
first_fundamental_date=None, last_fundamental_date=None, 
first_stock_price_date=1980-12-12, last_stock_price_date=None, is_etf=False, 
is_actively_trading=True, is_adr=False, is_fund=False, image=https://images.
financialmodelingprep.com/symbol/AAPL.png, currency=USD, 
market_cap=3785298636000, last_price=250.42, year_high=260.1, year_low=164.08, 
volume_avg=43821504, annualized_dividend_amount=0.99, beta=1.24)]
===============================================================================
"""

# Example 4: Financial Statements
print("\nExample 4: Financial Statements")
balance_sheet = toolkit.get_financial_statement(
    symbol="MSFT",
    statement_type="balance",
    period="annual",
    provider="fmp",
    limit=5,
)
income_stmt = toolkit.get_financial_statement(
    symbol="MSFT",
    statement_type="income",
    period="annual",
    provider="fmp",
    limit=5,
)
cash_flow = toolkit.get_financial_statement(
    symbol="MSFT",
    statement_type="cash",
    period="annual",
    provider="fmp",
    limit=5,
)
print("\nMicrosoft Financial Statements Overview:")
print(f"Balance Sheet: {balance_sheet}")
print(f"Income Statement: {income_stmt}")
print(f"Cash Flow Statement: {cash_flow}")
"""
===============================================================================
Microsoft Financial Statements Overview:
Balance Sheet: [FMPBalanceSheetData(period_ending=2024-06-30, 
fiscal_period=FY, fiscal_year=2024, filing_date=2024-07-30, 
accepted_date=2024-07-30 16:06:22, reported_currency=USD, 
cash_and_cash_equivalents=18315000000.0, short_term_investments=57216000000.0, 
cash_and_short_term_investments=75531000000.0, net_receivables=56924000000.0, 
inventory=1246000000.0, other_current_assets=26033000000.0, 
total_current_assets=159734000000.0, plant_property_equipment_net=154552000000.
0, goodwill=119220000000.0, intangible_assets=27597000000.0, 
goodwill_and_intangible_assets=146817000000.0, 
long_term_investments=14600000000.0, tax_assets=None, 
other_non_current_assets=36460000000.0, non_current_assets=352429000000.0, ..
===============================================================================
"""

# Example 5: Financial Analysis with ChatAgent
print("\nExample 5: Financial Analysis with ChatAgent")

# Initialize agent with toolkit tools
tech_agent = ChatAgent(
    system_message="""You are a financial analysis expert. Analyze the provided
    financial data and provide insights about the company's financial 
    health.""",
    tools=toolkit.get_tools(),
)

# Get company data
symbol = "AAPL"

# Get financial statements using correct provider
balance_sheet = toolkit.get_financial_statement(
    symbol=symbol,
    statement_type="balance",
    period="annual",
    provider="fmp",
    limit=3,
)
print(f"\n{symbol} Balance Sheet:")
print(balance_sheet)

income_stmt = toolkit.get_financial_statement(
    symbol=symbol,
    statement_type="income",
    period="annual",
    provider="fmp",
    limit=3,
)
print(f"\n{symbol} Income Statement:")
print(income_stmt)

# Get financial metrics
metrics = toolkit.get_financial_metrics(
    symbol=symbol, period="annual", provider="fmp", limit=3
)
print(f"\n{symbol} Financial Metrics:")
print(metrics)

# Get company profile
profile = toolkit.get_company_profile(symbol=symbol, provider="fmp")
print(f"\n{symbol} Company Profile:")
print(profile)

# Example analysis prompt
analysis_prompt = f"""
Analyze {symbol}'s financial health based on:
1. Balance sheet strength
2. Profitability trends
3. Key financial metrics
4. Business profile

Provide a concise summary of strengths and potential concerns.
"""

response = tech_agent.step(input_message=analysis_prompt)
print("\nFinancial Analysis:")
print(response.msgs[0].content)
"""
===============================================================================
Financial Analysis:
### Financial Health Analysis of Apple Inc. (AAPL)

#### 1. Balance Sheet Strength
- **Total Debt**: The total debt has shown a decreasing trend from 
approximately $132.48 billion in 2022 to $106.63 billion in 2024. This 
indicates a reduction in leverage and improved financial stability.
- **Net Debt**: Similarly, net debt has decreased from about $108.83 billion 
in 2022 to $76.69 billion in 2024, suggesting that the company is managing its 
debt effectively and has sufficient cash reserves to cover its liabilities.

#### 2. Profitability Trends
- **Revenue Growth**: AAPL has consistently generated significant revenue, 
with a notable increase in profitability over the years. The income statement 
shows a healthy profit margin, indicating effective cost management.
- **Operating Income**: The operating income has remained strong, reflecting 
the company's ability to generate profit from its core operations.
- **Interest Expenses**: Interest expenses have been relatively stable, which 
is a positive sign as it indicates that the company is not over-leveraged.

#### 3. Key Financial Metrics
- **Market Capitalization**: As of 2024, AAPL's market cap is approximately 
$3.50 trillion, making it one of the most valuable companies in the world.
- **P/E Ratio**: The P/E ratio has increased from 24.44 in 2022 to 37.29 in 
2024, indicating that the stock may be overvalued relative to its earnings, 
which could be a concern for investors.
- **Dividend Yield**: The dividend yield has decreased slightly, reflecting a 
focus on reinvesting profits for growth rather than returning cash to 
shareholders.
- **Graham Number**: The Graham number indicates that the stock may be 
overvalued, as the calculated value is negative, suggesting that the stock 
price exceeds its intrinsic value based on earnings and book value.

#### 4. Business Profile
- **Industry Position**: AAPL is a leader in the technology sector, 
particularly in consumer electronics, software, and services. Its strong brand 
loyalty and innovative product offerings contribute to its competitive 
advantage.
- **Growth Potential**: The company continues to invest in research and 
development, positioning itself for future growth in emerging technologies and 
services.

### Summary of Strengths and Potential Concerns
**Strengths:**
- Strong balance sheet with decreasing total and net debt.
- Consistent revenue and operating income growth.
- Leading market capitalization and brand recognition.

**Potential Concerns:**
- Increasing P/E ratio may indicate overvaluation.
- Decreasing dividend yield could concern income-focused investors.
- Negative Graham number suggests potential overvaluation based on intrinsic 
value metrics.

Overall, AAPL demonstrates robust financial health, but investors should be 
cautious of valuation metrics that may indicate a correction in stock price.
===============================================================================
"""

# Example 6: ChatAgent using OpenBB toolkit
print("\nExample 6: ChatAgent using OpenBB toolkit")
agent = ChatAgent(
    system_message="""You are a helpful financial analyst that can use
    OpenBB toolkit to analyze stocks and market data. When comparing stock
    prices with moving averages, use the data directly from the stock quotes
    including the volume_average_10d field for accurate analysis.""",
    tools=toolkit.get_tools(),
)

usr_msg = (
    "Compare the current stock prices of AAPL and MSFT with their trading "
    "volumes and 10-day average volumes using the quote data"
)
response = agent.step(input_message=usr_msg)
print("\nAI Analysis:")
print(response.msgs[0].content)
"""
===============================================================================
AI Analysis:
Here is the comparison of the current stock prices, trading volumes,
and 10-day average volumes for Apple Inc. (AAPL) and Microsoft Corporation
(MSFT):

### Apple Inc. (AAPL)
- **Current Price:** $244.75
- **Current Trading Volume:** 44,476,711
- **10-Day Average Volume:** 56,030,030

### Microsoft Corporation (MSFT)
- **Current Price:** $424.63
- **Current Trading Volume:** 20,960,541
- **10-Day Average Volume:** 25,580,240

### Summary
- **AAPL** has a higher current trading volume compared to its 10-day
average volume, indicating increased trading activity.
- **MSFT** has a lower current trading volume than its 10-day average
volume, suggesting less trading activity relative to the past 10 days.

If you need further analysis or details, feel free to ask!
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\post_weather_on_twitter.py
--------------------------------------------------------------------------------

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
from colorama import Fore

from camel.agents import ChatAgent
from camel.toolkits import SearchToolkit, TwitterToolkit, WeatherToolkit
from camel.utils import print_text_animated


def main():
    """
    To run this, you need to set the following environment variables:
    - TWITTER_CONSUMER_KEY
    - TWITTER_CONSUMER_SECRET
    - TWITTER_ACCESS_TOKEN
    - TWITTER_ACCESS_TOKEN_SECRET
    - OPENWEATHERMAP_API_KEY
    - GOOGLE_API_KEY
    - SEARCH_ENGINE_ID
    """

    sys_msg = "You are a helpful agent with multiple tools."

    agent = ChatAgent(
        system_message=sys_msg,
        tools=[
            *TwitterToolkit().get_tools(),
            *WeatherToolkit().get_tools(),
            *SearchToolkit().get_tools(),
        ],
    )

    usr_msg = "I'm in Chicago and want to travel to Oxford today. Make a "
    "travel plan for me, considering the weather today. Also announce my "
    "plan on Twitter from my perspective."

    response = agent.step(usr_msg)

    for tool_call in response.info["tool_calls"]:
        print(f"{Fore.YELLOW}{tool_call}{Fore.RESET}\n======")

    print_text_animated(
        f"{Fore.GREEN}{response.msg.content}{Fore.RESET}", delay=0.005
    )


if __name__ == '__main__':
    main()



--------------------------------------------------------------------------------
# File: toolkits\pubmed_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import PubMedToolkit
from camel.types import ModelPlatformType, ModelType

# Initialize PubMed toolkit and get tools
tools = PubMedToolkit().get_tools()

# Set up model configuration
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Create chat agent
system_msg = (
    "You are a research assistant specialized in medical literature. "
    "Help researchers find and analyze scientific papers from PubMed."
)
camel_agent = ChatAgent(
    system_message=system_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Example 1: Search for recent papers about mRNA vaccine technology
print("\nExample 1: Search for recent papers about mRNA vaccine technology")
print("=" * 80)

usr_msg = (
    "Find recent review papers about mRNA vaccine technology published "
    "in 2024, with a focus on therapeutic applications and clinical trials. "
    "Limit to 3 papers."
)

response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:2000])

"""
===============================================================================
ToolCallingRecord(
    tool_name='search_papers',
    args={
        'query': 'mRNA vaccine tech therapeutic applications trials',
        'max_results': 10,
        'sort': 'date',
        'date_range': {'from': '2024/01/01', 'to': '2024/12/31'},
        'publication_type': ['Review'],
    },
    result=[
        {
            'id': '39601789',
            'title': 'Example Title',
            'authors': 'First Author, Second Author',
            'journal': 'Example Journal',
            'pub_date': '2025 Jan 6',
            'abstract': 'Abstract of the paper',
===============================================================================
"""


# Example 2: Get detailed information about a specific paper
print("\nExample 2: Get detailed paper information")
print("=" * 80)

usr_msg = (
    "Get detailed information about PubMed ID 39601789 "
    "(a key paper about mRNA vaccine technology)."
)
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:2000])

"""
===============================================================================
[ToolCallingRecord(
    tool_name='get_paper_details',
    args={'paper_id': 37840631, 'include_references': True},
    result={
        'id': '37840631',
        'title': 'Chinese guideline for lipid management (2023):
                  a new guideline rich in domestic elements for 
                  controlling dyslipidemia.',
        'authors': 'Li JJ',
        'journal': 'J Geriatr Cardiol',
        'pub_date': '2023 Sep 28',
        'abstract': '1. J Geriatr Cardiol. 
                     2023 Sep 28;20(9):618-620. 
                     doi: 10.26599/1671-5411.2023.09.007.
                     Chinese guideline for lipid management (2023):
                     a new guideline rich in domestic elements for 
                     controlling dyslipidemia.Li JJ(1).\Author information:
                     (1)Division of Cardio-Metabolic Center,
                     State Key Laboratory of Cardiovascular 
                     Disease, Fu Wai Hospital, National Center 
                     for Cardiovascular Disease, Chinese Academy
                     of Medical Sciences, Peking Union Medical College,
                     Beijing, China.DOI: 10.26599/1671-5411.2023.09.007
                     PMCID: PMC10568543\nPMID: 37840631',
        'doi': 'doi: 10.26599/1671-5411.2023.09.007',
        'keywords': [],
        'mesh_terms': [],
        'publication_types': ['Journal Article'],
        'references': ['35729555', '34734202', '34404993', 
                       '31172370', '30586774', '30526649', 
                       '29434622', '20350253']
    },
    tool_call_id='call_k8s7oFcRvDBKuEKvk48uoWXZ'
)]
===============================================================================
"""

# Example 3: Find related papers and citation metrics
print("\nExample 3: Find related papers and citation metrics")
print("=" * 80)

usr_msg = (
    "Find papers related to PubMed ID 39601789 (limit to 3 papers) and "
    "show its citation count."
)
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:2000])

"""
===============================================================================
[ToolCallingRecord(
    tool_name='get_related_papers',
    args={'paper_id': 37840631, 'max_results': 5},
    result=[
        {'id': '37840631',
         'title': 'Chinese guideline for lipid management (2023):
                   a new guideline rich in domestic elements for 
                   controlling dyslipidemia.',
         'authors': 'Li JJ',
         'journal': 'J Geriatr Cardiol',
         'pub_date': '2023 Sep 28',
         'abstract': (
             '1. J Geriatr Cardiol. 2023 Sep 28;20(9):618-620. doi: '
             '10.26599/1671-5411.2023.09.007.'
             'Chinese guideline for lipid management (2023): a new guideline'
             'rich in domestic elements for controlling dyslipidemia.'
             'Li JJ(1).Author information:(1)Division of Cardio-Metabolic '
             'Center, State Key Laboratory of Cardiovascular Disease, Fu Wai '
             'Hospital, National Center for Cardiovascular Disease, Chinese '
             'Academy of Medical Sciences, Peking Union Medical College, '
             'Beijing, China.DOI: 10.26599/1671-5411.2023.09.007'
             'PMCID: PMC10568543  PMID: 37840631'
         ),
         'doi': 'doi: 10.26599/1671-5411.2023.09.007',
         'keywords': [],
         'mesh_terms': [],
         'publication_types': ['Journal Article'],
         'references': None},
        {'id': '22801311',
         'title': (
             '[Short-term impact of modified blood-lipid reports on physicians'
             'lipid lowering drug prescribing behavior and knowledge '
             'improvement on dyslipidemia].'
         ),
         'authors': 'Li JH, Jiang H, Sun XH, Li CC, Ke YN, Yan SK, Wu YF',
         'journal': 'Zhonghua Xin Xue Guan Bing Za Zhi',
         'pub_date': '2012 Apr',
         'abstract': (
             '1. Zhonghua Xin Xue Guan Bing Za Zhi. 2012 Apr;40(4):318-22.'
             '[Short-term impact modified blood-lipid reports on physicians'
             'lipid lowering drug prescribing behavior and knowledge '
             'improvement on dyslipidemia].Article in Chinese]'
             'Li JH(1), Jiang H, Sun XH, Li CC, Ke YN, Yan SK, Wu YF.'
             'Author information:(1)Department of Cardiology, China-Japan'
===============================================================================
"""

# Example 4: Advanced search with multiple filters
print("\nExample 4: Advanced search with multiple filters")
print("=" * 80)

usr_msg = (
    "Find clinical trial papers about mRNA-based cancer vaccines published "
    "between 2023/01/01 and 2024/03/01, focusing on phase III trials. "
    "Limit to 3 papers."
)
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:2000])

"""
===============================================================================
[ToolCallingRecord(
    tool_name='search_papers',
    args={
        'query': 'mRNA cancer vaccine phase III clinical trial',
        'max_results': 10,
        'sort': 'date',
        'date_range': {'from': '2023/01/01', 'to': '2024/03/01'},
        'publication_type': ['Clinical Trial']
    },
    result=[
        {
            'id': '37820782',
            'title': 'Stochastic interventional approach to assessing immune '
                      'correlates of protection: Application to the COVE '
                      'RNA-1273 vaccine trial.',
            'authors': (
                'Hejazi NS, Shen X, Carpp LN, Benkeser D, Follmann D, 
                Janes HE, Baden LR, El Sahly HM, Deng W, Zhou H, 
                Leav B, Montefiori DC, 'Gilbert PB'
            ),
            'journal': 'Int J Infect Dis',
            'pub_date': '2023 Dec',
            'abstract': Abstract of the paper
===============================================================================
"""

# Example 5: Get abstract and analyze citations
print("\nExample 5: Get abstract and analyze citations")
print("=" * 80)

usr_msg = (
    "Get the abstract of PubMed ID 39601789 and find out how many times "
    "it has been cited."
)
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:2000])

"""
===============================================================================
[
    ToolCallingRecord(
        tool_name='get_abstract',
        args={'paper_id': 37840631},
        result='''
            1. J Geriatr Cardiol. 2023 Sep 28;20(9):618-620. doi: 
            10.26599/1671-5411.2023.09.007.
            
            Chinese guideline for lipid management (2023):a new guideline 
            rich in domestic elements for controlling dyslipidemia.
            
            Li JJ(1).
            
            Author information:
            (1)Division of Cardio-Metabolic Center, State Key Laboratory
            of Cardiovascular Disease, Fu Wai Hospital, National Center 
            for Cardiovascular Disease, Chinese Academy of Medical Sciences,
            Peking Union Medical College, Beijing, China.
            
            DOI: 10.26599/1671-5411.2023.09.007
            PMCID: PMC10568543
            PMID: 37840631
        ''',
        tool_call_id='call_AFG6jLkdvWidaVGrj9UblTci'
    ),
    ToolCallingRecord(
        tool_name='get_citation_count',
        args={'paper_id': 37840631},
        result=0,
        tool_call_id='call_ZM3p59gtYmeR9DPdONNHV4Qw'
    )
]
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\reddit_toolkit.py
--------------------------------------------------------------------------------

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

from camel.toolkits import RedditToolkit

reddit_toolkit = RedditToolkit()

# Example usage of collect_top_posts
subreddit_name = "python"
post_limit = 2
comment_limit = 3

print(f"Collecting top {post_limit} posts from r/{subreddit_name}...\n")
top_posts_data = reddit_toolkit.collect_top_posts(
    subreddit_name, post_limit, comment_limit
)

# Output the top posts data
for post in top_posts_data:
    print(f"Post Title: {post['Post Title']}")
    for comment in post["Comments"]:
        print(f"  Comment: {comment['Comment Body']}")
        print(f"  Upvotes: {comment['Upvotes']}")
    print()

'''
===============================================================================
Collecting top 2 posts from r/python...

Post Title: Lad wrote a Python script to download 
            Alexa voice recordings, 
            he didn't expect this email.
  Comment: I will be honest, I was expecting a Cease 
           and Desist from Amazon.
  Upvotes: 1857
  Comment: Very cool. That is the beauty of sharing. 
           You never know who or how it will help someone, 
           but you post it anyway because that is just being awesome. 

Thanks for sharing.
  Upvotes: 264
  Comment: This was posted publicly by [Michael Haephrati]
            (https://www.facebook.com/photo.php?fbid=10220524693682311)
            on Facebook.

Update: The lad is a Redditor! [**u/haephrati**]
        (https://www.reddit.com/user/haephrati/)

Update: The lad turned it into a [Software]
        (https://www.facebook.com/pg/accexa2020/about/?ref=page_internal)!
  Upvotes: 219

Post Title: This post has:
  Comment: scale tap piquant quiet advise salt languid abundant dolls long
           -- mass edited with redact.dev
  Upvotes: 1325
  Comment: Good job. But honestly, add a sleep timer of a few seconds. 
           This will eventually get your IP banned on reddit 
           if you bombard them with too many requests.
  Upvotes: 408
  Comment: Cool! Could you share it?
  Upvotes: 113
===============================================================================
'''

# Track keyword discussions
keywords = [
    "python",
    "programming",
    "coding",
    "software",
    "development",
    "machine learning",
    "artificial intelligence",
    "AI",
    "deep learning",
    "data science",
    "analytics",
    "automation",
    "tech",
    "technology",
    "engineering",
    "developer",
    "algorithm",
    "API",
    "framework",
    "library",
    "tool",
    "debug",
    "optimization",
    "performance",
    "security",
    "privacy",
    "database",
    "cloud",
    "server",
    "network",
    "startup",
    "entrepreneur",
    "innovation",
    "research",
    "science",
]

subreddits = [
    "python",
    "learnprogramming",
    "datascience",
    "machinelearning",
]
keyword_data = reddit_toolkit.track_keyword_discussions(
    subreddits, keywords, post_limit=2, comment_limit=5
)


# Perform sentiment analysis on collected data
sentiment_data = reddit_toolkit.perform_sentiment_analysis(keyword_data)

# Output the results
for item in sentiment_data:
    print(f"Subreddit: {item['Subreddit']}")
    print(f"Post Title: {item['Post Title']}")
    print(f"Comment Body: {item['Comment Body']}")
    print(f"Upvotes: {item['Upvotes']}")
    if 'Sentiment Score' in item:
        print(f"Sentiment Score: {item['Sentiment Score']}")
    print()

'''
===============================================================================

Subreddit: learnprogramming
Post Title: I ran a 100% free full stack web development bootcamp
            for those laid off by the pandemic. 
            65 people got jobs and we are doing it again! 
            I would love to have you join us!
Comment Body: If you want to learn to code, this will change your life.
Can't make it to class? Recorded classes are on Twitch and YouTube
Never touched code before? He starts from square 1!
Shy/introvert/don't like talking? Stick to the chat
Don't have support in real life? 
Join the discord and get more support and hype than your family
Don't have money? It's free!
Not in the US? Leon is Mr. Worldwide when it comes to teaching!
100Devs isn't just a free online bootcamp, 
it's a whole support network that will be there for you to cheer you on, 
help you out, and give you a shoulder to cry on. 
If you're on the fence, give it a try. You won't regret it.
Upvotes: 518
Sentiment Score: 0.385

Subreddit: learnprogramming
Post Title: I ran a 100% free full stack web development bootcamp 
            for those laid off by the pandemic. 
            65 people got jobs and we are doing it again! 
            I would love to have you join us!
Comment Body: If you need any free dev help let me know

I was also a teacher for 15 years before coding if that's helpful too
Upvotes: 533
Sentiment Score: 0.4

Subreddit: datascience
Post Title: data siens
Comment Body: I was once reading this article that went as: 
              "The AI already predicted how many goals Cavani 
              will score at Manchester United". 
It was a linear regression.
Upvotes: 345
Sentiment Score: 0.5

Subreddit: machinelearning
Post Title: [D] A Demo from 1993 of 32-year-old Yann LeCun 
            showing off the World's first Convolutional 
            Network for Text Recognition
Comment Body: The fact that they also had to know the 
              location of the numbers and that the algorithm 
              was robust to scale changes is impressive for 1993

It's not like they just solved MNIST in 1993, it's one step above that
Upvotes: 412
Sentiment Score: 0.5
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\role_playing_with_functions.py
--------------------------------------------------------------------------------

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

from typing import List

from colorama import Fore

from camel.agents.chat_agent import ToolCallingRecord
from camel.models import ModelFactory
from camel.societies import RolePlaying
from camel.toolkits import (
    MathToolkit,
    SearchToolkit,
)
from camel.types import ModelPlatformType, ModelType
from camel.utils import print_text_animated


def main(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    chat_turn_limit=10,
) -> None:
    task_prompt = (
        "Assume now is 2024 in the Gregorian calendar, "
        "estimate the current age of University of Oxford "
        "and then add 10 more years to this age, "
        "and get the current weather of the city where "
        "the University is located. You must use tool to solve the task."
    )

    tools_list = [
        *MathToolkit().get_tools(),
        SearchToolkit().search_duckduckgo,
    ]

    role_play_session = RolePlaying(
        assistant_role_name="Searcher",
        user_role_name="Professor",
        assistant_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
            ),
            tools=tools_list,
        ),
        user_agent_kwargs=dict(
            model=ModelFactory.create(
                model_platform=model_platform,
                model_type=model_type,
            ),
        ),
        task_prompt=task_prompt,
        with_task_specify=False,
    )

    print(
        Fore.GREEN
        + f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n"
    )
    print(
        Fore.BLUE + f"AI User sys message:\n{role_play_session.user_sys_msg}\n"
    )

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN
        + "Specified task prompt:"
        + f"\n{role_play_session.specified_task_prompt}\n"
    )
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    n = 0
    input_msg = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI Assistant terminated. Reason: "
                    f"{assistant_response.info['termination_reasons']}."
                )
            )
            break
        if user_response.terminated:
            print(
                Fore.GREEN
                + (
                    "AI User terminated. "
                    f"Reason: {user_response.info['termination_reasons']}."
                )
            )
            break

        # Print output from the user
        print_text_animated(
            Fore.BLUE + f"AI User:\n\n{user_response.msg.content}\n"
        )

        # Print output from the assistant, including any function
        # execution information
        print_text_animated(Fore.GREEN + "AI Assistant:")
        tool_calls: List[ToolCallingRecord] = [
            ToolCallingRecord(**call.as_dict())
            for call in assistant_response.info['tool_calls']
        ]
        for func_record in tool_calls:
            print_text_animated(f"{func_record}")
        print_text_animated(f"{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_msg = assistant_response.msg


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: toolkits\search_toolkit.py
--------------------------------------------------------------------------------

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

from pydantic import BaseModel

from camel.agents import ChatAgent
from camel.toolkits import FunctionTool, SearchToolkit

res_simple = SearchToolkit().query_wolfram_alpha(
    query="solve 3x-7=11", is_detailed=False
)

print(res_simple)
'''
===============================================================================
x = 6
===============================================================================
'''

res_detailed = SearchToolkit().query_wolfram_alpha(
    query="solve 3x-7=11", is_detailed=True
)

print(res_detailed)
'''
===============================================================================
{'query': 'solve 3x-7=11', 'pod_info': [{'title': 'Input interpretation', 
'description': 'solve 3 x - 7 = 11', 'image_url': 'https://www6b3.wolframalpha.
com/Calculate/MSP/MSP37741a3dc67f338579ff00003fih94dg39300iaf?
MSPStoreType=image/gif&s=18'}, {'title': 'Result', 'description': 'x = 6', 
'image_url': 'https://www6b3.wolframalpha.com/Calculate/MSP/
MSP37751a3dc67f338579ff00001dg4gbdcd0f10i3f?MSPStoreType=image/gif&s=18'}, 
{'title': 'Plot', 'description': None, 'image_url': 'https://www6b3.
wolframalpha.com/Calculate/MSP/MSP37761a3dc67f338579ff0000374484g95bh3ah3e?
MSPStoreType=image/gif&s=18'}, {'title': 'Number line', 'description': None, 
'image_url': 'https://www6b3.wolframalpha.com/Calculate/MSP/
MSP37771a3dc67f338579ff00005573c3a87ahg8dbc?MSPStoreType=image/gif&s=18'}], 
'final_answer': 'x = 6', 'steps': {'step1': 'Isolate terms with x to the left 
hand side.\nAdd 7 to both sides:\n3 x + (7 - 7) = 7 + 11', 'step2': 'Look for 
the difference of two identical terms.\n7 - 7 = 0:\n3 x = 11 + 7', 'step3': 
'Evaluate 11 + 7.\n11 + 7 = 18:\n3 x = 18', 'step4': 'Divide both sides by a 
constant to simplify the equation.\nDivide both sides of 3 x = 18 by 3:\n(3 x)/
3 = 18/3', 'step5': 'Any nonzero number divided by itself is one.\n3/3 = 1:\nx 
= 18/3', 'step6': 'Reduce 18/3 to lowest terms. Start by finding the greatest 
common divisor of 18 and 3.\nThe greatest common divisor of 18 and 3 is 3, so 
factor out 3 from both the numerator and denominator: 18/3 = (3x6)/(3x1) = 3/3 
x 6 = 6\nAnswer: | \n | x = 6'}}
===============================================================================
'''

res_brave = SearchToolkit().search_brave(
    q="What is the weather in Tokyo?",
    search_lang="en",
)
print(res_brave)

# Example with ChatAgent using the Brave search engine

agent = ChatAgent(
    system_message="""You are a helpful assistant that can use brave search 
        engine to answer questions.""",
    tools=[FunctionTool(SearchToolkit().search_brave)],
)

usr_msg = "What is the temperature in Tokyo?"

response = agent.step(input_message=usr_msg, response_format=None)

print(response.msgs[0].content)
"""
===============================================================================
The current temperature in Tokyo can be found on various weather websites. 
Here are a couple of reliable sources where you can check the latest weather 
conditions:

1. [AccuWeather - Tokyo Current Weather](https://www.accuweather.com/en/jp/tokyo/226396/current-weather/226396)
2. [Time and Date - Tokyo Weather](https://www.timeanddate.com/weather/japan/tokyo)

You can visit these links to get the most up-to-date temperature and weather 
conditions in Tokyo.
===============================================================================
"""
search_linkup_response = SearchToolkit().search_linkup(
    query="Can you tell me which women were awarded the Physics Nobel Prize",
    depth="standard",
    output_type="searchResults",
)

print(search_linkup_response)
"""
===============================================================================
{'results': [{'type': 'text', 'name': 'Physics Nobel Prizes awarded to women | 
Scientia News', 'url': 'https://www.scientianews.org/
physics-nobel-prize-winners', 'content': 'The next female Nobel Prize in 
Physics award winner wouldn't be until another half-century later, with Donna 
Strickland. Strickland was awarded the Prize for her work on chirped pulse 
amplification and its applications. Although the research itself was published 
in 1985, she didn't receive the award until 2018.'}, {'type': 'text', 'name': 
'The 60 Women Who Have Won the Nobel Prize - Stacker', 'url': 'https://stacker.
com/history/60-women-who-have-won-nobel-prize', 'content': '- Award: Nobel 
Prize in Physics - Year: 1963. Maria Goeppert-Mayer was born in Germany. After 
she married, she migrated to America, where she worked on an American atom 
bomb project during World War II. Her work uncovered important discoveries 
about nuclear structure, and Goeppert-Mayer is one of only four women to win 
the Nobel Prize in physics.'}, {'type': 'text', 'name': 'Nobel Prize awarded 
women - NobelPrize.org', 'url': 'https://www.nobelprize.org/prizes/lists/
nobel-prize-awarded-women/', 'content': 'The Nobel Prize and the Sveriges 
Riksbank Prize in Economic Sciences in Memory of Alfred Nobel have been 
awarded to women 66 times between 1901 and 2024. Only one woman, Marie Curie, 
has been honoured twice, with the Nobel Prize in Physics 1903 and the Nobel 
Prize in Chemistry 1911. This means that 65 women in total have been awarded 
the Nobel ...'}, {'type': 'text', 'name': 'Women who changed science - The 
Nobel Prize', 'url': 'https://www.nobelprize.org/womenwhochangedscience/
stories', 'content': 'Nobel Prize in Physics 1903 Nobel Prize in Chemistry 
1911. MARIE CURIE. Read her story. Nobel Prize in Physiology or Medicine 1988. 
GERTRUDE B. ELION. Read her story. Nobel Prize in Physiology or Medicine 1988. 
GERTRUDE B. ELION. Read her story. Nobel Prize in Physics 1963. MARIA GOEPPERT 
MAYER. Read her story.'}, {'type': 'text', 'name': 'List of female Nobel 
laureates - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/
List_of_female_Nobel_laureates', 'content': "The most recent women to be 
awarded a Nobel Prize were Han Kang in Literature (2024), Claudia Goldin in 
Economics, Narges Mohammadi for Peace, Anne L'Huillier in Physics and Katalin 
Karikó in Physiology or Medicine (2023), Annie Ernaux in Literature and 
Carolyn R. Bertozzi for Chemistry (2022), Maria Ressa for Peace (2021), Louise 
Glück in ..."}, {'type': 'text', 'name': 'Only 5 women have won the Nobel 
Prize in physics—recent winners share ...', 'url': 'https://phys.org/news/
2024-10-women-won-nobel-prize-physics.html', 'content': 'Out of 225 people 
awarded the Nobel Prize in physics, only five have been women. This is a very 
small number, and certainly smaller than 50%—the percent of women in the human 
population.'}, {'type': 'text', 'name': 'All These Women Won Science Nobel 
Prizes - The Stemettes Zine', 'url': 'https://stemettes.org/zine/articles/
nobel-prize-women/', 'content': 'Currently, only 17% of Nobel Prize winners 
are women in the Science categories. So here we are celebrating all the 
amazing women who have Nobel Prizes for their Science research. ... & Physics 
(1903) Marie and her husband were awarded the Nobel Prize for Physics in 1903, 
for their study into the spontaneous radiation discovered by Becquerel. In ...
'}, {'type': 'text', 'name': 'These Are the 57 Women Who Have Won the Nobel 
Prize', 'url': 'https://www.newsweek.com/
these-are-57-women-who-have-won-nobel-prize-1538702', 'content': 'Getty Images/
Hulton-Deutsch Collection/CORBIS Marie Curie (born Skłodowska) - Award: Nobel 
Prize in Physics - Year: 1903. Marie Curie, who was the first woman to win a 
Nobel Prize, coined the ...'}, {'type': 'text', 'name': 'Anne L'Huillier - 
Banquet speech - NobelPrize.org', 'url': 'https://www.nobelprize.org/prizes/
physics/2023/lhuillier/speech/', 'content': 'The Nobel Prize in Physics 2023 
was awarded to Pierre Agostini, Ferenc Krausz and Anne L'Huillier "for 
experimental methods that generate attosecond pulses of light for the study of 
electron dynamics in matter" ... 120 years ago, Marie Skłodowska Curie was the 
first woman to be awarded the Nobel Prize in Physics. I am the fifth. For 
more ...'}, {'type': 'text', 'name': 'Facts on the Nobel Prize in Physics - 
NobelPrize.org', 'url': 'https://www.nobelprize.org/prizes/facts/
facts-on-the-nobel-prize-in-physics/', 'content': 'List of all female Nobel 
Prize laureates. Multiple Nobel Prize laureates in physics. John Bardeen is 
the only person who has received the Nobel Prize in Physics twice, year 1956 
and 1972 . Marie Curie was awarded the Nobel Prize twice, once in physics 1903 
and once in chemistry 1911.. See the list of multiple Nobel Prize laureates 
within other Nobel Prize categories here'}]}
===============================================================================
"""

search_linkup_response = SearchToolkit().search_linkup(
    query="Can you tell me which women were awarded the Physics Nobel Prize",
    depth="standard",
    output_type="sourcedAnswer",
)

print(search_linkup_response)
"""
===============================================================================
{'answer': "The women who have been awarded the Nobel Prize in Physics are: 1. 
Marie Curie - 1903 2. Maria Goeppert Mayer - 1963 3. Donna Strickland - 2018 
4. Anne L'Huillier - 2023", 'sources': [{'name': 'Nobel Prize awarded women - 
NobelPrize.org', 'url': 'https://www.nobelprize.org/prizes/lists/
nobel-prize-awarded-women/', 'snippet': 'The Nobel Prize and the Sveriges 
Riksbank Prize in Economic Sciences in Memory of Alfred Nobel have been 
awarded to women 66 times between 1901 and 2024.'}, {'name': 'Physics Nobel 
Prizes awarded to women | Scientia News', 'url': 'https://www.scientianews.org/
physics-nobel-prize-winners', 'snippet': 'The next female Nobel Prize in 
Physics award winner wouldn't be until another half-century later, with Donna 
Strickland.'}, {'name': 'List of female Nobel laureates - Wikipedia', 'url': 
'https://en.wikipedia.org/wiki/List_of_female_Nobel_laureates', 'snippet': 
"The most recent women to be awarded a Nobel Prize were Han Kang in Literature 
(2024), Claudia Goldin in Economics, Narges Mohammadi for Peace, Anne 
L'Huillier in Physics and Katalin Karikó in Physiology or Medicine (2023)."}]}
===============================================================================
"""


class PersonInfo(BaseModel):
    # Basic company information
    name: str = ""  # Company name
    description: str = ""


search_linkup_response = SearchToolkit().search_linkup(
    query="Can you tell me which women were awarded the Physics Nobel Prize",
    depth="standard",
    output_type="structured",
    structured_output_schema=PersonInfo,
)
print(search_linkup_response)

"""
===============================================================================
{'name': 'Female Nobel Prize Winners in Physics', 'description': 'The women 
awarded the Nobel Prize in Physics include: 1. Marie Curie (1903) 2. Maria 
Goeppert-Mayer (1963) 3. Donna Strickland (2018) 4. (4th winner not mentioned 
in the provided data) 5. (5th winner not mentioned in the provided data). Less 
than 5 women have won the Nobel Prize in Physics out of 225 total laureates.'}
===============================================================================
"""

search_bocha_response = SearchToolkit().search_bocha(
    query="阿里巴巴2024年的esg报告",
    freshness="noLimit",
    summary=False,
    count=10,
)
print(search_bocha_response)

"""
===============================================================================
{"_type":"SearchResponse","queryContext":{"originalQuery":"阿里巴巴2024年的esg报
告"},"webPages":{"webSearchUrl":"","totalEstimatedMatches":8912791,"value":[
{"id":None,"name":"阿里巴巴发布2024年ESG报告持续推进减碳与数字化普惠","url":"ht
tps://www.alibabagroup.com/document-1752073403914780672","displayUrl":"htt
ps://www.alibabagroup.com/document-1752073403914780672","snippet":"阿里巴巴
集团发布《2024财年环境、社会和治理(ESG)报告》(下称"报告"),详细分享过去一年在ESG各方面取
得的进展。报告显示,阿里巴巴扎实推进减碳举措,全集团自身运营净碳排放和价值链碳...","siteName"
:"www.alibabagroup.com","siteIcon":"https://th.bochaai.com/favicon?domain_url=
https://www.alibabagroup.com/document-1752073403914780672","dateLastCrawled":
"2024-07-22T00:00:00Z","cachedPageUrl":None,"language":None,"isFamilyFriendly"
:None,"isNavigational":None},],"someResultsRemoved":true},"images":{"id":None,
"readLink":None,"webSearchUrl":None,"value":[{"webSearchUrl":None,"name":None,
"thumbnailUrl":"http://q7.itc.cn/q_70/images01/20240726/ee26d6fa8658472d8b4c5
e7236b1640a.png","datePublished":None,"contentUrl":"http://q7.itc.cn/q_70/im
ages01/20240726/ee26d6fa8658472d8b4c5e7236b1640a.png","hostPageUrl":"https://
m.sohu.com/a/796245119_121713887/?pvid=000115_3w_a","contentSize":None,"enco
dingFormat":None,"hostPageDisplayUrl":"https://m.sohu.com/a/796245119_121713887
/?pvid=000115_3w_a","width":1285,"height":722,"thumbnail":None}],"isFamilyFrien
dly":None},"videos":None}
===============================================================================
"""


agent = ChatAgent(
    system_message="""You are a helpful assistant that can use baidu search 
        engine to answer questions.""",
    tools=[FunctionTool(SearchToolkit().search_baidu)],
)

usr_msg = "今天北京的天气如何"

response = agent.step(input_message=usr_msg, response_format=None)

print(response.msgs[0].content)

"""
===============================================================================
今天北京的天气信息可以通过以下链接查看:

1. [中国天气网 - 北京天气预报](http://www.baidu.com/link?
url=AJhE9PhEO3TmkJ70CUcRsR3NVB3m6wxN5Imdp0ZVsEBK1t8YhtM6YMxrQy3_vRN6dJv4FLHkBCe
fZURnzHTm9gio-dS4-4MwGVgJe40m7prOoggce2eB0h-3DsllbKMm)
2. [中国天气网 - 北京天气预报](http://www.baidu.com/link?
url=1vhNOfl9tV65_104GMQbDnU_fdCZPXDV2BtTJelxdd6isdSZjAHvtoXqOWG3n7D1N-m9zAmOhQG
c-jEGqiXe9K)
3. [中国天气网 - 北京天气预报](http://www.baidu.com/link?
url=Q0URfpodXDpUe1TKBPpToKIyIuCcjSGUR5jorx81g8Pni5XH-Tbc6AXMa7EwCWjBG3jysTZb43S
6ZCsJOKvPw2EbIlQ_bMu42-5sCraqXlS)
4. [中国天气网 - 北京天气预报一周](http://www.baidu.com/link?
url=TtFe8QryJFuwX1kx50YF5WijRcd2TMJRhPudDQvqW7TG4siah68gUZd_frsVWPi1xkYvrxoYL87
QMH0wSjDYOq)

请点击链接查看详细的天气预报信息。
===============================================================================
"""

bing_call_agent = ChatAgent(
    system_message="""You are a helpful assistant that can use baidu search 
        engine to answer questions.""",
    tools=[FunctionTool(SearchToolkit().search_bing)],
)

bing_usr_msg = "帮忙查询巴黎圣母院最新修复进展"

response = bing_call_agent.step(
    input_message=bing_usr_msg, response_format=None
)

print(response.msgs[0].content)

"""
===============================================================================
以下是关于巴黎圣母院最新修复进展的一些信息:

1. **时隔4年,灾后余生的巴黎圣母院即将重生** -
[知乎](https://zhuanlan.zhihu.com/p/619405504)
   
2. **历时4年,耗资70亿,被烧塌的巴黎圣母院修好了!!** -
[腾讯网](https://news.qq.com/rain/a/20231018A0329F00)

3. **一票难求!巴黎圣母院重新开放!5年修复离不开来自东方的支持** -
[新浪财经](https://finance.sina.com.cn/wm/2024-12-08/doc-incyumnp3384392.shtml)

4. **巴黎圣母院浴火重生!建筑学者:勘探报告近3000页,修复工作复杂** -
[腾讯网](https://news.qq.com/rain/a/20241208A05Q9K00)

这些链接提供了关于巴黎圣母院修复的详细信息和最新进展。
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\searxng_toolkit_example.py
--------------------------------------------------------------------------------

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
from typing import Optional

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.logger import get_logger
from camel.models import ModelFactory
from camel.toolkits import SearxNGToolkit
from camel.types import ModelPlatformType, ModelType

logger = get_logger(__name__)


def get_searxng_instance() -> Optional[str]:
    r"""Get SearxNG instance URL from environment variable.

    Returns:
        Optional[str]: The SearxNG instance URL if set, None otherwise.
    """
    instance_url = os.getenv('SEARXNG_URL')
    if not instance_url:
        logger.warning(
            "SEARXNG_URL environment variable not set. "
            "Please set it to your SearxNG instance URL."
        )
    return instance_url


def main() -> None:
    r"""Run the SearxNG toolkit example."""
    # Get SearxNG instance URL
    instance_url = get_searxng_instance()
    if not instance_url:
        logger.error(
            "\nTo run this example:"
            "\n1. Find a SearxNG instance (self-host or use public instance)"
            "\n2. Set the SEARXNG_URL environment variable:"
            "\n   export SEARXNG_URL='https://your-searxng-instance.com'"
            "\n\nPublic instances can be found at: https://searx.space"
        )
        return

    # Initialize the toolkit
    searxng_toolkit = SearxNGToolkit(
        searxng_host=instance_url,
        language="en",
        categories=["general", "news"],
        time_range="month",
        safe_search=1,
    )

    # Initialize the model
    model = ModelFactory.create(
        model_type=ModelType.DEFAULT,
        model_platform=ModelPlatformType.DEFAULT,
        model_config_dict=ChatGPTConfig(temperature=0.0).as_dict(),
    )

    # Create chat agent
    system_message = (
        "You are a helpful assistant that can search the web using SearxNG."
    )
    agent = ChatAgent(
        system_message=system_message,
        model=model,
        tools=[*searxng_toolkit.get_tools()],
    )

    # Example search query
    query = "Tell me about the CAMEL AI framework"
    response = agent.step(query)

    # Print the response message content
    print("\nAgent Response:")
    print(response.msgs[0].content)

    # Print tool calls if needed
    print("\nTool Calls:")
    print(response.info['tool_calls'])


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: toolkits\semantic_scholar_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import SemanticScholarToolkit
from camel.types import ModelPlatformType, ModelType

# Define the model, here in this case we use gpt-4o
model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=ChatGPTConfig(temperature=0.0).as_dict(),
)


sys_msg = "You are a helpful assistant"

# Initialize a toolkit
toolkit = SemanticScholarToolkit()
# Get list of tools
tools = toolkit.get_tools()

# Initialize a ChatAgent with your custom tools
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)

# Description of the added tools
usr_msg = "Describe the tools you've added"

response = camel_agent.step(usr_msg)
print(response.msgs[0].content)

'''
================================================================
1. **fetch_paper_data_title**: This tool fetches a single paper
 based on its title. You can specify which fields to include in
 the response, such as the abstract, authors, year, citation
 count, and more.

2. **fetch_paper_data_id**: Similar to the previous tool,
 this one retrieves a single paper but uses a paper ID instead
 of the title. It also allows for specifying the fields to
 include in the response.

3. **fetch_bulk_paper_data**: This tool allows you to fetch
 multiple papers at once based on a query that can include
 various operators (like AND, OR, NOT). You can filter by
 year and specify which fields to return.

4. **fetch_recommended_papers**: This tool provides
 recommendations for papers based on a list of positively
 and negatively correlated paper IDs. You can specify the
 fields to include in the response and limit the number
 of papers returned.

5. **fetch_author_data**: This tool retrieves information
 about authors based on their IDs. You can specify which
 fields to include in the response, such as the author's name,
 URL, paper count, h-index, and their papers.

These tools can be used individually or in combination to
 gather comprehensive information about academic literature
 and authors.
================================================================
'''

# Search a paper through its id
usr_msg = """search the paper 'Construction of the Literature
    Graph in Semantic Scholar' for me including its paperid"""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_paper_data_title', 
args={'paperTitle': 'Construction of the Literature Graph in
Semantic Scholar', 'fields': 'title,abstract,authors,year,
citationCount,paperId'}, result={'total': 1, 'offset': 0,
'data': [{'paperId': '649def34f8be52c8b66281af98ae884c09aef38b',
'title': 'Construction of the Literature Graph in Semantic
 Scholar', 'abstract': 'We describe a deployed scalable system
for organizing published scientific literature into a 
heterogeneous graph to facilitate algorithmic manipulation and 
discovery. The resulting literature graph consists of more than
 280M nodes, representing papers, authors, entities and various
 interactions between them (e.g., authorships, citations, 
 entity mentions). We reduce literature graph construction into
 familiar NLP tasks (e.g., entity extraction and linking),
 point out research challenges due to differences from standard
 formulations of these tasks, and report empirical results for
 each task. The methods describe
================================================================
'''

# Search a paper through its title
usr_msg = """search the paper with paper id of 
    '649def34f8be52c8b66281af98ae884c09aef38b' for me"""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_paper_data_id', args=
{'paperID': '649def34f8be52c8b66281af98ae884c09aef38b', 
'fields': 'title,abstract,authors,year,citationCount,
publicationTypes,publicationDate,openAccessPdf'}, 
result={'paperId': '649def34f8be52c8b66281af98ae884c09aef38b',
'title': 'Construction of the Literature Graph in Semantic
 Scholar', 'abstract': 'We describe a deployed scalable system
 for organizing published scientific literature into a
 heterogeneous graph to facilitate algorithmic manipulation
 and discovery. The resulting literature graph consists of 
 more than 280M nodes, representing papers, authors, entities
 and various interactions between them (e.g., authorships,
 citations, entity mentions). We reduce literature graph
 construction into familiar NLP tasks (e.g., entity extraction
 and linking), point out research challenges due to differences
 from standard formulations of these tasks, and report
 empirical results for each task. The methods described
 in this paper ar
================================================================
'''

# Search papers through related topic
usr_msg = """search 3 papers with topic related to
    'generative ai' from 2024 for me"""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_bulk_paper_data', 
args={'query': 'generative ai', 'year': '2024-', 'fields':
'title,url,publicationTypes,publicationDate,openAccessPdf'},
result={'total': 9849, 'token': 'PCOA3RZZB2ADADAEYCX2BLJJRDEGL
PUCFA3I5XJAKEAB3YXPGDOTY2GU3WHI4ZMALUMAPUDPHP724CEUVEFKTYRZY5K
LUU53Y5MWWEINIKYZZRC3YT3H4AF7CTSQ', 'data': [{'paperId': 
'0008cd09c0449451b9e6e6de35c29009f0883cd9', 'url': 'https://www
.semanticscholar.org/paper/0008cd09c0449451b9e6e6de35c29009
f0883cd9', 'title': 'A Chitchat on Using ChatGPT for Cheating',
 'openAccessPdf': {'url': 'https://doi.org/10.34074/proc.240106'
 , 'status': 'BRONZE'}, 'publicationTypes': ['Conference'], 
 'publicationDate': '2024-07-24'}, {'paperId': '0013aecf813400
 174158e4f012918c5408f90962', 'url': 'https://www.semanticsc
 holar.org/paper/0013aecf813400174158e4f012918c5408f90962', 
 'title': 'Can novice teachers detect AI-generated texts in EFL
 writing?', 'openAccessPdf': None, 'publicationTypes':
 ['JournalArticle'], 'publicationDate'
================================================================
'''

# Search papers through related topic and operator
usr_msg = """search 2 papers with topic related to
    'ai and bio' from 2024 for me"""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_bulk_paper_data', 
args={'query': 'ai and bio', 'year': '2024-', 'fields': 'title,
url,publicationTypes,publicationDate,openAccessPdf'}, result=
{'total': 207, 'token': None, 'data': [{'paperId': '00c8477a9c
c28b85e4f6da13d2a889c94a955291', 'url': 'https://www.semantics
cholar.org/paper/00c8477a9cc28b85e4f6da13d2a889c94a955291', 
'title': 'Explaining Enterprise Knowledge Graphs with Large
 Language Models and Ontological Reasoning', 'openAccessPdf': 
 None, 'publicationTypes': ['JournalArticle'], 'publicationDate
 ': None}, {'paperId': '01726fbfc8ee716c82b9c4cd70696906d3a4
 46d0', 'url': 'https://www.semanticscholar.org/paper/01726fbfc
 8ee716c82b9c4cd70696906d3a446d0', 'title': 'Study Research 
 Protocol for Phenome India-CSIR Health Cohort Knowledgebase
 (PI-CHeCK): A Prospective multi-modal follow-up study on a 
 nationwide employee cohort.', 'openAccessPdf': {'url': 
 'https://www.medrxiv.org/content/medrxiv/early/2024/10/19/2024
 .10.17.24315252.full.pdf', 'status'
================================================================
'''

# Recommend papers through positive and negative paper id
usr_msg = """recommend 2 papers with positive paper id
    of "02138d6d094d1e7511c157f0b1a3dd4e5b20ebee",
    "018f58247a20ec6b3256fd3119f57980a6f37748" and negative
    paper id of "0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc"
    for me"""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_recommended_papers',
args={'positive_paper_ids': ['02138d6d094d1e7511c157f0b1a3dd4e
5b20ebee', '018f58247a20ec6b3256fd3119f57980a6f37748'], 'negati
ve_paper_ids': ['0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc'], 
'fields': 'title,url,citationCount,authors,publicationTypes,
publicationDate,openAccessPdf', 'limit': 20, 'save_to_file': F
alse}, result={'recommendedPapers': [{'paperId': '9cb202a72171
dc954f8180b42e08da7ab31e16a1', 'url': 'https://www.semanticsc
holar.org/paper/9cb202a72171dc954f8180b42e08da7ab31e16a1', 'tit
le': 'Embrace, Don't Avoid: Reimagining Higher Education with
 Generative Artificial Intelligence', 'citationCount': 0, 'op
 enAccessPdf': {'url': 'https://heca-analitika.com/jeml/arti
 cle/download/233/157', 'status': 'HYBRID'}, 'publicationT
 ypes': ['JournalArticle'], 'publicationDate': '2024-11-2
 8', 'authors': [{'authorId': '1659371967', 'name': 'T. R. N
 oviandy'}, {'authorId': '1657989613', 'name': 'A. Maulan
 a'}, {'authorId': '146805414', 'name
================================================================
'''

# Recommend papers and save the result in a file
usr_msg = """search the authors of author ids of "2281351310",
    "2281342663","2300302076","2300141520" for me"""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_recommended_papers', 
args={'positive_paper_ids': ['02138d6d094d1e7511c157f0b1a3dd4e5
b20ebee', '018f58247a20ec6b3256fd3119f57980a6f37748'], 'negativ
e_paper_ids': ['0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc'],
 'fields': 'title,url,citationCount,authors,publicationTypes,
 publicationDate,openAccessPdf', 'limit': 20, 'save_to_file': T
 rue}, result={'recommendedPapers': [{'paperId': '9cb202a7217
 1dc954f8180b42e08da7ab31e16a1', 'url': 'https://www.semantics
 cholar.org/paper/9cb202a72171dc954f8180b42e08da7ab31e16a1', 
 'title': 'Embrace, Don't Avoid: Reimagining Higher Education
 with Generative Artificial Intelligence', 'citationCount':
 0, 'openAccessPdf': {'url': 'https://heca-analitika.com/jeml
 /article/download/233/157', 'status': 'HYBRID'}, 'publication
 Types': ['JournalArticle'], 'publicationDate': '2024-11-28',
 'authors': [{'authorId': '1659371967', 'name': 'T. R. Novia
 ndy'}, {'authorId': '1657989613', 'name': 'A. Maulana'}, 
 {'authorId': '146805414', 'name'
================================================================
'''

# Search author information through author id
usr_msg = """recommend 2 papers with positive paper id
    of "02138d6d094d1e7511c157f0b1a3dd4e5b20ebee", "018f5
    8247a20ec6b3256fd3119f57980a6f37748" and negative paper
    id of "0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc" for me,
    and please save the result in a file."""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_recommended_papers', 
args={'positive_paper_ids': ['02138d6d094d1e7511c157f0b1a3dd4e5
b20ebee', '018f58247a20ec6b3256fd3119f57980a6f37748'], 'negat
ive_paper_ids': ['0045ad0c1e14a4d1f4b011c92eb36b8df63d65bc'],
 'fields': 'title,url,citationCount,authors,publicationTypes
 ,publicationDate,openAccessPdf', 'limit': 20, 'save_to_file
 ': True}, result={'recommendedPapers': [{'paperId': '9cb20
 2a72171dc954f8180b42e08da7ab31e16a1', 'url': 'https://www.se
 manticscholar.org/paper/9cb202a72171dc954f8180b42e08da7ab31e
 16a1', 'title': 'Embrace, Don't Avoid: Reimagining Higher 
 Education with Generative Artificial Intelligence', 'citat
 ionCount': 0, 'openAccessPdf': {'url': 'https://heca-anali
 tika.com/jeml/article/download/233/157', 'status': 'HYBR
 ID'}, 'publicationTypes': ['JournalArticle'], 'publicatio
 nDate': '2024-11-28', 'authors': [{'authorId': '165937196
 7', 'name': 'T. R. Noviandy'}, {'authorId': '1657989613',
 'name': 'A. Maulana'}, {'authorId': '146805414', 'name'
================================================================
'''

# Search author information and save the result in a file
usr_msg = """search the authors of author ids of "2281351310"
    ,"2281342663","2300302076","2300141520" for me, and please
    save the record in a file."""
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])

'''
================================================================
[FunctionCallingRecord(func_name='fetch_author_data', args=
{'ids': ['2281351310', '2281342663', '2300302076', '230014152
0'], 'fields': 'name,url,paperCount,hIndex,papers', 'save_to_
file': True}, result=[{'authorId': '2281351310', 'url': 'ht
tps://www.semanticscholar.org/author/2281351310', 'name': 'Tho
mas K. F. Chiu', 'paperCount': 3, 'hIndex': 1, 'papers': [{'p
aperId': '218b2e3d3418edff705336a6e0c7f2125be7c562', 'title': N
one}, {'paperId': '630642b7040a0c396967e4dab93cf73094fa4f8f
', 'title': None}, {'paperId': '833ff07d2d1be9be7b12e88487d5631
c141a2e95', 'title': None}]}, {'authorId': '2281342663', 'ur
l': 'https://www.semanticscholar.org/author/2281342663', 'nam
e': 'C. Chai', 'paperCount': 6, 'hIndex': 2, 'papers': [{'pape
rId': '0c70ca68c0239895b0d36abf7f11302cdcf01855', 'title': Non
e}, {'paperId': '218b2e3d3418edff705336a6e0c7f2125be7c562', 't
itle': None}, {'paperId': '7ce699e1cfb81cecf298df6be8eaac8f50
2e0fcc', 'title': None}, {'paperId': '4521b51a8465e69d20a3ae4
b770cf164a180f67b', 'ti
================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\sympy_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import SymPyToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = """You are a helpful math assistant that can perform symbolic 
computations"""

# Set model config
tools = SymPyToolkit().get_tools()
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message with a complex expression
usr_msg = """Simplify the expression: (x^4 - 16)/(x^2 - 4) + sin(x)^2 + cos(x)
^2 + (x^3 + 6*x^2 + 12*x + 8)/(x + 2)"""

# Get response information
response = camel_agent.step(usr_msg)
print(response.info['tool_calls'])
'''
===============================================================================
[ToolCallingRecord(tool_name='simplify_expression', args={'expression': '(x**4 
- 16)/(x**2 - 4) + sin(x)**2 + cos(x)**2 + (x**3 + 6*x**2 + 12*x + 8)/(x + 2)
'}, result='{"status": "success", "result": "2*x**2 + 4*x + 9"}', 
tool_call_id='call_CdoZsLWeagT0yBM13RYuz09W')]
===============================================================================
'''



--------------------------------------------------------------------------------
# File: toolkits\synthesize_function_execution.py
--------------------------------------------------------------------------------

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

from typing import Any, Dict

import requests
from pydantic import BaseModel, Field

from camel.agents import ChatAgent
from camel.toolkits import FunctionTool


# example function
def movie_data_by_id(id: int) -> Dict[str, Any]:
    r"""Fetch movie data by its ID from the IMDB Top 100 Movies API.

    Args:
        id (int): The ID of the movie to retrieve information for.

    Returns:
        Dict[str, Any]: A dictionary with the following keys:
            - rank (int): The rank of the movie in the top 100 list.
            - movie_title (str): The title of the movie.
            - rating (str): The movie's rating.
            - id (str): The unique identifier of the movie.
            - year (int): The release year of the movie.
            - description (str): A brief description of the movie.

    Raises:
        Exception: If an unexpected error occurs while fetching the data.
    """
    try:
        url = f"https://imdb-top-100-movies.p.rapidapi.com/{id}"
        headers = {
            "x-rapidapi-key": "Your API Key",
            "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        return {
            "error": str(e),
        }


# Define the response format for movie data
class MovieResponse(BaseModel):
    rating: str = Field(description="The movie's rating.")
    description: str = Field(description="A brief description of the movie.")
    movie_title: str = Field(description="The title of the movie.")


real_get_movie = FunctionTool(movie_data_by_id)
synthesized_get_movie = FunctionTool(movie_data_by_id, synthesize_output=True)

assistant_sys_msg = "You are a helpful assistant."
user_msg = (
    "What is the rating, description and movie_title of the movie with id 2048"
)

print("Synthesize output: False")
real_agent = ChatAgent(assistant_sys_msg, tools=[real_get_movie])
assistant_response = real_agent.step(user_msg)
print(assistant_response.msg.content)


print("\nSynthesize output: True")
synthesized_agent = ChatAgent(assistant_sys_msg, tools=[synthesized_get_movie])
assistant_response = synthesized_agent.step(
    user_msg, response_format=MovieResponse
)
print(assistant_response.msg.content)

"""
===============================================================================
Warning: No synthesize_output_model provided. Use `gpt-4o-mini` to synthesize 
the output.
Synthesize output: False
It seems that I'm unable to access the movie data at the moment due to a 
subscription issue with the API. However, if you provide me with the title of 
the movie or any other details, I can help you find information about it!
===============================================================================
"""

"""
===============================================================================
Synthesize output: True
{'rating': '8.8', 'description': 'A thief who steals corporate secrets through 
the use of dream-sharing technology is given the inverse task of planting an 
idea into the mind of a CEO.', 'movie_title': 'Inception'}
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\terminal_toolkit.py
--------------------------------------------------------------------------------

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

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import TerminalToolkit
from camel.types import ModelPlatformType, ModelType

# Get current script directory
base_dir = os.path.dirname(os.path.abspath(__file__))
# Define workspace directory for the toolkit
workspace_dir = os.path.join(
    os.path.dirname(os.path.dirname(base_dir)), "workspace"
)

# Define system message
sys_msg = (
    "You are a System Administrator helping with log management tasks. "
    "You have access to terminal tools that can help you execute "
    "shell commands and search files. "
)

# Set model config
tools = TerminalToolkit(working_dir=workspace_dir).get_tools()

model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# Define a user message for creating logs directory
usr_msg = (
    f"Create a 'logs' directory in '{workspace_dir}' and list its contents"
)

# Get response information
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(tool_name='shell_exec', args={'id': 'session1', 'exec_dir': 
'/Users/enrei/Desktop/camel0302/camel/workspace', 'command': 'mkdir logs'}, 
result='', tool_call_id='call_ekWtDhrwxOg20lz55pqLEKvm'), ToolCallingRecord
(tool_name='shell_exec', args={'id': 'session2', 'exec_dir': '/Users/enrei/
Desktop/camel0302/camel/workspace/logs', 'command': 'ls -la'}, result='total 
0\ndrwxr-xr-x  2 enrei  staff   64 Mar 30 04:29 .\ndrwxr-xr-x  4 enrei  staff  
128 Mar 30 04:29 ..\n', tool_call_id='call_FNdkLkvUahtEZUf7YZiJrjfo')]
===============================================================================
"""

# Define a user message for creating log files
usr_msg = (
    f"Create 'app.log' in the logs directory at "
    f"'{os.path.join(workspace_dir, 'logs')}' with content: INFO: Application "
    f"started successfully at 2024-03-10 and show the file content"
)

# Get response information
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(tool_name='shell_exec', args={'id': 'create_log_file', 
'exec_dir': '/Users/enrei/Desktop/camel0302/camel/workspace/logs', 'command': 
"echo 'INFO: Application started successfully at 2024-03-10' > app.log"}, 
result='', tool_call_id='call_bctQQYnWgAuPp1ga7a7xM6bo'), ToolCallingRecord
(tool_name='shell_exec', args={'id': 'show_log_file_content', 'exec_dir': '/
Users/enrei/Desktop/camel0302/camel/workspace/logs', 'command': 'cat app.
log'}, result='INFO: Application started successfully at 2024-03-10\n', 
tool_call_id='call_wPYJBG3eYrUsjFJYIYYynxuz')]
===============================================================================
"""

# Define a user message for searching in logs
usr_msg = (
    f"Search for 'INFO' keyword in the log file at "
    f"'{os.path.join(workspace_dir, 'logs', 'app.log')}'"
)

# Get response information
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(tool_name='file_find_in_content', args={'file': '/Users/
enrei/Desktop/camel0302/camel/workspace/logs/app.log', 'regex': 'INFO', 
'sudo': False}, result='INFO: Application started successfully at 2024-03-10',
 tool_call_id='call_PpeRUsldHyg5jSPLZxiGoVfq')]
===============================================================================
"""

# Define a user message for cleaning up logs
usr_msg = (
    f"Remove the 'logs' directory and all its contents in '{workspace_dir}'"
)

# Get response information
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(response.info['tool_calls'])
"""
===============================================================================
[ToolCallingRecord(tool_name='shell_exec', args={'id': 'remove_logs', 
'exec_dir': '/Users/enrei/Desktop/camel0302/camel/workspace', 'command': 'rm 
-rf logs'}, result='', tool_call_id='call_A2kUkVIAhkD9flWmmpTlS9FA')]
===============================================================================
"""

# Define a user message for find the content of the log file
usr_msg = "Find all the files under path `examples/bots`"

# Get response information
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(response.info['tool_calls'])
"""
===============================================================================
[ToolCallingRecord(tool_name='file_find_by_name', args={'path': 'examples/
bots', 'glob': '*'}, result='examples/bots\nexamples/bots/discord_bot.
py\nexamples/bots/discord_bot_installation_management.py\nexamples/bots/
slack_bot_use_msg_queue.py\nexamples/bots/discord_bot_use_msg_queue.
py\nexamples/bots/slack_bot.py', tool_call_id='call_LzRjSotNqKOWwU4yHcstlnG9')]
===============================================================================
"""

# Define a user message for testing resource cleanup via __del__ method
print("\n\n================ Testing Resource Cleanup ================")
usr_msg = (
    "Start a long-running process that sleeps for 300 seconds in the "
    "background, then show me the list of running processes"
)


# Get response information for starting the process
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(tool_name='shell_exec', args={'id': 'session1', 'exec_dir': 
'/tmp', 'command': 'sleep 300 & echo $!'}, result='Operation restriction: 
Execution path /tmp must be within working directory /home/jjyaoao/openSource/
camel/workspace', tool_call_id='call_G7TcVUJs195Er6yocORHysXP'), 
ToolCallingRecord(tool_name='shell_exec', args={'id': 'session1', 'exec_dir': 
'/home/jjyaoao/openSource/camel/workspace', 'command': 'sleep 300 & echo $!'}, 
result='10804\n', tool_call_id='call_mncQosy3b4cuc1j5MGiltohH'), 
ToolCallingRecord(tool_name='shell_exec', args={'id': 'session2', 'exec_dir': 
'/home/jjyaoao/openSource/camel/workspace', 'command': 'ps aux'}, 
result='USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME 
COMMAND\nroot           1  0.0  0.2 170104 12368 ?        Ss   10:06   0:00 
/sbin/init\nroot           2  0.0  0.0   2776  1928 ?        Sl   10:06   0:00 
/init\nroot           8  0.0  0.0   2776     4 ?        Sl   10:06   0:00 
plan9 --control-socket 7 --log-level=debug --log-file=/dev/null ...',
tool_call_id='call_UvxQrsb1GpfDHTQQc6rLoQ3P')]
===============================================================================
"""
# Define a user message to check if the process was terminated by __del__
usr_msg = "Check if there are any sleep processes running on the system"

# Get response information for checking the processes
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls'])[:1000])
"""
===============================================================================
[ToolCallingRecord(tool_name='shell_exec', args={'id': 'check_sleep_processes',
'exec_dir': '/', 'command': 'ps aux | grep sleep'}, result='Operation 
restriction: Execution path / must be within working directory 
/home/jjyaoao/openSource/camel/workspace', tool_call_id=
'call_gbhmZ3mwpB07uPtVF3FxZaHu'), ToolCallingRecord(tool_name='shell_exec',
args={'id': 'check_sleep_processes', 'exec_dir': 
'/home/jjyaoao/openSource/camel/workspace', 'command': 'ps aux | grep sleep'}, 
result='root       11385  0.0  0.0   2620   532 pts/4    S+   11:16   0:00 
/bin/sh -c ps aux | grep sleep\nroot       11387  0.0  0.0   8172   656 pts/4  
S+   11:16   0:00 grep sleep\n', tool_call_id='call_gSZqRaqNAtYjUXOfvVuaObw2')]
===============================================================================
"""

usr_msg = "help me use uv pip install pptx, and create a ppt, and show me the"
" output of the terminal"

# Get response information for checking the processes
camel_agent.reset()
response = camel_agent.step(usr_msg)
print(str(response.info['tool_calls']))



--------------------------------------------------------------------------------
# File: toolkits\thinking_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import ThinkingToolkit
from camel.types import ModelPlatformType, ModelType

# Create a Model
model_config_dict = ChatGPTConfig(temperature=0.0).as_dict()
model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Initialize the ThinkingToolkit
thinking_toolkit = ThinkingToolkit()
tools = thinking_toolkit.get_tools()

# Set up the ChatAgent with thinking capabilities
sys_msg = (
    "You are an assistant that can break down complex problems and think "
    "through solutions step by step. Use the thinking toolkit to organize "
    "your thoughts, reflect on the problem, and create plans."
)

agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)

# Example: Problem solving with thinking toolkit
print("\nExample: Problem solving with thinking toolkit")
print("=" * 80)

usr_msg = """
Help me solve this math problem:
If a train travels at 60 mph and needs to cover 300 miles, 
with 3 stops of 15 minutes each, how long will the journey take?
"""

response = agent.step(usr_msg)
print(response.msgs[0].content)
print("\nTool calls:")
print(response.info['tool_calls'])

"""
Example: Problem Solving with Thinking Toolkit
===============================================================================
The train's total journey time for traveling 300 miles at 60 mph, with 
3 stops of 15 minutes each, is 5.75 hours. This consists of 5 hours of 
travel time and 0.75 hours (or 45 minutes) of stop time. The conversion 
of stop time from minutes to hours was explicitly noted for clarity.

Tool Calls:
[
    ToolCallingRecord(
        tool_name='plan',
        args={
            'plan': '1. Compute the travel time for 300 miles at 60 mph '
                    'without stops.\n'
                    '2. Determine the total stop time.\n'
                    '3. Sum the travel time and stop time to get the total '
                    'journey duration.'
        },
        result='Plan: 1. Compute the travel time for 300 miles at 60 mph '
               'without stops.\n'
               '2. Determine the total stop time.\n'
               '3. Sum the travel time and stop time to get the total journey '
               'duration.',
        tool_call_id='call_kKYeTFLMGPf0mhimAZ8hapFk'
    ),
    ToolCallingRecord(
        tool_name='think',
        args={
            'thought': 'Using the formula time = distance / speed, where '
                       'distance = 300 miles and speed = 60 mph, we can '
                       'determine the travel time.'
        },
        result='Thought: Using the formula time = distance / speed, where '
               'distance = 300 miles and speed = 60 mph, we can determine '
               'the travel time.',
        tool_call_id='call_t3DXWahikwhc8ps0y2GTE9ko'
    ),
    ToolCallingRecord(
        tool_name='think',
        args={
            'thought': 'The total stop time is calculated as: number of '
                       'stops * time per stop, which is 3 * 15 minutes.'
        },
        result='Thought: The total stop time is calculated as: number of '
               'stops * time per stop, which is 3 * 15 minutes.',
        tool_call_id='call_MM1YlTPmiMhhiy6HWqraKh8E'
    ),
    ToolCallingRecord(
        tool_name='hypothesize',
        args={
            'hypothesis': 'The travel time for 300 miles at 60 mph should '
                          'be 5 hours.'
        },
        result='Hypothesis: The travel time for 300 miles at 60 mph should '
               'be 5 hours.',
        tool_call_id='call_F16dfESrJmUDwieYDA2aCheB'
    ),
    ToolCallingRecord(
        tool_name='hypothesize',
        args={
            'hypothesis': 'The total stop time for 3 stops of 15 minutes '
                          'each should be 45 minutes.'
        },
        result='Hypothesis: The total stop time for 3 stops of 15 minutes '
               'each should be 45 minutes.',
        tool_call_id='call_coxWcLPATfKNdiqQDz853pm4'
    ),
    ToolCallingRecord(
        tool_name='synthesize',
        args={
            'synthesis': 'The total journey time for the train traveling '
                         '300 miles at 60 mph, with 3 stops of 15 minutes '
                         'each, is 5.75 hours. This includes 5 hours of '
                         'travel time and 0.75 hours (or 45 minutes) of '
                         'stop time. The conversion of stop time from '
                         'minutes to hours was explicitly noted for clarity.'
        },
        result='Synthesis: The total journey time for the train traveling '
               '300 miles at 60 mph, with 3 stops of 15 minutes each, is '
               '5.75 hours. This includes 5 hours of travel time and 0.75 '
               'hours (or 45 minutes) of stop time. The conversion of stop '
               'time from minutes to hours was explicitly noted for clarity.',
        tool_call_id='call_9AHg54snm17XN7Mj1UzgSV04'
    )
]
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\toolkit_timeout.py
--------------------------------------------------------------------------------

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

import time
from typing import Optional

from camel.toolkits.base import BaseToolkit
from camel.utils import with_timeout


# Example 1: Basic function with timeout
@with_timeout(1.0)
def basic_function() -> str:
    r"""A basic function with a 1-second timeout."""
    time.sleep(0.5)  # Simulating some work
    return "Basic function completed successfully!"


# Example 2: Function that exceeds timeout
@with_timeout(1.0)
def slow_function() -> str:
    r"""A slow function that will exceed the timeout."""
    time.sleep(2.0)  # This will exceed the timeout
    return "This message will never be returned"


# Example 3: Class with configurable timeout
class TimeoutExample:
    def __init__(self, timeout: Optional[float] = None):
        self.timeout = timeout

    @with_timeout()  # Uses instance timeout
    def instance_timeout_method(self) -> str:
        r"""Method using the instance's timeout value."""
        time.sleep(0.5)
        return "Instance timeout method completed!"

    @with_timeout(0.1)  # Uses decorator-specific timeout
    def decorator_timeout_method(self) -> str:
        r"""Method using the decorator's timeout value."""
        time.sleep(0.5)
        return "This will timeout"


# Example 4: Toolkit with timeout
class TimeoutToolkit(BaseToolkit):
    def __init__(self, timeout: Optional[float] = None):
        super().__init__(timeout=timeout)

    @with_timeout()
    def fast_operation(self) -> str:
        r"""A fast operation that completes within timeout."""
        time.sleep(0.1)
        return "Fast operation completed!"

    @with_timeout()
    def slow_operation(self) -> str:
        r"""A slow operation that exceeds timeout."""
        time.sleep(1.0)
        return "Slow operation completed!"


def main():
    # Example 1: Basic function
    print("\nExample 1: Basic function")
    print(basic_function())

    # Example 2: Slow function
    print("\nExample 2: Slow function")
    print(slow_function())

    # Example 3: Class with timeout
    print("\nExample 3: Class with timeout")
    example = TimeoutExample(timeout=0.2)
    print(example.instance_timeout_method())
    print(example.decorator_timeout_method())

    # Example 4: Toolkit
    print("\nExample 4: Toolkit with timeout")
    toolkit = TimeoutToolkit(timeout=0.5)
    print(toolkit.fast_operation())
    print(toolkit.slow_operation())


if __name__ == "__main__":
    main()

"""
===============================================================================
Example 1: Basic function
Basic function completed successfully!

Example 2: Slow function
Function `slow_function` execution timed out, exceeded 1.0 seconds.

Example 3: Class with timeout
Function `instance_timeout_method` execution timed out, exceeded 0.2 seconds.
Function `decorator_timeout_method` execution timed out, exceeded 0.1 seconds.

Example 4: Toolkit with timeout
Fast operation completed!
Function `slow_operation` execution timed out, exceeded 0.5 seconds.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\video_analysis_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import VideoAnalysisToolkit
from camel.types import ModelPlatformType, ModelType

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

video_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0,
    ).as_dict(),
)

# Initialize the VideoAnalysisToolkit with the model
# Note: Audio transcription is disabled for faster processing
video_toolkit = VideoAnalysisToolkit(
    model=video_model,
    use_audio_transcription=False,
)

# Create an agent with the video toolkit's tools
agent = ChatAgent(
    system_message="You are a helpful assistant that can analyze videos.",
    model=model,
    tools=[*video_toolkit.get_tools()],
)

# Example video URL (Very short sample video)
video_url = "https://www.youtube.com/watch?v=kQ_7GtE529M"
question = "What is shown in the first few seconds of this video?"

# Use the toolkit directly for faster processing with fewer frames
print("Analyzing video...")
result = video_toolkit.ask_question_about_video(
    video_path=video_url,
    question=question,
    num_frames=5,  # Extract only 5 frames for faster processing
)

print("Video Analysis Result:")
print("-" * 50)
print(result)
print("-" * 50)
"""
==========================================================================
Analyzing video...
[youtube] Extracting URL: https://www.youtube.com/watch?v=kQ_7GtE529M
[youtube] kQ_7GtE529M: Downloading webpage
[youtube] kQ_7GtE529M: Downloading ios player API JSON
[youtube] kQ_7GtE529M: Downloading mweb player API JSON
[youtube] kQ_7GtE529M: Downloading m3u8 information
[info] kQ_7GtE529M: Downloading 1 format(s): 247+251
[download] Destination: /private/var/folders/93/f_71_t957cq9cmq2gsybs4_40000gn/
T/tmp4plhd3s3/Douchebag Bison.f247.webm
[download] 100% of    1.95MiB in 00:00:01 at 1.18MiB/s
[download] Destination: /private/var/folders/93/f_71_t957cq9cmq2gsybs4_40000gn/
T/tmp4plhd3s3/Douchebag Bison.f251.webm
[download] 100% of  303.08KiB in 00:00:00 at 490.62KiB/s
[Merger] Merging formats into "/private/var/folders/93/
f_71_t957cq9cmq2gsybs4_40000gn/T/tmp4plhd3s3/Douchebag Bison.webm"
Deleting original file /private/var/folders/93/f_71_t957cq9cmq2gsybs4_40000gn/
T/tmp4plhd3s3/Douchebag Bison.f251.webm (pass -k to keep)
Deleting original file /private/var/folders/93/f_71_t957cq9cmq2gsybs4_40000gn/
T/tmp4plhd3s3/Douchebag Bison.f247.webm (pass -k to keep)
2025-03-09 21:17:08,036 - pyscenedetect - ERROR - VideoManager is deprecated 
and will be removed.
2025-03-09 21:17:08,060 - pyscenedetect - INFO - Loaded 1 video, framerate: 30.
000 FPS, resolution: 1280 x 720
2025-03-09 21:17:08,061 - pyscenedetect - INFO - Duration set, start: None, 
duration: None, end: None.
2025-03-09 21:17:08,061 - pyscenedetect - INFO - Detecting scenes...
2025-03-09 21:17:09,065 - camel.camel.toolkits.video_analysis_toolkit - 
WARNING - No scenes detected in video, capturing frames at regular intervals
Video Analysis Result:
--------------------------------------------------
### Visual Analysis

1. **Identified Entities**:
   - **Wolves**: Multiple wolves are visible in the frames, characterized by 
   their grayish fur, slender bodies, and bushy tails. They appear to be in a 
   pack, indicating social behavior.
   - **Bison**: A bison is present, identifiable by its large size, shaggy 
   brown fur, and distinctive hump on its back. The bison is significantly 
   larger than the wolves.

2. **Key Attributes**:
   - **Wolves**: 
     - Size: Smaller than the bison, typically around 26-32 inches tall at the 
     shoulder.
     - Color: Predominantly gray with some variations in fur color.
     - Behavior: The wolves are shown moving in a coordinated manner, 
     suggesting they are hunting or scavenging.
   - **Bison**:
     - Size: Much larger, can weigh up to 2,000 pounds.
     - Color: Dark brown, with a thick coat.
     - Behavior: The bison appears to be stationary or moving slowly, possibly 
     in a defensive posture.

3. **Groupings and Interactions**:
   - The wolves are seen surrounding the bison, indicating a predatory 
   behavior. The interaction suggests a hunting scenario, where the wolves are 
   attempting to take down or scavenge from the bison.

### Audio Integration
- **No audio transcription available**: Therefore, the analysis relies solely 
on visual observations.

### Detailed Reasoning and Justification
- **Identification of Species**:
  - The wolves are identified by their physical characteristics and social 
  behavior, which is typical of pack animals. Their movement patterns and 
  proximity to the bison indicate a hunting strategy.
  - The bison is easily distinguishable due to its size and unique physical 
  features, such as the hump and thick fur.

### Comprehensive Answer
- **Total Number of Distinct Species**: 2 (Wolves and Bison)
- **Defining Characteristics**:
  - **Wolves**: Gray fur, slender build, social behavior in a pack.
  - **Bison**: Large size, shaggy brown fur, distinctive hump.

### Important Considerations
- The wolves exhibit coordinated movement, which is crucial for hunting, while 
the bison's size and defensive posture highlight its role as prey in this 
scenario. The visual cues of size, color, and behavior effectively distinguish 
these two species in the context of a predatory interaction.
==========================================================================
"""



--------------------------------------------------------------------------------
# File: toolkits\zapier_toolkit.py
--------------------------------------------------------------------------------

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
from camel.configs.openai_config import ChatGPTConfig
from camel.models import ModelFactory
from camel.toolkits import ZapierToolkit
from camel.types import ModelPlatformType, ModelType

# Define system message
sys_msg = """You are a helpful AI assistant that can use Zapier AI tools to 
perform various tasks. When using tools, first list the available tools using 
list_actions, then use the appropriate tool based on the task. Always provide 
clear explanations of what you're doing."""

# Set model config
tools = ZapierToolkit().get_tools()
model_config_dict = ChatGPTConfig(
    temperature=0.0,
).as_dict()


model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
    model_config_dict=model_config_dict,
)

# Set agent
camel_agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    tools=tools,
)
camel_agent.reset()

# First, list available tools
usr_msg = "First, list all available Zapier tools."
response = camel_agent.step(usr_msg)
print("Available Tools:")
print(response.msg.content)
print("\n" + "=" * 80 + "\n")

# Now, use the translation tool
usr_msg = """Now that we can see the translation tool is available, please 
use it to translate 'hello camel' from en to zh. Use 
the tool ID from the list above and make sure to specify the language codes 
correctly in the instructions."""
response = camel_agent.step(usr_msg)
print("Translation Result:")
print(response.msg.content)

"""
===============================================================================
Here are the available Zapier tools:

1. **Gmail: Find Email**
   - **ID:** 0d82cfd3-2bd7-4e08-9f3d-692719e81a26
   - **Description:** This action allows you to find an email in Gmail based 
        on a search string.
   - **Parameters:**
     - `instructions`: Instructions for executing the action.
     - `Search_String`: The string to search for in the emails.

2. **Translate by Zapier: Translate Text**
   - **ID:** f7527450-d7c7-401f-a764-2f69f622e7f3
   - **Description:** This action translates text into a specified target 
        language.
   - **Parameters:**
     - `instructions`: Instructions for executing the action.
     - `Text`: The text to be translated.
     - `Target_Language`: The language to translate the text into.

If you need to perform a specific task using one of these tools, please let me 
know!

================================================================================

Translation Result:
The translation of "hello camel" from English to Chinese (zh) is:

**Translation:** 你好骆驼

- **Source Language:** English (en)
- **Target Language:** Chinese (zh)

If you need any further assistance or additional translations, feel free to 
ask!
===============================================================================
"""



--------------------------------------------------------------------------------
# File: translation\translator.py
--------------------------------------------------------------------------------

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
import argparse
import codecs
import json
import multiprocessing
import os
import os.path as osp
import warnings

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.generators import SystemMessageGenerator
from camel.models import ModelFactory
from camel.types import (
    ModelPlatformType,
    ModelType,
    RoleType,
    TaskType,
)

warnings.filterwarnings("ignore")

language_list = [
    "arabic",
    "chinese",
    "french",
    "german",
    "hindi",
    "italian",
    "japanese",
    "korean",
    "russian",
    "spanish",
]

parser = argparse.ArgumentParser(description='Arguments for translation.')
parser.add_argument(
    '--directory_path',
    type=str,
    help='Directory that contains original json files',
    default='../camel_data/ai_society',
)
parser.add_argument(
    '--save_directory_path',
    type=str,
    help='Directory to save translated files',
    default='../camel_data/ai_society_translated',
)
parser.add_argument(
    '--single',
    action='store_true',
    help='Run translator in a non-parallel way.',
)
parser.add_argument(
    '--stream',
    action='store_true',
    help='Set OpenAI GPT model with the stream mode.',
)
parser.add_argument(
    '--language',
    type=str,
    help='Language you want to translated to. '
    'Notice that this is not used in the parallel mode, '
    'which uses SLURM_ARRAY_TASK_ID to indicate the '
    'language to be translated.',
    choices=language_list,
    default='arabic',
)


def translate_content(
    args: argparse.Namespace, file_path: str, language: str
) -> None:
    # Extract file name from the .json file path to be translated
    file_name = osp.splitext(osp.basename(file_path))[0]

    if not osp.exists(args.save_directory_path):
        os.makedirs(args.save_directory_path)

    save_lang_director_path = osp.join(args.save_directory_path, language)
    if not osp.exists(save_lang_director_path):
        os.makedirs(save_lang_director_path)

    # Check that file_name.json does not exist in the save directory
    save_path = osp.join(save_lang_director_path, f'{file_name}.json')
    if osp.exists(save_path):
        return

    # Load the json file
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)

    # Translate the content of each message in the json
    for i in range(json_data['num_messages']):
        msg_i_content = (
            "Sentence to translate: " + json_data[f"message_{i+1}"]["content"]
        )

        sys_msg_generator = SystemMessageGenerator(
            task_type=TaskType.TRANSLATION
        )

        assistant_sys_msg = sys_msg_generator.from_dict(
            meta_dict=dict(language=language.capitalize()),
            role_tuple=('Language Translator', RoleType.ASSISTANT),
        )

        if not args.stream:
            model_config = ChatGPTConfig(stream=False)
        else:
            model_config = ChatGPTConfig(stream=True)

        model = ModelFactory.create(
            model_platform=ModelPlatformType.DEFAULT,
            model_type=ModelType.DEFAULT,
            model_config=model_config,
        )

        assistant_agent = ChatAgent(
            system_message=assistant_sys_msg,
            model=model,
        )

        user_msg = msg_i_content

        assistant_response = assistant_agent.step(user_msg)
        assistant_msg = assistant_response.msg

        json_data[f"message_{i+1}"]["content"] = assistant_msg.content

    with codecs.open(save_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def main(args: argparse.Namespace) -> None:
    if not args.single:
        # Get the language to translate based on Slurm array index
        slum_id_env = "SLURM_ARRAY_TASK_ID"
        try:
            language_index = int(os.environ[slum_id_env])
        except KeyError:
            print(f"{slum_id_env} not found. Defaulting to 0 (i.e Arabic)")
            # Default to Arabic, you can change to any other language
            language_index = 0
        # List of languages to translate to
        language_list = [
            "arabic",
            "chinese",
            "french",
            "german",
            "hindi",
            "italian",
            "japanese",
            "korean",
            "russian",
            "spanish",
        ]
        language = language_list[language_index]
    else:
        language = args.language

    # Get list of all .json files paths
    json_file_paths = []

    for filename in os.listdir(args.directory_path):
        if filename.endswith(".json"):
            file_path = osp.join(args.directory_path, filename)
            json_file_paths.append(file_path)

    if not args.single:
        pool = multiprocessing.Pool()
        # Apply parallel translation to all .json files
        for file_path in json_file_paths:
            pool.apply_async(
                translate_content, args=(args, file_path, language)
            )
        pool.close()
        pool.join()
    else:
        for file_path in json_file_paths:
            translate_content(args, file_path, language)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args=args)



--------------------------------------------------------------------------------
# File: verifier\math_verifier_example.py
--------------------------------------------------------------------------------

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

import asyncio

from camel.logger import get_logger
from camel.verifiers import MathVerifier

logger = get_logger(__name__)

# Initialize verifier with configuration
verifier = MathVerifier(float_rounding=6, numeric_precision=15)


async def main():
    r"""Run test cases demonstrating different verification scenarios."""

    print("\nStarting Math Verifier Examples\n")
    await verifier.setup()

    try:
        # Test case 1: Basic numerical equivalence (should succeed)
        print("=== Test 1: Basic Numerical ===")
        result = await verifier.verify(
            solution="0.333333", reference_answer="1/3"
        )
        print("Input: 0.333333 ≈ 1/3")
        print(f"Result: {result.status}")
        print(
            f"err: {result.error_message if result.error_message else 'None'}"
        )

        # Test case 2: LaTeX expressions (should succeed)
        print("=== Test 2: LaTeX Expression ===")
        result = await verifier.verify(
            solution=r"$\frac{1}{2}$", reference_answer=r"0.5"
        )
        print("Input: \\frac{1}{2} = 0.5")
        print(f"Result: {result.status}")
        print(
            f"err: {result.error_message if result.error_message else 'None'}"
        )

        # Test case 3: Deliberate mismatch (should fail)
        print("=== Test 3: Expected Failure ===")
        result = await verifier.verify(
            solution="0.5", reference_answer="0.3333"
        )
        print("Input: 0.5 ≠ 0.3333")
        print(f"Result: {result.status}")
        print(
            f"err: {result.error_message if result.error_message else 'None'}"
        )

    finally:
        await verifier.cleanup()
        print("Math Verifier Examples Completed")


if __name__ == "__main__":
    asyncio.run(main())

"""
===============================================================================
Starting Math Verifier Examples

=== Test 1: Basic Numerical ===
Input: 0.333333 ≈ 1/3
Result: VerificationOutcome.SUCCESS
err: None

=== Test 2: LaTeX Expression ===
Input: \frac{1}{2} = 0.5
Result: VerificationOutcome.SUCCESS
err: None

=== Test 3: Expected Failure ===
Input: 0.5 ≠ 0.3333
Result: VerificationOutcome.FAILURE
err: Solution does not match ground truth

Math Verifier Examples Completed
===============================================================================
"""



--------------------------------------------------------------------------------
# File: verifier\python_verifier_example.py
--------------------------------------------------------------------------------

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
import asyncio

from camel.verifiers import PythonVerifier

verifier = PythonVerifier(required_packages=["numpy"])
asyncio.run(verifier.setup(uv=True))

numpy_test_code = """
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.dot(a, b)
print(result)
"""


# Since the output of the above numpy code evaluates to 32,
# we expect the verification outcome to be a success.
result = asyncio.run(
    verifier.verify(solution=numpy_test_code, reference_answer="32")
)
print(f"Result: {result}")

result = asyncio.run(
    verifier.verify(solution=numpy_test_code, reference_answer="40")
)

# Now we expect the VerificationOutcome to be a failure,
# because the answer is wrong.
print(f"Result: {result}")

asyncio.run(verifier.cleanup())



--------------------------------------------------------------------------------
# File: vision\duckduckgo_video_object_recognition.py
--------------------------------------------------------------------------------

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
from typing import List

from PIL import Image

from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.prompts import PromptTemplateGenerator
from camel.toolkits import SearchToolkit, VideoDownloaderToolkit
from camel.types import RoleType, TaskType


def detect_image_obj(image_list: List[Image.Image]) -> None:
    sys_msg = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.OBJECT_RECOGNITION, RoleType.ASSISTANT
    )
    print("=" * 20 + " SYS MSG " + "=" * 20)
    print(sys_msg)
    print("=" * 49)
    agent = ChatAgent(sys_msg)

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content="Please start the object detection for the following images!",
        image_list=image_list,
        image_detail="high",
    )

    assistant_response = agent.step(user_msg)
    print("=" * 20 + " RESULT " + "=" * 20)
    print(assistant_response.msgs[0].content)
    print("=" * 48)


def main():
    # Create an instance of the SearchToolkit
    search_toolkit = SearchToolkit()

    # Example query for DuckDuckGo video search
    query = "The future of AI in education"

    # Perform a DuckDuckGo search with the query, setting source to 'videos'
    results = search_toolkit.search_duckduckgo(
        query=query, source="videos", max_results=5
    )

    # Try to download videos from the search results
    for result in results:
        video_url = result['embed_url']
        if not video_url:
            print(f"No valid video URL provided for result: {result}")
            continue

        print(f"Trying to download video from: {video_url}")
        downloader = VideoDownloaderToolkit()
        image_list = downloader.get_video_screenshots(video_url, 3)
        if image_list and len(image_list) > 0:
            print(
                f'''Successfully downloaded video and captured screenshots 
                from: {video_url}'''
            )
            detect_image_obj(image_list)
            print("Stopping further downloads as we found valid images.")
            break
        else:
            print(f"Failed to capture screenshots from video: {video_url}")

    print("Exited the video download loop.")


if __name__ == "__main__":
    main()

"""
===============================================================================
Successfully downloaded video and captured screenshots 
                from: https://www.youtube.com/embed/RRMVF0PPqZI?autoplay=1
==================== SYS MSG ====================
You have been assigned an object recognition task.
Your mission is to list all detected objects in following image.
Your output should always be a list of strings starting with `1.`, `2.` etc.
Do not explain yourself or output anything else.
=================================================
==================== RESULT ====================
1. Drone
2. Hangar
3. Person (in uniform)
4. Plants
5. Wall (brick)
6. Table
7. Electrical panels
8. Lights
9. Floor
================================================
Stopping further downloads as we found valid images.
Exited the video download loop.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: vision\image_crafting.py
--------------------------------------------------------------------------------

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
from camel.agents.chat_agent import ChatAgent
from camel.models import ModelFactory
from camel.prompts import PromptTemplateGenerator
from camel.toolkits import DalleToolkit
from camel.types import (
    ModelPlatformType,
    ModelType,
    RoleType,
    TaskType,
)


def main():
    sys_msg = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.IMAGE_CRAFT, RoleType.ASSISTANT
    )
    print("=" * 20 + " SYS MSG " + "=" * 20)
    print(sys_msg)
    print("=" * 49)

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )

    dalle_agent = ChatAgent(
        system_message=sys_msg,
        model=model,
        tools=DalleToolkit().get_tools(),
    )

    response = dalle_agent.step("Draw a picture of a camel.")

    print("=" * 20 + " RESULT " + "=" * 20)
    print(response.msg.content)
    print("=" * 48)


if __name__ == "__main__":
    main()

"""
===============================================================================
==================== SYS MSG ====================
You are tasked with creating an original image based on
        the provided descriptive captions. Use your imagination
        and artistic skills to visualize and draw the images and
        explain your thought process.
=================================================
==================== RESULT ====================
I have created an image of a camel standing in a desert oasis under the shade 
of a palm tree. You can see the realistic and detailed drawing of the camel in 
the image below. 

![Camel in a Desert Oasis](img/58a2a3fa-1e7e-407c-8cd6-4b99448b6a90.png) 

The scene captures the essence of the desert environment with the camel 
peacefully resting in the oasis.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: vision\multi_condition_image_crafting.py
--------------------------------------------------------------------------------

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
from PIL import Image

from camel.agents.chat_agent import ChatAgent
from camel.generators import PromptTemplateGenerator
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.toolkits import DalleToolkit
from camel.types import (
    ModelPlatformType,
    ModelType,
    RoleType,
    TaskType,
)


def main(image_paths: list[str]) -> list[str]:
    sys_msg = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.MULTI_CONDITION_IMAGE_CRAFT, RoleType.ASSISTANT
    )
    print("=" * 20 + " SYS MSG " + "=" * 20)
    print(sys_msg)
    print("=" * 49)

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )

    dalle_agent = ChatAgent(
        system_message=sys_msg,
        model=model,
        tools=DalleToolkit().get_tools(),
    )

    image_list = [Image.open(image_path) for image_path in image_paths]

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content='''Please generate an image based on the provided images and 
        text, make the backgroup of this image is in the morning''',
        image_list=image_list,
    )

    response = dalle_agent.step(user_msg)

    print("=" * 20 + " RESULT " + "=" * 20)
    print(response.msg.content)
    print("=" * 48)


if __name__ == "__main__":
    main()

"""
===============================================================================
==================== SYS MSG ====================
You are tasked with creating an image based on
        the provided text and images conditions. Please use your
        imagination and artistic capabilities to visualize and
        draw the images and explain what you are thinking about.
=================================================
==================== RESULT ====================
Here is the generated image of a serene desert scene in the morning:

![Morning Desert Scene](img/3d8310e8-9f14-48be-94db-c66dd0461cd0.png)

The scene features a camel standing on a sand dune, palm trees, and an oasis 
in the background. The sun is rising, casting a soft golden light over the 
landscape with clear skies and a few scattered clouds.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: vision\multi_turn_image_refining.py
--------------------------------------------------------------------------------

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
import re
from copy import deepcopy

from colorama import Fore
from PIL import Image

from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.prompts import PromptTemplateGenerator
from camel.responses import ChatAgentResponse
from camel.toolkits import DalleToolkit
from camel.types import (
    ModelPlatformType,
    ModelType,
    RoleType,
    TaskType,
)
from camel.utils import print_text_animated


class MMChat:
    r"""The class of multimodal chat session.

    NOTE: Currently this example doesn't work properly, since the generated
    image is not included in the response message. Need to add support to
    include Image in response message.
    """

    def __init__(
        self,
    ) -> None:
        self.critic = None
        self.artist = None
        critic_sys = """You need to describe what you see in the figure
and improve the prompt of it.
Reply with the following format:

CRITICS: the image needs to improve...
PROMPT: here is the updated prompt!
        """
        self.critic_sys_msg = BaseMessage.make_assistant_message(
            role_name='Critic', content=critic_sys
        )

        self.artist_sys_msg = BaseMessage.make_assistant_message(
            role_name="Artist",
            content=PromptTemplateGenerator().get_prompt_from_key(
                TaskType.MULTI_CONDITION_IMAGE_CRAFT, RoleType.ASSISTANT
            ),
        )

        self.init_agents()

    def init_agents(self):
        r"""Initialize artist and critic agents with their system messages."""
        model = ModelFactory.create(
            model_platform=ModelPlatformType.DEFAULT,
            model_type=ModelType.DEFAULT,
        )

        self.artist = ChatAgent(
            system_message=self.artist_sys_msg,
            model=model,
            tools=DalleToolkit().get_tools(),
        )

        self.artist.reset()

        self.critic = ChatAgent(
            system_message=self.critic_sys_msg, model=model
        )
        self.critic.reset()

    def step(self, initialPrompt: str, iter_num=2) -> ChatAgentResponse:
        r"""Process of the drawing and criticising.

        Returns:
            ChatAgentResponse: it contains the response message of
            the artist agent in the last iteration.

        """

        artist_user_msg = BaseMessage.make_user_message(
            role_name="User", content=initialPrompt
        )
        print(
            Fore.MAGENTA
            + "=" * 10
            + "ARTIST SYS"
            + "=" * 10
            + "\n"
            + self.artist_sys_msg.content
        )
        print(
            Fore.YELLOW
            + "=" * 10
            + "ARTIST USR"
            + "=" * 10
            + "\n"
            + artist_user_msg.content
        )

        pattern = r'''\(.*?/([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-
        [0-9a-fA-F]{4}-[0-9a-fA-F]{12})(\.jpg|\.png)\)'''
        response = self.artist.step(artist_user_msg)
        matches = re.findall(pattern, response.msg.content)

        image_paths = [f"./img/{uuid}{ext}" for uuid, ext in matches]
        tmp_paths = deepcopy(image_paths)
        response_msg = re.sub(
            pattern,
            lambda x: "(" + image_paths.pop(0) + ")",
            response.msg.content,
        )
        image_paths = deepcopy(tmp_paths)

        print_text_animated(
            Fore.BLUE
            + "=" * 10
            + "ARTIST RES"
            + "=" * 10
            + "\n"
            + response_msg
        )
        print(response_msg)

        i = 0
        while i < iter_num:
            i += 1
            # Resize the image to 128x128
            resized_imgs = [
                Image.open(image_path).resize(
                    (128, 128), Image.Resampling.LANCZOS
                )
                for image_path in image_paths
            ]
            # Save for maintaining the image format
            [
                img.save(f"tmp_{i}.png", "PNG")
                for i, img in enumerate(resized_imgs)
            ]
            saved = [f"tmp_{i}.png" for i in range(len(resized_imgs))]
            image_list = [Image.open(image) for image in saved]

            critic_user_msg = BaseMessage.make_user_message(
                role_name="User",
                content="image:",
                image_list=image_list,
                image_detail="low",
            )
            print(
                Fore.GREEN
                + "=" * 10
                + "CRITIC SYS"
                + "=" * 10
                + "\n"
                + self.critic_sys_msg.content
            )
            print(
                Fore.RED
                + "=" * 10
                + "CRITIC USR"
                + "=" * 10
                + "\n"
                + critic_user_msg.content
            )
            prompt = self.critic.step(critic_user_msg).msg.content
            print_text_animated(
                Fore.CYAN
                + "=" * 10
                + "CRITIC RES"
                + "=" * 10
                + "\n"
                + prompt
                + Fore.RESET
            )

            artist_user_msg = BaseMessage.make_user_message(
                role_name="User",
                content='''Please generate a image based on
                the following prompt: \n'''
                + prompt,
            )
            response = self.artist.step(artist_user_msg)

            matches = re.findall(pattern, response.msg.content)
            image_paths = [f"./img/{uuid}{ext}" for uuid, ext in matches]
            tmp_paths = deepcopy(image_paths)
            response_msg = re.sub(
                pattern,
                lambda x, image_paths=image_paths: "("
                + image_paths.pop(0)
                + ")",
                response.msg.content,
            )
            image_paths = deepcopy(tmp_paths)
            print_text_animated(
                Fore.BLUE
                + "=" * 10
                + "ARTIST RES"
                + "=" * 10
                + "\n"
                + response_msg
            )
            print(response_msg)

        return response


if __name__ == "__main__":
    session = MMChat()
    res = session.step(
        initialPrompt='''Create an image with pink background,
        a dog is showing a sign with 'I Love Camel'.''',
        iter_num=1,
    )



--------------------------------------------------------------------------------
# File: vision\object_recognition.py
--------------------------------------------------------------------------------

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
import argparse

from PIL import Image

from camel.agents import ChatAgent
from camel.generators import PromptTemplateGenerator
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import (
    ModelPlatformType,
    ModelType,
    RoleType,
    TaskType,
)

parser = argparse.ArgumentParser(description="Arguments for object detection.")
parser.add_argument(
    "--image_paths",
    metavar='N',
    type=str,
    nargs='+',
    help="Path to the images for object detection.",
    default=None,
    required=True,
)


def detect_image_obj(image_paths: str) -> None:
    sys_msg = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.OBJECT_RECOGNITION, RoleType.ASSISTANT
    )
    print("=" * 20 + " SYS MSG " + "=" * 20)
    print(sys_msg)
    print("=" * 49)

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )
    agent = ChatAgent(
        sys_msg,
        model=model,
    )
    image_list = [Image.open(image_path) for image_path in image_paths]

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content="Please start the object detection for following image!",
        image_list=image_list,
        image_detail="high",
    )
    assistant_response = agent.step(user_msg)
    print("=" * 20 + " RESULT " + "=" * 20)
    print(assistant_response.msgs[0].content)
    print("=" * 48)


def main(args: argparse.Namespace) -> None:
    detect_image_obj(args.image_paths)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args=args)



--------------------------------------------------------------------------------
# File: vision\video_description.py
--------------------------------------------------------------------------------

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
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.prompts.prompt_templates import PromptTemplateGenerator
from camel.types import ModelPlatformType, ModelType
from camel.types.enums import RoleType, TaskType

# Define system message
sys_msg_prompt = PromptTemplateGenerator().get_prompt_from_key(
    TaskType.VIDEO_DESCRIPTION, RoleType.ASSISTANT
)

model = ModelFactory.create(
    model_platform=ModelPlatformType.DEFAULT,
    model_type=ModelType.DEFAULT,
)

# Set agent
camel_agent = ChatAgent(sys_msg_prompt, model=model)

# The video from YouTube can be found at the following link:
# https://www.youtube.com/watch?v=kQ_7GtE529M
video_path = "bison.mp4"
with open(video_path, "rb") as video_file:
    video_bytes = video_file.read()
user_msg = BaseMessage.make_user_message(
    role_name="User",
    content="These are frames from a video that I want to upload. Generate a"
    "compelling description that I can upload along with the video.",
    video_bytes=video_bytes,
)

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
"""
===============================================================================
Title: "Survival in the Snow: A Bison's Battle Against Wolves" 
Description:
Witness the raw power of nature in this gripping video showcasing a dramatic 
encounter between a lone bison and a pack of wolves in a snowy wilderness. As 
the harsh winter blankets the landscape, the struggle for survival 
intensifies. Watch as the bison, isolated from its herd, faces the relentless
pursuit of hungry wolves. The tension escalates as the wolves coordinate 
their attack, attempting to overcome the bison with their numbers and 
strategic movements. Experience the breathtaking and brutal moments of this 
wildlife interaction, where every second is a fight for survival. This video 
captures the fierce beauty and the stark realities of life in the wild. Join 
us in observing these incredible animals and the instinctual battles that 
unfold in the heart of winter's grasp.
===============================================================================
"""



--------------------------------------------------------------------------------
# File: vision\web_video_description_extractor.py
--------------------------------------------------------------------------------

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
from camel.messages import BaseMessage
from camel.prompts import PromptTemplateGenerator
from camel.toolkits import VideoDownloaderToolkit
from camel.types import RoleType, TaskType

video_url = (
    "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"
)
downloader = VideoDownloaderToolkit()

# Get the video bytes
video_bytes = downloader.get_video_bytes(video_url)

sys_msg = PromptTemplateGenerator().get_prompt_from_key(
    TaskType.VIDEO_DESCRIPTION, RoleType.ASSISTANT
)

camel_agent = ChatAgent(sys_msg)

# Create user message with video bytes
user_msg = BaseMessage.make_user_message(
    role_name="User",
    content="These are frames from a video that I want to upload. Generate a"
    " compelling description that I can upload along with the video.",
    video_bytes=video_bytes,
)

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
"""
===============================================================================
Join the delightful adventure of a lovable, chubby bunny as he emerges from
 his cozy burrow to greet the day! Watch as he stretches and yawns, ready to
explore the vibrant, lush world around him. This heartwarming and beautifully 
animated scene is sure to bring a smile to your face and brighten your day. 
Don't miss out on this charming moment of pure joy and wonder! 🌿🐰✨
===============================================================================
"""



--------------------------------------------------------------------------------
# File: vision\web_video_object_recognition.py
--------------------------------------------------------------------------------

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
import argparse

from camel.agents import ChatAgent
from camel.generators import PromptTemplateGenerator
from camel.messages import BaseMessage
from camel.toolkits.video_toolkit import VideoDownloaderToolkit
from camel.types import (
    RoleType,
    TaskType,
)

parser = argparse.ArgumentParser(description="Arguments for object detection.")
parser.add_argument(
    "--video_url",
    type=str,
    help="URL of the video for screenshot extraction.",
    required=True,
)
parser.add_argument(
    "--timestamps",
    type=int,
    help="Number of screenshots to capture.",
    default=3,
)


def detect_image_obj(image_list) -> None:
    sys_msg = PromptTemplateGenerator().get_prompt_from_key(
        TaskType.OBJECT_RECOGNITION, RoleType.ASSISTANT
    )
    print("=" * 20 + " SYS MSG " + "=" * 20)
    print(sys_msg)
    print("=" * 49)

    agent = ChatAgent(sys_msg)

    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content="Please start the object detection for the following images!",
        image_list=image_list,
        image_detail="high",
    )
    assistant_response = agent.step(user_msg)
    print("=" * 20 + " RESULT " + "=" * 20)
    print(assistant_response.msgs[0].content)
    print("=" * 48)


def main() -> None:
    video_url = 'https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4'
    downloader = VideoDownloaderToolkit()

    image_list = downloader.get_video_screenshots(video_url, 3)

    detect_image_obj(image_list)


if __name__ == "__main__":
    main()
"""
===============================================================================
==================== SYS MSG ====================
You have been assigned an object recognition task.
Your mission is to list all detected objects in following image.
Your output should always be a list of strings starting with `1.`, `2.` etc.
Do not explain yourself or output anything else.
=================================================
==================== RESULT ====================
1. Rabbit
2. Grass
3. Rocks
4. Tree roots
5. Background trees
6. Hill
7. Sky
8. Stone structure
================================================
===============================================================================
"""



--------------------------------------------------------------------------------
# File: workforce\hackathon_judges.py
--------------------------------------------------------------------------------

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
import textwrap

from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.societies.workforce import Workforce
from camel.tasks import Task
from camel.toolkits import FunctionTool, SearchToolkit
from camel.types import ModelPlatformType, ModelType


def make_judge(
    persona: str,
    example_feedback: str,
    criteria: str,
) -> ChatAgent:
    msg_content = textwrap.dedent(
        f"""\
        You are a judge in a hackathon.
        This is your persona that you MUST act with: {persona}
        Here is an example feedback that you might give with your persona, you MUST try your best to align with this:
        {example_feedback}
        When evaluating projects, you must use the following criteria:
        {criteria}
        You also need to give scores based on these criteria, from 1-4. The score given should be like 3/4, 2/4, etc.
        """  # noqa: E501
    )

    sys_msg = BaseMessage.make_assistant_message(
        role_name="Hackathon Judge",
        content=msg_content,
    )

    model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )

    agent = ChatAgent(
        system_message=sys_msg,
        model=model,
    )

    return agent


def main():
    proj_content = textwrap.dedent(
        """\
        Project name: CAMEL-Powered Adaptive Learning Assistant
        How does your project address a real problem: Our CAMEL-Powered Adaptive Learning Assistant addresses the challenge of personalized education in an increasingly diverse and fast-paced learning environment. Traditional one-size-fits-all approaches to education often fail to meet the unique needs of individual learners, leading to gaps in understanding and reduced engagement. Our project leverages CAMEL-AI's advanced capabilities to create a highly adaptive, intelligent tutoring system that can understand and respond to each student's learning style, pace, and knowledge gaps in real-time.
        Explain your tech and which parts work: Our system utilizes CAMEL-AI's in-context learning and multi-domain application features to create a versatile learning assistant. The core components include:
        1. Learner Profile Analysis: Uses natural language processing to assess the student's current knowledge, learning preferences, and goals.
        2. Dynamic Content Generation: Leverages CAMEL-AI to create personalized learning materials, explanations, and practice questions tailored to each student's needs.
        3. Adaptive Feedback Loop: Continuously analyzes student responses and adjusts the difficulty and style of content in real-time.
        4. Multi-Modal Integration: Incorporates text, images, and interactive elements to cater to different learning styles.
        5. Progress Tracking: Provides detailed insights into the student's learning journey, identifying strengths and areas for improvement.
        Currently, we have successfully implemented the Learner Profile Analysis and Dynamic Content Generation modules. The Adaptive Feedback Loop is partially functional, while the Multi-Modal Integration and Progress Tracking features are still in development.
        """  # noqa: E501
    )

    search_toolkit = SearchToolkit()
    search_tools = [
        FunctionTool(search_toolkit.search_google),
        FunctionTool(search_toolkit.search_duckduckgo),
    ]

    researcher_model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )

    researcher_agent = ChatAgent(
        system_message=BaseMessage.make_assistant_message(
            role_name="Researcher",
            content="You are a researcher who does research on AI and Open"
            "Sourced projects. You use web search to stay updated on the "
            "latest innovations and trends.",
        ),
        model=researcher_model,
        tools=search_tools,
    )

    vc_persona = (
        'You are a venture capitalist who is obsessed with how projects can '
        'be scaled into "unicorn" companies. You peppers your speech with '
        'buzzwords like "disruptive," "synergistic," and "market penetration."'
        ' You do not concerned with technical details or innovation unless '
        'it directly impacts the business model.'
    )

    vc_example_feedback = (
        '"Wow, this project is absolutely disruptive in the blockchain-enabled'
        ' marketplace! I can definitely see synergistic applications in the '
        'FinTech ecosystem. The scalability is through the roof--this is '
        'revolutionary!'
    )

    vc_criteria = textwrap.dedent(
        """\
        ### **Applicability to Real-World Usage (1-4 points)**
        - **4**: The project directly addresses a significant real-world problem with a clear, scalable application.
        - **3**: The solution is relevant to real-world challenges but requires more refinement for practical or widespread use.
        - **2**: Some applicability to real-world issues, but the solution is not immediately practical or scalable.
        - **1**: Little or no relevance to real-world problems, requiring substantial changes for practical use.
        """  # noqa: E501
    )

    vc_agent = make_judge(
        vc_persona,
        vc_example_feedback,
        vc_criteria,
    )

    eng_persona = (
        'You are an experienced engineer and a perfectionist. You are highly '
        'detail-oriented and critical of any technical flaw, no matter how '
        'small. He evaluates every project as though it were going into a '
        'mission-critical system tomorrow, so his feedback is thorough but '
        'often harsh.'
    )

    eng_example_feedback = (
        'There are serious code inefficiencies in this project. The '
        'architecture is unstable, and the memory management is suboptimal. '
        'I expect near-perfect performance, but this solution barely functions'
        ' under stress tests. It has potential, but it is nowhere near '
        'deployment-ready.'
    )

    eng_criteria = textwrap.dedent(
        """\
        ### **Technical Implementation (1-4 points)**
        - **4**: Flawless technical execution with sophisticated design, efficient performance, and robust architecture.
        - **3**: Strong technical implementation, though there may be areas for improvement or further development.
        - **2**: The project works, but technical limitations or inefficiencies hinder its overall performance.
        - **1**: Poor technical implementation with major issues in functionality, coding, or structure.
        """  # noqa: E501
    )

    eng_agent = make_judge(
        eng_persona,
        eng_example_feedback,
        eng_criteria,
    )

    founder_persona = (
        'You are a well-known AI startup founder who is always looking for the'
        ' "next big thing" in AI. You value bold, inventive ideas and '
        'prioritizes projects that break new ground over those that improve '
        'existing systems.'
    )

    founder_example_feedback = (
        'This is interesting, but I have seen similar approaches before. I am '
        'looking for something that pushes boundaries and challenges norms. '
        'What is the most revolutionary part of this project? Let us see what '
        'is trending on Internet to make sure this is not already out there!'
    )

    founder_criteria = textwrap.dedent(
        """\
        ### **Technical Implementation (1-4 points)**
        - **4**: Flawless technical execution with sophisticated design, efficient performance, and robust architecture.
        - **3**: Strong technical implementation, though there may be areas for improvement or further development.
        - **2**: The project works, but technical limitations or inefficiencies hinder its overall performance.
        - **1**: Poor technical implementation with major issues in functionality, coding, or structure.
        """  # noqa: E501
    )

    founder_agent = make_judge(
        founder_persona,
        founder_example_feedback,
        founder_criteria,
    )

    contributor_persona = (
        'You are a contributor to the CAMEL-AI project and is always excited '
        'to see how people are using it. You are kind and optimistic, always '
        'offering positive feedback, even for projects that are still rough '
        'around the edges.'
    )

    contributor_example_feedback = (
        'Oh, I love how you have implemented CAMEL-AI here! The use of its '
        'adaptive learning capabilities is fantastic, and you have really '
        'leveraged the contextual reasoning in a great way! Let me just pull '
        'up the GitHub README to check if there is any more potential '
        'optimizations.'
    )

    contributor_criteria = textwrap.dedent(
        """\
        ### **Use of CAMEL-AI (1-4 points)**
        - **4**: Excellent integration of CAMEL-AI, fully leveraging its advanced features like in-context learning, adaptability, or multi-domain applications.
        - **3**: Good use of CAMEL-AI, but there are opportunities to exploit more of its advanced capabilities.
        - **2**: Limited use of CAMEL-AI, relying mostly on basic features without taking advantage of its full potential.
        - **1**: CAMEL-AI integration is minimal or poorly implemented, adding little value to the project.
        """  # noqa: E501
    )

    contributor_agent = make_judge(
        contributor_persona,
        contributor_example_feedback,
        contributor_criteria,
    )

    workforce = Workforce('Hackathon Judges')
    task = Task(
        content="Evaluate the hackathon project. First, do some research on "
        "the information related to the project, then each judge should give a"
        " score accordingly. Finally, list the opinions from each judge while"
        " preserving the judge's unique identity, along with the score and"
        " judge name, and also give a final summary of the opinions.",
        additional_info=proj_content,
        id="0",
    )

    workforce.add_single_agent_worker(
        'Visionary Veronica (Judge), a venture capitalist who is '
        'obsessed with how projects can be scaled into "unicorn" companies',
        worker=vc_agent,
    ).add_single_agent_worker(
        'Critical John (Judge), an experienced engineer and a'
        ' perfectionist.',
        worker=eng_agent,
    ).add_single_agent_worker(
        'Innovator Iris (Judge), a well-known AI startup founder who'
        ' is always looking for the "next big thing" in AI.',
        worker=founder_agent,
    ).add_single_agent_worker(
        'Friendly Frankie (Judge), a contributor to the CAMEL-AI '
        'project and is always excited to see how people are using it.',
        worker=contributor_agent,
    ).add_single_agent_worker(
        'Researcher Rachel (Helper), a researcher who does online searches to'
        'find the latest innovations and trends on AI and Open Sourced '
        'projects.',
        worker=researcher_agent,
    )

    task = workforce.process_task(task)
    print(task.result)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: workforce\multiple_single_agents.py
--------------------------------------------------------------------------------

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

from camel.agents.chat_agent import ChatAgent
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.societies.workforce import Workforce
from camel.tasks.task import Task
from camel.toolkits import (
    FunctionTool,
    GoogleMapsToolkit,
    SearchToolkit,
    WeatherToolkit,
)
from camel.types import ModelPlatformType, ModelType


def main():
    search_toolkit = SearchToolkit()
    search_tools = [
        FunctionTool(search_toolkit.search_google),
        FunctionTool(search_toolkit.search_duckduckgo),
    ]

    # Set up web searching agent
    search_agent_model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )
    search_agent = ChatAgent(
        system_message=BaseMessage.make_assistant_message(
            role_name="Web searching agent",
            content="You can search online for information",
        ),
        model=search_agent_model,
        tools=[*search_tools, *WeatherToolkit().get_tools()],
    )

    # Set up tour guide agent
    tour_guide_agent_model = ModelFactory.create(
        model_platform=ModelPlatformType.DEFAULT,
        model_type=ModelType.DEFAULT,
    )

    tour_guide_agent = ChatAgent(
        BaseMessage.make_assistant_message(
            role_name="Tour guide",
            content="You are a tour guide",
        ),
        model=tour_guide_agent_model,
        tools=GoogleMapsToolkit().get_tools(),
    )

    # Set up traveler agent
    traveler_agent = ChatAgent(
        BaseMessage.make_assistant_message(
            role_name="Traveler",
            content="You can ask questions about your travel plans",
        ),
        model=ModelFactory.create(
            model_platform=ModelPlatformType.DEFAULT,
            model_type=ModelType.DEFAULT,
        ),
    )

    workforce = Workforce('A travel group')

    workforce.add_single_agent_worker(
        "A tour guide",
        worker=tour_guide_agent,
    ).add_single_agent_worker(
        "A traveler", worker=traveler_agent
    ).add_single_agent_worker(
        "An agent who can do online searches", worker=search_agent
    )

    # specify the task to be solved
    human_task = Task(
        content=(
            "Plan a one-week trip to Paris, considering some historical places"
            " to visit and weather conditions."
        ),
        id='0',
    )

    task = workforce.process_task(human_task)

    print('Final Result of Original task:\n', task.result)


if __name__ == "__main__":
    main()



--------------------------------------------------------------------------------
# File: workforce\role_playing_with_agents.py
--------------------------------------------------------------------------------

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

from camel.agents.chat_agent import ChatAgent
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.societies.workforce import Workforce
from camel.tasks.task import Task
from camel.toolkits import GoogleMapsToolkit, SearchToolkit, WeatherToolkit
from camel.types import ModelPlatformType, ModelType


def main():
    guide_sysmsg = BaseMessage.make_assistant_message(
        role_name="tour guide",
        content="You have to lead everyone to have fun",
    )

    planner_sysmsg = BaseMessage.make_assistant_message(
        role_name="planner",
        content="good at tour plan.",
    )

    guide_agent = ChatAgent(guide_sysmsg)
    planner_agent = ChatAgent(planner_sysmsg)

    function_list = [
        *SearchToolkit().get_tools(),
        *WeatherToolkit().get_tools(),
        *GoogleMapsToolkit().get_tools(),
    ]

    model_platform = ModelPlatformType.DEFAULT
    model_type = ModelType.DEFAULT
    assistant_role_name = "Searcher"
    user_role_name = "Professor"
    assistant_agent_kwargs = dict(
        model=ModelFactory.create(
            model_platform=model_platform,
            model_type=model_type,
        ),
        tools=function_list,
    )
    user_agent_kwargs = dict(
        model=ModelFactory.create(
            model_platform=model_platform,
            model_type=model_type,
        ),
    )

    workforce = Workforce('a travel group')
    workforce.add_role_playing_worker(
        'research Group',
        assistant_role_name,
        user_role_name,
        assistant_agent_kwargs,
        user_agent_kwargs,
        1,
    ).add_single_agent_worker(
        'tour guide', guide_agent
    ).add_single_agent_worker('planner', planner_agent)

    human_task = Task(
        content="research history of Paris and plan a tour.",
        id='0',
    )
    task = workforce.process_task(human_task)

    print('Final result of original task:\n', task.result)


if __name__ == "__main__":
    main()


