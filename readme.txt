Necessário adquirir uma chave em : https://docs.thedogapi.com/

Após a aquisição da chave crie um arquivo chamado .env com a seguinte estrutura:

API_KEY= SUA CHAVE DA API

ou passe a chave direto na url:

ex:

chave = {
    "x-api-key": SUA CHAVE AQUI
}

r = requests.get('https://api.thedogapi.com/v1/breeds/',params=chave)
