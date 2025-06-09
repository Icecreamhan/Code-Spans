# 加载一些基础包
from llm import qwen25_72b

# 1.获取用户问题
query = input("")


# 2.用户问题改写(llm)
def rewrite(query):
    prompt = "请将用户问题改写为四个问题，要求以列表格式输出"

    return qwen25_72b(prompt) # list


# 3.获取问题embedding
def emb_model(text_list):
    from llm import bge_m3
    return bge_m3(text_list)


# 4.读取文档内容，将文档进行切片
# 5.文档片段进行embedding化
def load_docu(file):
    # 根据文档后缀，判断文档类型
    # word等文档
    from documentparse import parser
    content = parser(file)
    str_list = content.split("\n\n")
    # return emb_model(str_list) # str_list
    embeddings = emb_model(str_list)
    db = FAISS.from_documents(str_list,embeddings)
    return str_list


# 6.入库、召回的操作
def retrieve_relevent_docs(query, top_k):
    similar_docs = db.similarity_search(query,top_k)
    return [doc.page_content for doc in similar_docs]


# 7.使用余弦相似度，获取与用户问题相关的top_k个文档片段
def macth_topk(query,chunk_list):
    from rag import consine
    return consine(query,emb_model(chunk_list))


# 将用户问题+文档片段+ 提示词，送入模型中
def generate_answer(query):
    relvent_docs = retrieve_relevent_docs(query,top_k = 2)
    context = "\n".join(relvent_docs)
    prompt = f"请根据下面```中的信息回复用户问题，```{context}```用户问题：{query}"
    response = qwen25_72b(query,prompt)