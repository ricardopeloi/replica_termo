def criar_novo_jogador(nome_jogador, sobrescrever = False):
    lista_campos = "Data, Palavra, Qtd palpites, Resultado"

    try:
        arquivo = open("Histórico dos jogadores//" + nome_jogador + ".csv", "x", encoding="utf-8")
        arquivo.write(lista_campos)
        arquivo.close()
    
    except: # Se o jogador já existir, vai dar um erro. Será que é para sobrescrever?
        if sobrescrever == True:
            print("Jogador já existe!")
            var_escolha = input(">>> Deseja recriar histórico do zero? 🛑 \033[41m NÃO PODE SER DESFEITO \033[0m🛑 (\033[1mS\033[0m para sim, qualquer tecla para não) ")

            if (var_escolha == "S") + (var_escolha == "s"):
                arquivo = open("Histórico dos jogadores//" + nome_jogador + ".csv", "w", encoding="utf-8")
                arquivo.write(lista_campos)
                arquivo.close()

            else:
                pass



def criar_novo_resultado(nome_jogador, resultado):
    try:
        tabela_jogador = pd.read_csv("Histórico dos jogadores//" + nome_jogador + ".csv")
    except:
        criar_novo_jogador(nome_jogador)
        tabela_jogador = pd.read_csv("Histórico dos jogadores//" + nome_jogador + ".csv")


    tabela_jogador = pd.concat(
        [
            tabela_jogador if not tabela_jogador.empty else None, 
            pd.DataFrame([resultado], columns = tabela_jogador.columns)
        ],
        ignore_index = True
    )
    
    tabela_jogador.to_csv("Histórico dos jogadores//" + nome_jogador + ".csv", index = False)

    # print(len(tabela_jogador))
    # print(tabela_jogador)



def ver_historico(nome_jogador):
    try:
        tabela_jogador = pd.read_csv("Histórico dos jogadores//" + nome_jogador + ".csv")
    except:
        criar_novo_jogador(nome_jogador)
        tabela_jogador = pd.read_csv("Histórico dos jogadores//" + nome_jogador + ".csv")
    
    print(tabela_jogador)



from main import check_and_install_packages
lista_libraries = ["pandas"]
check_and_install_packages(lista_libraries)
import pandas as pd # type: ignore

# criar_novo_jogador("jogador_teste", sobrescrever = True)
# criar_novo_resultado("jogador_teste", [datetime.datetime.now(), "teste", 5, "vitória"])