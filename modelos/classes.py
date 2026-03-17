import requests
from dotenv import load_dotenv
import os



#Lê a chave da API que está em .env
load_dotenv()
api_key = os.getenv("API_KEY")
chave = {
    "x-api-key": api_key
}

#Clase responsavel por manipular API
class ApiCliente:
    def __init__(self,url):
        self.url = url

    #Metodo para obter os dogs
    def get_dogs(self):
        url = self.url
        resposta = requests.get(url,params=chave)
        resposta.raise_for_status()
        return resposta.json()




