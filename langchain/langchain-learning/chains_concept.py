from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="gemma3:1b"
)

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a beginner."
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "Django"
})

print(result)