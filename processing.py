from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

key = ''
with open('key.txt', 'r') as f: key = f.readlines()

class Processor:
    def __init__(self) -> None:

        self.llm = OpenAI(temperature=0, openai_api_key=key)
        self.chain = load_summarize_chain(self.llm, chain_type="map_reduce")
        self.text_splitter = CharacterTextSplitter()
        self.buffer = ''
        #pass

    def process(self, text: str) -> str:
        #print(text+'      oi')
        texts = self.text_splitter.split_text(text)
        docs = [Document(page_content=t) for t in texts]
        self.buffer = self.chain.run(docs)
        #print(self.buffer) 
        return self.buffer
        #return text + ' -> funfou!!\n'