# -*- coding: utf-8 -*-
#Projeto_Visualizacao_da_Informacao.ipynb

from pandas_datareader import data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

empresas = [('Itaú', 'ITUB4.SA'), ('Bradesco', 'BBDC4.SA'), ('Magalu', 'MGLU3.SA')]

# usando um for de 0 a 3 porque temos três nomes de empresas
# quero pegar os tikers de cada uma
for i in range(3):
    nome = empresas[i][1]
    # em uma variavel colocamos os dados que vem do site
    cotacao = web.DataReader(f'{nome}', data_source='yahoo',start='2022-5-1', end='2022-5-11')
    # aqui pedimos para o python salvar os dados da variavel em um arquivo csv
    cotacao.to_csv(f'{nome}.csv')
    # arquivos gravados na mesma pasta do projeto

# Para utilizar a biblioteca usei o link
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
# gravando dados em arquivos csv

# vamos consultar os dados dos arquivos
# colocar os dados dos arquivos csv em data frame 
itub4_df = pd.read_csv('ITUB4.SA.csv')
display(itub4_df)
bbdc4_df = pd.read_csv('BBDC4.SA.csv')
display(bbdc4_df)
mglu3_df = pd.read_csv('MGLU3.SA.csv')
display(bbdc4_df)

# Com o dataset pronto
# DataFrame com dados de cada arquivo csv
# inicia a montagem de cada gráfico

# abre uma lista vazia
volume_vendas = []
# pegamos o ultimo valor da coluna Volume de cada data frame e coloca na lista volume_vendas
volume_vendas.append(itub4_df['Volume'].iloc[-1])
volume_vendas.append(bbdc4_df['Volume'].iloc[-1])
volume_vendas.append(mglu3_df['Volume'].iloc[-1])
# abre uma lista com cores para ser usada no gráfico
cores = ['pink','yellow','cyan']
# abre uma lista com rotulos para identificar as empresas
rotulos = ['Itau','Bradesco','Magalu']
print(volume_vendas)
print(cores)
print(rotulos)

# Criando o gráfico

# tamanho da figura 7x7
plt.figure(figsize=(7,7))
# montar o grafico:
# pegamos os dados, os rotulos e as cores 
# transforma os valores em porcentagem sem casas decimais e o angulo de inicio é de 90 graus
plt.pie(volume_vendas, labels=rotulos, colors=cores, autopct=('%1.0f%%''A'), startangle=90)
# grafico com eixos iguais para a figura ser igual a uma pizza
plt.axis('equal')
# coloca um titulo na figura com cor e tamanho da fonte
plt.title('Volume de Vendas de Ações em  11/05/2022', color='blue', fontsize=14)
# coloco a legenda
plt.legend()
plt.show()

# Preparando dados para o segundo grafico

# montando lista de valores da coluna fechamento ajustado
itau = itub4_df['Adj Close']
# montando lista bradesco
bradesco = bbdc4_df['Adj Close']
# montando lista magalu
magalu = mglu3_df['Adj Close']
# montando a lista de datas do periodo 
datas = itub4_df['Date']

print('ITAU\n',itau)
print('Bradesco\n',bradesco)
print('Magalu\n',magalu)
print('Data\n',datas)

# Criando o Próximo gráfico 

# uma lista com os labels
labels = ['Itau','Bradesco','Magalu']
# tamanho da figura 
plt.figure(figsize=(13,6))
data_x = np.arange(len(datas))
# ajustes para que as barras não fiquem uma em cima da outra
# aqui uma das barras fica 0.1 a esquerda a largura 0.1 e cor vermelha
plt.bar(data_x-0.1, itau, width=0.1,color='red')
# esta barra fica no centro tem largura 0.1 de cor azul
plt.bar(data_x, bradesco, width=0.1,color='blue')
# esta barra fica 0.1 a direita tem largura 0.1 cor='verde'
plt.bar(data_x+0.1, magalu, width=0.1,color='green')
# coloquei a legenda no centro
plt.legend(labels,loc='center')
# colocando as datas no eixo x
plt.xticks(data_x, datas)
# no eixo y coloquei preço minimo da magalu ate preço maximo do itau
plt.yticks(np.arange(min(magalu), max(itau)))
# coloquei um grid no y para ficar mais visivel
plt.grid(color='black', linestyle='--', linewidth=1, axis='y', alpha=0.3)
# titulo do grafico
plt.title('As variaçoes dos valores das Ações da carteira', color='blue', fontsize=14)
# label no eixo x
plt.xlabel('Periodo', fontsize=20, color='red')
# label no eixo y
plt.ylabel('Preços', fontsize=20, color='blue')
plt.show()

# Criando o Próximo gráfico 

# tamanho da figura
plt.figure(figsize=(13,7))
data_x = np.arange(len(datas))
# neste plot dados do anterior cor vermelha largura da linha 0.1 marcador nas datas
plt.plot(itau, c='red', lw='1', marker='o', label='ITUB4.SA')# vermelho
# neste plot dados do anterior cor azul largura da linha 0.1 marcador nas datas
plt.plot(bradesco, c='blue', lw='1', marker='o', label='BBDC4.SA')# azul
# neste plot dados do anterior cor verde largura da linha 0.1 marcador nas datas
plt.plot(magalu, c='green', lw='1', marker='o', label='MGLU3.SA')# verde
# colocar legenda
plt.legend()
# colocando no eixo x as datas do periodo selecionado
plt.xticks(data_x, datas)
# no eixo y o valor minimo da magalu e o valor maximo do itau
plt.yticks(np.arange(min(magalu), max(itau)))
# colocado um grid para a melhor visualização
plt.grid(color='black', linestyle='--', linewidth=1, axis='y', alpha=0.3)
# colocando titulo
plt.title('As variaçoes dos valores das Ações da carteira', color='blue', fontsize=20)
# uma label no eixo x
plt.xlabel('Periodo', fontsize=20, color='red')# vermelho
# uma label no eixo y
plt.ylabel('Preços', fontsize=20, color='blue')# azul
plt.show()

