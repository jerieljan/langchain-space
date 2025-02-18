from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

MODEL_NAME = "gpt-4o-mini"
EMBEDDING_NAME = "text-embedding-3-small"
BASE_URL = "https://ainovate.novare.com.hk/"
load_dotenv()


def init_model(streaming=False) -> ChatOpenAI:
    return ChatOpenAI(model=MODEL_NAME, base_url=BASE_URL, streaming=streaming)


def init_embedding() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(model=EMBEDDING_NAME, base_url=BASE_URL)
