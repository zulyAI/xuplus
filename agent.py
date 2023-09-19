from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import mysql.connector



# execute only once,
# store table names and description in the vector db
# later use different strategy find diff result
def _init_tables_from_schema():
    mydb = mysql.connector.connect(host="localhost",  user="root",  password="q1w2e3r4",  database="db")
    cursor = mydb.cursor()
    query_find_tables = ("select tables.table_name,tables.table_comment"
                         " from information_schema.tables where tables.table_schema='db'")
    cursor.execute(query_find_tables)
    table_result = cursor.fetchall()
    # init return list
    table_info = []
    column_info = []
    for i in range(len(table_result)):
        table_item = table_result[i]
        table_name = table_item[0]
        description = table_item[1]
        _temp = {"name": table_name,"descript":description}
        table_info.append(_temp)
        # assemble table
        query_find_columns = "SELECT COLUMN_NAME,COLUMN_COMMENT from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='" + table_name +"'"
        cursor.execute(query_find_columns)
        column_result = cursor.fetchall()
        # assemble column
        _column = {"table": table_name, "column": column_result}
        column_info.append(_column)
    mydb.close()
    return table_info, column_info


def from_vec2word_with_strategy(table_info, column_info):
    embedding_function = SentenceTransformerEmbeddings(model_name="../text2vec-base-chinese")
    table_ = ""
    for i in range(len(table_info)):
        table_item = table_info[i]
        table_name = table_item["name"]
        table_description = table_item["descript"]
        table_text_for_embedding = table_name + ":" + table_description + "\n"
        table_ += table_text_for_embedding
    ## persist table
    print(table_)

    text_splitter = CharacterTextSplitter(separator="\n")
    table_2_persist = text_splitter.split_text(table_)
    table_db = Chroma.from_texts(table_2_persist, embedding=embedding_function, persist_directory="./database/table.db")
    table_db.persist()

    field_2_ = ""
    for j in range(len(column_info)):
        column_item = column_info[j]
        table_name = column_item["table"]
        field_2_ += table_name + ":\n"
        columns = column_item["column"]

        for q in range(len(columns)):
            single_column = columns[q]
            field_name = single_column[0]
            field_descript = single_column[1]
            field_ = "  " + field_name + ":" + field_descript + "\n"
            field_2_ += field_
        field_2_ += "\n\n"
    ## persist field
    field_splitter = CharacterTextSplitter(separator="\n\n")
    field_2_persist = field_splitter.split_text(field_2_)
    field_db = Chroma.from_texts(field_2_persist, embedding=embedding_function, persist_directory="./database/field.db")
    field_db.persist()

    print(field_2_)

## test
table, column = _init_tables_from_schema()
from_vec2word_with_strategy(table, column)



