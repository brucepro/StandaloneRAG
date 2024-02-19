import requests
import langchain
from datetime import datetime, timedelta
from rag.rag_data_memory import RAG_DATA_MEMORY
from langchain_community.document_loaders import SeleniumURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class UrlHandler():
    def __init__(self, character_name):
        self.character_name = character_name
        pass

    def get_url(self, url, mode='output'):
        urls = [url]
        loader = SeleniumURLLoader(urls=urls)
        
        data = loader.load()
        
        #save to rag memory
           
        if mode == 'input':
            return data
        elif mode == 'output':
            thedata = str(data)
            return f"[URL_CONTENT={url}]\n{thedata}"
