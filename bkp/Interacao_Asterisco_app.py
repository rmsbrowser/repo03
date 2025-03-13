
import streamlit as st
import subprocess

def main():
    st.title("Executar as interações do Programa em C com Entrada do Usuário")
    st.text("Obs: O programa original em Cpossui um erro , ele sempre subtrai duas interações")

    # Solicita um número inteiro ao usuário
    numero = st.text_input("Digite o número de interações:") 

    if st.button("Executar"):
        if numero.isdigit():
            # Executa o programa com o número como entrada
            resultado = subprocess.run(["/work/C_Program/LinuxBuild-DeepNote/asterisco.x64"], input=numero, capture_output=True, text=True)

            # Exibe a saída do programa
            st.text("Saída do programa:")
            st.text(resultado.stdout)
        else:
            st.error("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
