import imp
import re
from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import ElasticVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings, CacheBackedEmbeddings
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
from langchain.document_loaders import PyMuPDFLoader,DirectoryLoader
from langchain.storage import LocalFileStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.retrievers import BM25Retriever,EnsembleRetriever


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
    dir_loader = DirectoryLoader(r"D:\Workspace\DocChat\source_documents",
                                 glob="*.pdf",
                                 loader_cls=PyMuPDFLoader)
    docs = dir_loader.load()
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=450,
                                      chunk_overlap=200,)
    esops_documents = text_splitter.transform_documents(docs)
    print(f"number of chunks in documents : {len(esops_documents)}")

    store = LocalFileStore("./cache/")
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    core_embeddings_model = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs)
    embedder = CacheBackedEmbeddings.from_bytes_store(core_embeddings_model,
                                                      store,
                                                      namespace=model_name)
    # Create VectorStore
    vectorstore = FAISS.from_documents(esops_documents,embedder)
    bm25_retriever = BM25Retriever.from_documents(esops_documents)
    bm25_retriever.k=2

    faiss_retriever = vectorstore.as_retriever(search_kwargs={"k":2})
    ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever,faiss_retriever],
                                           weights=[0.5,0.5])

    """Logic for loading the chain you want to use should go here."""    
    llm = LlamaCpp(model_path=r"D:\Workspace\DocChat\models\llama-2-7b.q4_0.gguf", n_ctx=2048, max_tokens=2048, callbacks=[QueueCallback(q)], n_batch=512, n_gpu_layers=5, verbose=True)
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
        retriever=ensemble_retriever,
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
def main():

    def ask_llm(message, history):
        for next_token, content in stream(message):
            print(next_token)
            yield(content)

    demo = chatInterface = gr.ChatInterface(
                    fn=ask_llm,
    )
    demo.queue().launch()

if __name__ == "__main__":
    main()
