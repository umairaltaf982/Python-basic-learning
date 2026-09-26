from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma3:1b"
)

questions = [
    'What is python?',
    'What are its 5 most important topics?',
    'Is python here, refered to a snake?'
]

for q in questions:
    response = model.invoke(q)
    print(response.content)