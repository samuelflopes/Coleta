# -*- coding: utf-8 -*-
"""5.2 Script da Coleta

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12uROKbFqHY_iXtFtBmQRNeYsALds6Tel

### Instalação do Request e Beautfulsoup
"""

''' Instalação e Importação das bibliotecas requests ( requisição HTTPS )
    && BeautifulSoup ( Extração de dados de arquivos HTML e XML )
    Comand Request:  Requests lhe permite integrar seus programas Python com web services.
    Comand BeautifulSoup: é projetado para fazer com que a captura de tela ou screen-scraping seja feita rapidamente.
    
---------------------      
  Analise da tabela
  100592
  1082
---------------------  

page = requests.get(url)

page.text

# read_csv("arquivo.csv")
'''

!pip install requests

"""### Importação das Bibliotecas"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

"""### Inicio"""

total_df=[]

for i in range (199709,201709):
  i = str(i)
  
  if not i[-1] == '0' and i[-2] == '0':
    
    requisicao = requests.get('http://www.nuforc.org/webreports/ndxe' + i +'.html')
    reqts = requisicao.text
    soup = BeautifulSoup(reqts,'html.parser')
    table = soup.find_all(name='table')
    table_str = str(table)
    df = pd.read_html (table_str)[0]
    total_df.append(df)
    time.sleep(1)
  
df_total = pd.concat(total_df, ignore_index=True)

df_total.to_csv('ndx.csv')

"""## INICIO"""

total_df = [] 
  
for i in range (199709,201709):
  requisicao = requests.get('http://www.nuforc.org/webreports/ndxe'+str(i)+'.html')       # requisição da pagina html
  soup = BeautifulSoup(requisicao.text,'html.parser')                                               # biblioteca BeautifulSoup p/ extrair os elementos da tabela
  table = soup.find_all(name='table')                                                     # Acessando os elementos da tabela
  table_str = str(table)                                                                  # 
  df = pd.read_html (table_str)[0]                                                        # Acessando o ponto 0 da tablela
  total_df.append(df)
  time.sleep(1)

  df_total = pd.concat(total_df, ignore_index=True)

df_total.to_csv('coleta.csv')

lists = []

meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]

for i in range(1997,2018):
  for mes in meses:
    link = "{}{}.html".format('http://www.nuforc.org/webreports/ndxe.html',str(i) + mes)
               
    if i == 1997:
      if mes not in ['09','10','11','12']:
        continue
               
    if i == 2017:
      if mes not in ['09','10','11','12']:
        continue

    requisicao = requests.get(link).text
    reqts = requisicao

    soup = BeautifulSoup(requisicao, 'html.parser')
    table = soup.find_all(name='table')
    table_str = str(table)
    df= pd.read_html(table_str)[0]
    lists.append(df)

    time.sleep(1)
    
file_df =  pd.concat(lists, ignore_index=True)  
file_df.to_csv('arv.csv')