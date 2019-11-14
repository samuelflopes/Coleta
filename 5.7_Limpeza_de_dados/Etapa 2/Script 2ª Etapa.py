
#1 Carregando dados CSV
df_ovni = pd.read_csv('https://raw.githubusercontent.com/oliveirafhm/data_science/master/OVNIS.csv')
df_ovni
shape_popular

"""## Salvando o DataFrame em arquivo CSV"""

# Salvar o 'Df' com os dados limpos 
shape_popular.to_csv('df_OVINI_limpo.csv')

# ...