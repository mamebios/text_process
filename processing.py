from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain


#llm = OpenAI(temperature=0)

text_splitter = CharacterTextSplitter()

class Processor:
    def __init__(self) -> None:
        #self.chain = load_summarize_chain(llm, chain_type="map_reduce")
        pass

    def process(self, text: str) -> str: 
        #return self.chain.run(text)
        return text + ' -> funfou!!\n'