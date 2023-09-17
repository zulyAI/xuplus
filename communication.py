import zhipuai

# "4aa3832d305a9ea60708bf2c5b1ef2bf.kLu6LT45idWHNJJd" // my id
#
zhipuai.api_key = "a6c25810da99d24a71a0893bf5f56e6b.ypC0VAO4DUyuqoGM"


def post(post_input):
    return_response = zhipuai.model_api.invoke(
        model="chatglm_pro",
        prompt=post_input,
        top_p=0.7,
        temperature=0.0,
    )
    return return_response
