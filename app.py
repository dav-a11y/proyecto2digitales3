import streamlit as st

st.title("TechNova Systems")
st.subheader("Plataforma de Ventas y Comercio")
st.write("Bienvenido al portal de gestión de ventas de TechNova Systems.")
st.metric("Ventas del día", "$12,450", "+5.3%")
st.line_chart({"Ventas": [100, 200, 150, 300, 250, 400]})

