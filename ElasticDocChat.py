from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores.elasticsearch import ElasticsearchStore
from search import main1



def main():
    loader = PyMuPDFLoader(r"D:\Workspace\DocChat\source_documents\AnnualReport_04_05.pdf")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=512, chunk_overlap=0
    )
    documents = text_splitter.split_documents(data)

    embeddings = HuggingFaceEmbeddings(model_name=r"D:\Workspace\DocChat\models\embedding\all-mpnet-base-v2")
    es_username = "elastic"
    ex_password = "YvuKJ4M9filZPxB7INKe"
    db = ElasticsearchStore.from_documents(
        documents,
        embeddings,
        es_url=f"http://{es_username}:{ex_password}@localhost:9200",
        #es_url = "http://localhost:9200",
        es_username = "elastic",
        ex_password = "YvuKJ4M9filZPxB7INKe",
        index_name="elastic-index",
        strategy=ElasticsearchStore.ApproxRetrievalStrategy(
        hybrid=True,
        ),
        distance_strategy="COSINE"

    )
    print(db.client.info())



if __name__ == "__main__":
    #main()
    main1()


