import requests
from collections import Counter
import numpy as np

response = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/')
resultados = response.json()

#AQUI É GERADO UMA LISTA DE LISTAS SENDO QUE CADA SUB-LISTA É UM RESULTADO DA LOTOFACIL
def get_lotofacil_results():
    all_results = [] 
    for result in resultados:
        dezenas = result['dezenas']
        dezenas_int = [int(d) for d in dezenas]
        all_results.append(dezenas_int)
    return all_results

#AQUI É GERADO O RANK DOS NUMEROS QUE MAIS SE REPETIRAM
def analisa_lista_de_listas(lista_de_listas):
    numeros = [numero for sublista in lista_de_listas for numero in sublista]
    contagem = Counter(numeros)
    ranking = contagem.most_common(25)
    for i, (numero, frequencia) in enumerate(ranking, 1):
         print(f"{i}. {numero}: {frequencia} vezes")

#AQUI RECEBE DUAS LISTAS, A PRIMEIRA DEVE SER OS RESULTADOS DA LOTOFACIL
#A SEGUNDA DEVE SER O JOGO QUE SE QUER SABER SE JÁ OCORREU OU NÃO    
def verifica_listas(lista_principal: list, lista_verificada: list) -> str:
    for lista in lista_principal:
        if lista == lista_verificada:
            return "Esse jogo já ocorreu."
    return "Esse jogo nunca ocorreu."