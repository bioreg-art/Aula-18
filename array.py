import numpy as np


dados_vendas = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 150])

print(dados_vendas)

#Calculando a Média (sensivel e extremos)
media_vendas = np.mean(dados_vendas)
print(media_vendas)

#Calculando a Mediana(robusta a extremos)
mediana_vendas = np.median(dados_vendas)
print(mediana_vendas)

#Calculando os quartis
q1 = np.percentile(dados_vendas, 25)
print(q1) 

q2 = np.percentile(dados_vendas, 50)
print(q2)

q3 = np.percentile(dados_vendas, 75)
print(q3)