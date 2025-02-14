import streamlit as st

st.title("🤖 Chatbot de Recetas de Cocina")
st.write("¡Bienvenido! Pregunta lo que desees sobre cocina.")

# Verificar si el modelo se carga correctamente
try:
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    st.write("✅ Modelo cargado correctamente.")
except Exception as e:
    st.write(f"❌ Error al cargar el modelo: {e}")

# Entrada del usuario
user_input = st.text_input("🍽️ ¿Qué deseas saber sobre cocina?")

# Respuesta del chatbot
if user_input:
    try:
        response = chatbot(user_input, max_length=100, pad_token_id=50256)
        st.write(f"🧑‍🍳 Respuesta del chatbot: {response[0]['generated_text']}")
    except Exception as e:
        st.write(f"❌ Error al generar respuesta: {e}") en la pagina me salio esto  Error al cargar el modelo: name 'pipeline' is not defined corrigelo que no me muestre


