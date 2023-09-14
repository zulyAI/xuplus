import main

name_and_description = {}


def _generate_name_and_description():
    return name_and_description


# 首先判断Agent是否已经结束
# 如果没有结束：
#       依据LLM 提供的Thought来使用Action，最好让LLM来选择Action.(LLM 返回的结果需要能够找到合适的TOOL)
#

def _switch(thought: str):
    action = _generate_action(thought)
    response = main.send_post(action)
    print(response)
    return response


def _generate_action(thought: str):
    action_to_take = {"name": "Action input", "value": "AD_USER,AD_PRODUCT"}

    return action_to_take


asd = _generate_name_and_description()
print(asd)
