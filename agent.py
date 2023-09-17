from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
import mysql.connector


name_and_description = {}


def _generate_name_and_description():
    return name_and_description


# execute only once,
# store table names and description in the vector db
# later use different strategy find diff result
def _init_tables_from_schema(persistence_path):
    mydb = mysql.connector.connect(host="localhost",  user="root",  password="q1w2e3r4",  database="db")
    cursor = mydb.cursor()
    query_find_tables = ("select tables.table_name,tables.table_comment"
                         " from information_schema.tables where tables.table_schema='db'")
    cursor.execute(query_find_tables)
    table_result = cursor.fetchall()
    mydb.close()
    qa = []
    for i in range(len(table_result)):
        table_item = table_result[i]
        table = table_item[0]
        description = table_item[1]
        item = {table: description}
        qa.append(item)
    return qa


def _init_columns_from_schema(persistence_path,qa):
    mydb = mysql.connector.connect(host="localhost",  user="root",  password="q1w2e3r4",  database="db")
    cursor = mydb.cursor()
    for i in range(len(qa)):
    # keep

    #query_find_column = ("select column_name,column_comment,data_type from information_schema.columns where table_name='" + qa + "'")


def from_vec2word_with_strategy(sql_task: str):
    # load the document and split it into chunks
    loader = TextLoader(file_path=".\table.txt", encoding="utf-8")
    sql_table_document = loader.load()

    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    table_docs = text_splitter.split_documents(sql_table_document)

    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="shibing624/text2vec-base-chinese")

    # load it into Chroma
    db = Chroma.from_documents(table_docs, embedding_function, persist_directory="./database/table.db")
    db.persist()


_init_tables_from_schema("123123")




