import mysql.connector
import re

# 下面的函数用于从返回信息中提取SQL代码块
def __parse_sql_from_text(response_text):
    # 使用正则表达式匹配 SQL 代码块
    sql_pattern = re.compile(r'(\b(?:SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|GRANT|REVOKE|LOAD_FILE|CREATE_FUNCTION|CALL|RETURN|IF|ELSE|END IF|WHILE|FOR|IN|OUT|PUT|GET|SET|VALUES)\b.*;?)',
                             re.IGNORECASE)
    sql_blocks = sql_pattern.findall(response_text)
    for sql_block in sql_blocks:
        print(' '.join(sql_block))
    return sql_blocks

def exec_sql(response_text: str):
    mydb = mysql.connector.connect(host="localhost",  user="root",  password="q1w2e3r4",  database="db")
    cursor = mydb.cursor()
    #如果没有查询字符串就抛出异常
    #如果查询字符串出错，也抛出异常
    sql_text = __parse_sql_from_text(response_text)
    # 可能会返回多段SQL，此处需要做额外的处理
    cursor.execute(sql_text)
    table_result = cursor.fetchall()
    return table_result