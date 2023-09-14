import streamlit as st
import zhipuai

zhipuai.api_key = "4aa3832d305a9ea60708bf2c5b1ef2bf.kLu6LT45idWHNJJd"


def send_post(post_input: str, role: str):
    url = "https://open.bigmodel.cn/api/paas/v3/model-api/chatglm_pro/sse-invoke"
    prompt = [{"role": str, "content": post_input}]
    return_response = zhipuai.model_api.invoke(model="chatglm_pro", prompt=prompt, top_p=0.7, temperature=0.0)
    return return_response


with st.form("form"):
    text = st.text_area(label="请提出问题", value="您好", height=2)
    submitted = st.form_submit_button('Submit')
    if submitted:
        response_text = send_post(text)
        answer_text = response_text["data"]
        choices = answer_text["choices"][0]
        content = choices["content"]
        st.write(content)
