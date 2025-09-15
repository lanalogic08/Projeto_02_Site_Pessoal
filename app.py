
#impot streamlit

# aqui eu coloco o titulo 
# st.tittle('Olá, mundo')

# #criando um calendario 
# date = st.date_input("Selecione uma data")

# #Permitindo o upload 
# file = st.file_uploader("Pick a file")
#  python -m streamlit run app.py

import streamlit as st 
import pandas as pd 

#sidebar para mexer na barra lateral
st.sidebar.image("logo.webp")
st.sidebar.title('Almeida Select - Moda, Acessórios & Autocuidado')
st.title('Curadoria premium pensada para mulheres que se valorizam.')

#opções de roupas que ira ter no meu site
itens = ['Vestidos', 'Acessorios']

#opção para a pessoa clicar e escolher a sua roupa
#opcao = st.sidebar.selectbox('Clique aqui, para fazer sua escolha', roupas)

#DICIONARIO RELACIONANDOI OS TIPOS DE ROPUPAS 
estilo = {
    "Vestidos": ["Midi", "Longo Maxi", "Ciganinha (Off-shoulder)", "Slip Dress", "Boho", "Elegante de festa"], 
    "Acessorios": ["Brincos", "Colares", "Aneis", "Pulseiras", "Bolsas", "Óculos", "Cintos"],
    }

# Selectbox para escolher a opção
item_selecionado = st.sidebar.selectbox("Selecione o que deseja:", itens)

# Selectbox para escolher o item 
if item_selecionado:
    item_escolhido = st.sidebar.selectbox(
        "Selecione o item:",
        estilo[item_selecionado]
    )

# Mostrar apenas o item selecionado
if item_selecionado and item_escolhido:
    st.write(f"{item_escolhido}")
    st.write(f"{item_selecionado}")
    st.image(f"{item_escolhido}.png")

st.markdown('🩲 Siga a Almeida Select nas redes sociais e acompanhe as novidades')
st.link_button = ''
# import streamlit as st
#titulo do site
# #escolhendo as opções que tem no site 
# st.image(f'{opcao}.png')
# st.markdown(f'## Você gostou destes modelo : {opcao}')
# st.markdown('---')

# dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
# km =  st.text_input(f'Quantos km você pretende rodar com o {opcao}?')

# if opcao == 'Fiat Mobi':
#     diaria = 130

# elif opcao == 'Renaut Kwid':
#     diaria = 160

# elif opcao == 'Hyundai HB20 Sedan':
#     diaria = 200

# elif opcao == 'Honda Civic':
#     diaria = 250

# elif opcao == 'Audi Q5':
#     diaria = 850

# elif opcao == 'Mercedes-AMG GT':
#     diaria = 4.500

# elif opcao == 'BMW X6':
#     diaria = 2.500

# elif opcao == 'Fiat Toro':
#     diaria = 350 


# if st.button('Calcular'):
#     dias = int(dias)
#     km = float(km)

#     total_dias = dias * diaria 
#     total_km = km * 0.15
#     aluguel_total = total_dias + total_km

#     st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')

