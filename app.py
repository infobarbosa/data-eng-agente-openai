import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

st.set_page_config(page_title="Agente Simples de Perguntas e Respostas", layout="centered")

def gerar_resposta(pergunta: str) -> str:
    """
    Função para enviar a pergunta à API da OpenAI e retornar a resposta do modelo GPT-4.
    """
    try:
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual que responde em português."},
                {"role": "user", "content": pergunta}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        print(response.choices[0].message)

        # Pega apenas o texto da resposta
        resposta = response.choices[0].message.content
        return resposta
    
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

def main():
    st.title("Agente Simples de Perguntas e Respostas (GPT-4)")
    st.write("Digite sua pergunta e aguarde a resposta.")

    # Caixa de texto para o usuário digitar a pergunta
    pergunta_usuario = st.text_area("Pergunta:", value="", height=100)

    if st.button("Enviar"):
        if pergunta_usuario.strip() == "":
            st.warning("Por favor, digite uma pergunta válida.")
        else:
            with st.spinner("Gerando resposta..."):
                resposta = gerar_resposta(pergunta_usuario)
            st.success("Resposta do GPT-4:")
            st.write(resposta)

if __name__ == "__main__":
    main()
