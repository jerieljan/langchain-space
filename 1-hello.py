from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini",
                 base_url="https://ainovate.novare.com.hk")

print(llm.invoke("Hello world"))