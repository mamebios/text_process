from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader
#from langchain.chains.retrieval_qa.base import RetrievalQA
#from langchain.indexes.vectorstore import VectorStoreIndexWrapper
#from langchain.vectorstores.chroma import Chroma
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index import Document as Doc
from llama_index import ServiceContext
from llama_index import LLMPredictor

import os

key = ''
with open('key.txt', 'r') as f: key = f.readlines()[0]
os.environ["OPENAI_API_KEY"] = key

class Summarizer:
    def __init__(self) -> None:

        self.llm = OpenAI(temperature=1, openai_api_key=key)
        self.chain = load_summarize_chain(self.llm, chain_type="map_reduce")
        self.text_splitter = CharacterTextSplitter()
        self.buffer = ''
        
    def process(self, text: str) -> str:
        
        texts = self.text_splitter.split_text(text)
        docs = [Document(page_content=t) for t in texts]
        self.buffer = self.chain.run(docs)
         
        return self.buffer

    def change_temperature(self, value: float) -> None:
        self.llm.temperature = value

    def get_temperature(self) -> float:
        return self.llm.temperature
    
class Topicfier:
    def __init__(self) -> None:
        self.query = 'Give me a list of the most important topics'

    def process(self, text: str) -> str:

        doc = [Doc(text)]

        index = GPTSimpleVectorIndex.from_documents(doc)
        response = index.query(self.query)
        print(response)
        print(type(response))
        
        return response.response
        