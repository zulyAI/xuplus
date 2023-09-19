import re

def __parse_pythoncode_from_response(response):
    # 使用正则表达式匹配 Python 代码块
    python_pattern = re.compile(r'(\b(?:def|class|import|from|raise|try|except|finally|with)\b.*?;?)', re.IGNORECASE)
    # 提取匹配的 Python 代码块
    python_blocks = python_pattern.findall(response)
    return python_blocks


# 这个代码有安全隐患，如果没有权限限制将会被黑客使用
def _exec_python_code(response):
    python_code_for_exec = __parse_pythoncode_from_response(response)
    exec(python_code_for_exec)