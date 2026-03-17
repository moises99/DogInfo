from deep_translator import GoogleTranslator as gl
import streamlit as st

#Função para tradução
def traducao(texto,traducao = False):
    '''
    Recebe como parametro o texto da requisição.
    Mude o parametro traducao para True e tenha a traducao em PT-BR.
    Mude o target e tenha a tradução para o idioma desejado, ex target='uk'
    '''    
    if traducao:
        texto_pt = gl(source='en',target='pt').translate(str(texto))
        return texto_pt
    else:
        return texto
    
