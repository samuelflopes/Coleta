
#2 Removendo os dados vazios da coluna City, Shape e State
                                                                                              # df_ovni = df_ovini.dropna() -> Comando para deletando todos os valores vazios do Dataframe
df_ovni = [df_ovni['City'].notna()]
df_ovni = [df_ovni['State'].notna()]
df_ovni = [df_ovni['Shape'].notna()]

#...