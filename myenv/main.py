import requests
import os
import random
import secrets
import numpy as np

response = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/')
resultados = response.json()

def get_lotofacil_results():
    # Lista vazia para armazenar as dezenas de todos os resultados
    all_results = []
    
    # Percorrendo cada resultado da Lotofácil
    for result in resultados:
        # Obtendo as dezenas do resultado atual
        dezenas = result['dezenas']
        
        # Convertendo as dezenas para inteiros e adicionando à lista de resultados
        dezenas_int = [int(d) for d in dezenas]
        all_results.append(dezenas_int)
    
    # Retornando a lista com as dezenas de todos os resultados
    return all_results

def comparar_listas(listas):
    # Inicializa duas listas vazias para armazenar as informações das listas
    pares_comuns = []

    # Percorre cada lista na entrada, comparando-a com todas as outras listas que estão a sua frente
    for i, lista1 in enumerate(listas):
        for lista2 in listas[i+1:]:
            # Verifica os números em comum entre as duas listas
            numeros_em_comum = set(lista1) & set(lista2)
            # Se houver mais de 11 números em comum, adiciona as informações à lista de pares comuns
            if len(numeros_em_comum) >= 14:
                NumerosQueElasTemEmComum = len(set(lista1 + lista2)) - len(numeros_em_comum)
                pares_comuns.append((lista1, lista2, numeros_em_comum, NumerosQueElasTemEmComum))
        
    # Imprime as listas com números em comum
    for lista1, lista2, numeros_em_comum, NumerosQueElasTemEmComum in pares_comuns:
    #    print(f"Essas listas: {lista1}, {lista2}")
     #   print(f'possuem {len(numeros_em_comum)} números em comum:')
        print(f'{numeros_em_comum}')
    
def is_present(resultados_lotofacil, meu_palpite):
    if meu_palpite in resultados_lotofacil:
        return "A meu_palpite esta presente na lista1."
    else:
        return "A meu_palpite nao esta presente na lista1."
    
    
def ordenar_lista(lista):
    return sorted(lista)

(melhor_palpite_segundo_14) = ordenar_lista([15,2,24,13,3,25,14,6,19,20,1,10,23,4,16])
melhor_palpite_segundo_geral = ordenar_lista([10,20,11,25,13,24,14,5,3,4,12,9,22,19,18])
#print("melhor palpite segundo 14:")
#print(melhor_palpite_segundo_14)    
#print("melhor palpite segundo geral:")
#print(melhor_palpite_segundo_geral)
#print(is_present(get_lotofacil_results(), melhor_palpite_segundo_14))    
#print(is_present(get_lotofacil_results(), melhor_palpite_segundo_geral))    

ordem_de_frequencia_14 = [(15, 117), (2, 113), (24, 112), (13, 111), (3, 110), (25, 109), (14, 107), (6, 107), (19, 105), (20, 105), (1, 105), (10, 104), (23, 103), (4, 102), (16, 99), (21, 99), (22, 99), (12, 98), (7, 97), (17, 95), (5, 95), (8, 94), (11, 93), (18, 92), (9, 91)]

ordem_frequencia_geral = [(10, 1719), (20, 1719), (11, 1711), (25, 1696), (13, 1690), (24, 1683), (14, 1681), (5, 1676), (3, 1674), (4, 1657), (12, 1656), (9, 1653), (22, 1650), (19, 1648), (18, 1647), (2, 1645), (1, 1645), (21, 1639), (15, 1636), (17, 1635), (23, 1623), (7, 1613), (6, 1602), (8, 1594), (16, 1593)]

def random_numbers():
    # Gera uma lista de 15 números aleatórios entre 1 e 25 sem repetições
    random.seed(secrets.token_bytes(16))  # Semente para a fonte de entropia
    numbers = random.sample(range(1, 26), 15)

    # Ordena a lista
    numbers.sort()

    return numbers

lista_aleatoria = random_numbers()
print(lista_aleatoria)
print(is_present(get_lotofacil_results(), lista_aleatoria))



#sequencias_lotofacil = get_lotofacil_results()

#print(comparar_listas(sequencias_lotofacil))
