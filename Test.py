import random

import communication

prompt = ("now we have following tools:\n"
          "table : useful when you want to find database tables correctly.\n"
          "field : useful when you want to find fields correctly.\n"
          "join : useful when you want to know the relationship between tables.\n"

          "answer me use following format:\n"
          "role: never forgot role you have played.\n"
          "task: task you must done.\n"
          "think: choose one or more tools from [table,field,join].\n"
          "input: information generated by tool , is you got nothing , set it to NULL.\n"
          "output: final answer.\n"
          "begin.\n"
          "role:assistance.\n"
          "task:generate simplest SQL , query the 8th's payment of alex.\n")


task = ("input:after using table tool, I have found following tables in the database.\n"
        "   1、customer_info: include id,name and other information of customer.\n"
        "   2、customer_order: include order information of customer.\n"
        "   3、customer_payment: include payment information of customer.\n"
        "input:after using join tool,I have determined relationship between tables.\n"
        "   1、customer_info and customer_payment:one to many,key is customer_id.\n"
        "   2、customer_order and customer_payment：one to one,key is order_id.\n"
        "input:after using field tool,I have found following fields in the tables.\n"
        "   customer_info\n"
        "       1、customer_name: name of customer.\n"
        "       2、customer_id: id of customer.\n"
        "       3、customer_reg_date: reg time of customer\n"
        "   customer_order:\n"
        "       1、order_id: id of order.\n"
        "       2、order_date：date of order.\n"
        "       3、order_state：state of order, must one of [1,0].\n"
        "   customer_payment:\n"
        "       1、order_id: id of order\n"
        "       2、customer_id: id of customer.\n"
        "       3、customer_payments: payments of a order.\n")



def print_result(llm_response):
    answer_text = llm_response["data"]
    choices = answer_text["choices"][0]
    # use request_id to force in one conversion
    request_id = answer_text["request_id"]
    content = choices["content"]
    contexts = content.split("\\n")
    for i in range(len(contexts)):
        text = contexts[i]
        if len(text) > 0:
            print(f"contexts = {text}", end="\n")


random_int = random.randint(1000, 100000)
print(f"request_id={random_int}")

response = communication.post(role="Assistant", post_input=prompt, request_id=str(random_int))
print_result(response)



new_response = communication.post(role="User", post_input=task, request_id=str(random_int))
print(f"task={task}")
print_result(new_response)

# prompt_by_user =
