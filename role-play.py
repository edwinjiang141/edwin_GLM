import os
import streamlit as st
from typing import Generator


API_KEY: str = os.getenv("ZHIPU_API_KEY", "")
button_labels = {
    "generate_role_1": "生成人设一",
    "generate_role_2": "生成人设二"
}
message_placeholder = st.empty()

if "meta" not in st.session_state:
    st.session_state["meta"] = {
        "bot_info": "",
        "bot_name": "",
        "user_info": "",
        "user_name": ""
    }

with st.container():

    col1, col2 = st.columns(2)
    n_button = len(button_labels)
    cols = st.columns(n_button)
    button_key_to_col = dict(zip(button_labels.keys(), cols))
    with col1:
        st.text_area(label="角色描述一", key="bot_info", on_change=lambda : st.session_state["meta"].update(bot_info=st.session_state["bot_info"]), help="角色的详细人设信息，不可以为空")
        with button_key_to_col["generate_role_1"]:
            generate_role_1 = st.button(button_labels["generate_role_1"], key="generate_role_1")
        
    with col2:
        st.text_area(label="角色描述二", key="user_info", on_change=lambda : st.session_state["meta"].update(user_info=st.session_state["user_info"]), help="角色的详细人设信息，不可以为空")
        with button_key_to_col["generate_role_2"]:
            generate_role_2 = st.button(button_labels["generate_role_2"], key="generate_role_2")
            
with st.container():
    generate_chat= st.button("生成对话", key="generate_chat")

def get_chatglm_response_via_sdk(messages: list) -> Generator[str, None, None]:
    """ 通过sdk调用chatglm """
    # reference: https://open.bigmodel.cn/dev/api#glm-3-turbo  `GLM-3-Turbo`相关内容
    # 需要安装新版zhipuai
    from zhipuai import ZhipuAI
    client = ZhipuAI(api_key=API_KEY) # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages
    )
    return response.choices[0].message.content



def generate_role_1_appearance(role_profile: str) -> Generator[str, None, None]:
    """ 用chatglm生成角色的名称"""

    instruction = f"""
        请从下列文本中，只返回一个合适的人设或者职业的名称。

        文本：
        {role_profile}
        """
    return get_chatglm_response_via_sdk(
        messages=[
            {
                "role": "user",
                "content": instruction.strip()
            }
        ]
    )

def generate_role_2_appearance(role_profile: str) -> Generator[str, None, None]:
    """ 用chatglm生成角色的名称"""

    instruction = f"""
        请从下列文本中，只返回一个合适的人设或者职业的名称。长度不超过8个字

        文本：
        {role_profile}
        """
    return get_chatglm_response_via_sdk(
        messages=[
            {
                "role": "user",
                "content": instruction.strip()
            }
        ]
    )

if generate_role_1:
    role_1_desc = generate_role_1_appearance(st.session_state["meta"]["bot_info"])
    st.session_state["meta"]["bot_name"] = role_1_desc
    

if generate_role_2:
    role_2_desc = generate_role_1_appearance(st.session_state["meta"]["user_info"])
    st.session_state["meta"]["user_name"] = role_2_desc


if generate_chat:
     st.write(st.session_state["meta"]["bot_name"] )
     st.write(st.session_state["meta"]["user_name"] )

     instruction = f"""
        请从下列文本中，根据生成的2个人设角色，和每个角色的描述，生成20轮对话

        角色1：
        {st.session_state["meta"]["bot_name"]}

        角色2：
        {st.session_state["meta"]["user_name"]}
        
        要求：
        生成类似的对话格式如下：
        角色1：你今天感觉如何？
        角色2：我今天感觉不太舒服
        """
     
     
     chat_data=get_chatglm_response_via_sdk(
        messages=[
            {
                "role": "user",
                "content": instruction.strip()
            }
        ]
     )
     with open("chatdata.txt","a") as file:
        file.write(chat_data)

     st.write(chat_data)