from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description= "A simple API server"
)

prompt = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful assistant. Please answer the user questions related to mental health problems."),
        ("user", "Question: {question}")
    ]
)

llm = Ollama(model="gemma2:2b")
output_parser=StrOutputParser()


add_routes(
    app,
    prompt | llm | output_parser,
    path = "/chat"
)


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)