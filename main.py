from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Responda la pregunta a continuación.

A continuación se muestra el historial de la conversación: {context}

Pregunta: {question}

Respuesta:
"""

model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context = ""
    result = ""
    print("Bienvenido a la conversación. Escribe 'exit' para salir.")
    while True:
        question = input("Pregunta: ")
        if question.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": question})
        print("Respuesta:", result)
        context += f"\nUsuario: {question}\nBot: {result}\n"

if __name__ == "__main__":
    handle_conversation()