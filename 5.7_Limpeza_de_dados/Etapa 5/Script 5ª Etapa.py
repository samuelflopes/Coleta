
# 4 Removendo colunas irrelevantes 'Duration' , 'Summary' && 'Posted'
df = df_ovni.drop(['Duration','Summary','Posted'],axis=1)
df

# ...