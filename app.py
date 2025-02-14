import streamlit as st
from transformers import pipeline  # ✅ Importación corregida

# Título y descripción
st.title("🤖 Chatbot de Recetas de Cocina")
st.write("¡Bienvenido! Pregunta lo que desees sobre cocina.")

# Cargar modelo de forma segura
chatbot = None  # Inicializar en None para evitar errores si no carga

try:
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    st.success("✅ Modelo cargado correctamente.")
except Exception:
    st.warning("⚠️ El chatbot no está disponible en este momento.")

# Entrada del usuario
user_input = st.text_input("🍽️ ¿Qué deseas saber sobre cocina?")

# Respuesta del chatbot
if user_input and chatbot:
    try:
        response = chatbot(user_input, max_length=100, pad_token_id=50256)
        respuesta_chatbot = response[0]['generated_text'].split(user_input)[-1].strip()  # Limpiar respuesta
        st.write(f"🧑‍🍳 **Chatbot:** {respuesta_chatbot}")
    except Exception:
        st.error("❌ Error al generar respuesta.")
