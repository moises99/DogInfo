from modelos.classes import ApiCliente
from modelos.funcoes import traducao
import streamlit as st


st.set_page_config(layout="wide",
                   page_title='Doguinhos',
                   page_icon='🐶',
                   )

st.title('Bem vindo a DogInfo 🐶',text_alignment='center')

api = ApiCliente(f'https://api.thedogapi.com/v1/breeds/')
dogs = api.get_dogs()

with st.container(horizontal_alignment="center"):
    buscah = st.text_input('Buscar Dog',width=500,max_chars= 30,placeholder='American Bully')
    botao_pequisa = st.button(label='Pesquisar')
    
if botao_pequisa:
    if len(buscah) <= 0:
        with st.container(horizontal_alignment="center"):
            st.warning('Para realizar uma pesquise, preencha o campo acima!',width=500)
        api = ApiCliente(f'https://api.thedogapi.com/v1/breeds/')
        dogs = api.get_dogs()
    else:
        api = ApiCliente(f'https://api.thedogapi.com/v1/breeds/search?q={buscah}')
        dogs = api.get_dogs()



colunas = st.columns(4)
limitar_colunas = 0
for doguinho in dogs:
    with colunas[limitar_colunas]:
        with st.container(height=1000,border=True):
            st.title(f"{traducao(doguinho['name'])}",text_alignment='center')
            with st.container(width=400):
                st.image(doguinho['image']['url'],caption=doguinho['name'], link=doguinho['image']['url'])
            st.write(f"{traducao('Origem:')} {traducao(doguinho['origin'])}")
            st.write(f"{traducao('Temperamento:')} {traducao(doguinho['temperament'])}.")
            st.write(f"{traducao('Descrição:')} {traducao(doguinho['description'])}")
            limitar_colunas+=1
            if limitar_colunas == 4:
                limitar_colunas = 0
