import streamlit as st

# Configuración de la página para usar todo el ancho
st.set_page_config(page_title="Tablero", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
        .header-container {
            background-color: #2685eb;
            padding: 10px 0;
            text-align: center;
        }
        .header-text {
            color: white;
            font-size: 24px;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .block-container {
            padding: 0 !important;
        }
        body {
            background-color: #f4f4f4;
        }
        iframe {
            width: 100%;
            height: calc(100vh - 80px); /* Esto hace que el iframe ocupe todo el espacio disponible menos la altura del encabezado */
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown("""
    <div style="background-color: #2685eb; height: 80px; display: flex; justify-content: center; align-items: flex-start; padding-top: 25px;">
        <h1 style="color: white; font-size: 24px; margin: 0;"> Proyecto:</h1>
    </div>
""", unsafe_allow_html=True)

# Iframe ocupando todo el espacio disponible (puedo poner el enlace que yo quiera)
st.components.v1.iframe(
    src="https://docs.google.com/spreadsheets/d/11OutLl_fA8jZEiMQScnEUHFsU7Tf883bLatvoxqRofA/edit?usp=sharing",
    height=900,  # Aquí no es necesario especificar la altura si usamos calc(100vh - 80px)
    scrolling=True
)
