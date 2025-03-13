
import streamlit as st
import subprocess

def main():
    st.title("Soma dos Dígitos de um Número")

    # Solicita um número ao usuário
    numero = st.text_input("Digite um número:")

    if st.button("Calcular"):
        if numero.isdigit():
            # Executa o programa SomaDigitos_x64 com o número como entrada
            processo = subprocess.run(['/work/C_Program/LinuxBuild-DeepNote/SomaDigitos_x64'], input=numero, text=True, capture_output=True)

            # Exibe a saída do programa
            st.text("Saída do programa:")
            st.text(processo.stdout)
        else:
            st.error("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
