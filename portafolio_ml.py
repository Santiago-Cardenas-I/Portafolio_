import streamlit as st
from PIL import Image

st.title("Aplicaciones de Machine Learning.")

with st.sidebar:
    st.subheader("Aplicaciones de Machine Learning.")
    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.write(parrafo)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ml})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Prueba Streamlit")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearning-wykpjd5xmsfqqvb6zpypep.streamlit.app//"
    st.write(f"KNN: [Enlace]({url})")

    

with col2:
    st.subheader("Regresión logística")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo agrupar datos usando K-Means.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://santiagoappseguros.streamlit.app/"
    st.write(f"K-Means: [Enlace]({url})")

with col3:
    st.subheader("Algoritmos de clasificación.")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://clasificadorapp.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col4:
    st.subheader("Consumo electrico.")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://appconsumoenergia.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col5:
    st.subheader("Árboles de Decisión")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://arboldedecision-fqqvqqt3xu7eovbgetngs4.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col6:
    st.subheader("Medidor de energía")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://medidordeenergia-ckh2webpsnpldwujpjsf6f.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")


