
#3 Mantendo somente os estados dos estados Unidos 
# Carregando dados com estados somente dos estados unidos 
df_states_usa = pd.read_csv('https://raw.githubusercontent.com/oliveirafhm/data_science/master/usa_states.csv') 
df_ovni['State']


filtro2 = []
for reg in list(df_ovni['State']):
  if reg in list(df_states_usa['Abbreviation']):
    filtro2.append(True)
  else:
    filtro2.append(False)
df_ovni = df_ovni[filtro2]
# Amostra filtrada somente com estados dos 'Estados Unidos'
df_ovni
# ...