import pandas as pd

tabela_historico = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")

# print(tabela_historico)

lista_jogadores = tabela_historico["Jogador"].unique()

print(lista_jogadores)