import zhipuai

zhipuai.api_key = "4aa3832d305a9ea60708bf2c5b1ef2bf.kLu6LT45idWHNJJd"


def post(post_input: str, role: str, history: str):
    url = "https://open.bigmodel.cn/api/paas/v3/model-api/chatglm_pro/sse-invoke"
    prompt = [{"role": role, "content": post_input, "history": history}]
    return_response = zhipuai.model_api.invoke(model="chatglm_pro", prompt=prompt, top_p=0.7, temperature=0.0)
    return return_response
