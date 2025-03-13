import streamlit as st
from datetime import date

def calculate_age(birth_day, birth_month, birth_year):
    today = date.today()
    age = (
        today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    )
    return age

st.title("Calculadora de Idade")

birth_day = st.number_input("Digite o dia que você nasceu:", min_value=1, max_value=31, step=1)
birth_month = st.number_input("Digite o mês que você nasceu:", min_value=1, max_value=12, step=1)
birth_year = st.number_input("Digite o ano que você nasceu:", min_value=1900, max_value=date.today().year, step=1)

if st.button("Calcular Idade"):
    age = calculate_age(birth_day, birth_month, birth_year)
    st.write(f"Sua idade é {age} anos.")
