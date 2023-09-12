import imp
import re
from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import ElasticVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import  LlamaCpp
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import tiktoken
from queue import Queue, Empty
from langchain.chains import ConversationChain
from threading import Thread
from collections.abc import Generator
import gradio as gr


from langchain.callbacks.base import BaseCallbackHandler

class QueueCallback(BaseCallbackHandler):
    """Callback handler for streaming LLM responses to a queue."""

    def __init__(self, q):
        self.q = q

    def on_llm_new_token(self, token: str, **kwargs: any) -> None:
        self.q.put(token)

    def on_llm_end(self, *args, **kwargs: any) -> None:
        return self.q.empty()

def stream(input_text) -> Generator:
    # Create a Queue
    q = Queue()
    job_done = object()
    embeddings = HuggingFaceEmbeddings(model_name=r"D:\Workspace\DocChat\models\embedding\all-mpnet-base-v2")
    es_username = "elastic"
    ex_password = "YvuKJ4M9filZPxB7INKe"
    db = ElasticVectorSearch(
        elasticsearch_url=f"http://{es_username}:{ex_password}@localhost:9200",
        #es_url = "http://localhost:9200",
        index_name="elastic-index",
        embedding=embeddings,
    )
    retriver = db.as_retriever()

    """Logic for loading the chain you want to use should go here."""    
    llm = LlamaCpp(model_path="D:\Workspace\DocChat\models\llm\llama-2-7b.q4_0.gguf", n_ctx=20000, max_tokens=2048, callbacks=[QueueCallback(q)], n_batch=512, n_gpu_layers=20, verbose=False)
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer,\
    just say that you don't know, don't try to make up an answer.

    {context}

    {history}
    Question: {question}
    Helpful Answer:"""
    prompt = PromptTemplate(input_variables=["history", "context", "question"], template=template)
    memory = ConversationBufferMemory(input_key="question", memory_key="history")



    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriver,
        chain_type_kwargs={"prompt": prompt, "memory": memory},

    )
    # Create a funciton to call - this will run in a thread
    def task():
        resp = qa.run(input_text)
        q.put(job_done)

    # Create a thread and start the function
    t = Thread(target=task)
    t.start()

    content = ""

    # Get each new token from the queue and yield for our generator
    while True:
        try:
            next_token = q.get(True, timeout=1)
            if next_token is job_done:
                break
            content += next_token
            yield next_token, content
        except Empty:
            continue
def main1():

    def ask_llm(message, history):
        for next_token, content in stream(message):
            print(next_token)
            yield(content)

    demo = chatInterface = gr.ChatInterface(
                    fn=ask_llm,
    )
    demo.queue().launch()

    #callbacks =  [StreamingStdOutCallbackHandler()]
    #llm = LlamaCpp(model_path="D:\Workspace\DocChat\models\llm\LLaMA-2-7B-32K-Q4_0.gguf", n_ctx=20000, max_tokens=2048, n_batch=512, callbacks=callbacks, n_gpu_layers=20, verbose=False)
    ##qa = RetrievalQA.from_chain_type(
    ##    llm=llm,
    ##    chain_type="stuff",
    ##    retriever=retriver,
    ##)


    #template = """Use the following pieces of context to answer the question at the end. If you don't know the answer,\
    #just say that you don't know, don't try to make up an answer.

    #{context}

    #{history}
    #Question: {question}
    #Helpful Answer:"""

    #prompt = PromptTemplate(input_variables=["history", "context", "question"], template=template)
    #memory = ConversationBufferMemory(input_key="question", memory_key="history")



    #qa = RetrievalQA.from_chain_type(
    #    llm=llm,
    #    chain_type="stuff",
    #    retriever=retriver,
    #    return_source_documents=True,
    #    chain_type_kwargs={"prompt": prompt, "memory": memory},

    #)
    #encoding = tiktoken.get_encoding("cl100k_base")
    #print(qa)
    #query = input("Please enter: ")
    ##response = qa.run(query)
    ##print(response)
    #res = qa(query)
    #answer = res["result"]
    #print(answer)

