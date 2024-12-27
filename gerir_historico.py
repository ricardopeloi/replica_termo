def criar_novo_historico(sobrescrever = False):
    lista_campos = "Data,Jogador,Palavra,Qtd palpites,Resultado,Palpite 1,Palpite 2,Palpite 3,Palpite 4,Palpite 5,Palpite 6,Palpite 7,Palpite 8,Palpite 9,Palpite 10,Palpite 11,Palpite 12,Palpite 13,Palpite 14,Palpite 15"

    try:
        arquivo = open("Histórico dos jogadores//Histórico.csv", "x", encoding="utf-8")
        arquivo.write(lista_campos)
        arquivo.close()
    
    except: # Se o histórico já existir, vai dar um erro. Será que é para sobrescrever?
        if sobrescrever == True:
            print("Histórico já existe!")
            var_escolha = input(">>> Deseja recriar histórico do zero? 🛑 \033[41m NÃO PODE SER DESFEITO \033[0m🛑 (\033[1mS\033[0m para sim, qualquer tecla para não) ")

            if (var_escolha == "S") + (var_escolha == "s"):
                arquivo = open("Histórico dos jogadores//Histórico.csv", "w", encoding="utf-8")
                arquivo.write(lista_campos)
                arquivo.close()

            else:
                pass



def criar_novo_resultado(resultado):
    try:
        tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")
    except:
        criar_novo_historico()
        tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")


    tabela_jogador = pd.concat(
        [
            tabela_jogador if not tabela_jogador.empty else None, 
            pd.DataFrame([resultado], columns = tabela_jogador.columns)
        ],
        ignore_index = False
    )
    
    # tabela_jogador.to_csv("Histórico dos jogadores//Histórico.csv", index = False, encoding="utf-8")
    tabela_jogador.to_csv("Histórico dos jogadores//Histórico.csv", index = False, encoding="ISO-8859-2")
    

    # print(len(tabela_jogador))
    # print(tabela_jogador)



def ver_historico(var_nome_jogador = False):
    try:
        # tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")
        tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="ISO-8859-2")
    except:
        criar_novo_historico()
        # tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")
        tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="ISO-8859-2")

    if var_nome_jogador == False:
        return tabela_jogador

    else:
        try:
            tabela_jogador = tabela_jogador[tabela_jogador["Jogador"] == var_nome_jogador].copy()
            # print(tabela_jogador)
            return tabela_jogador
        except:
            print("Este jogador não existe!")
            return [False]

    


def ver_jogadores():
    try:
        tabela_jogador = ver_historico(var_nome_jogador = False)
    except:
        criar_novo_historico()
        tabela_jogador = ver_historico(var_nome_jogador = False)

    try:
        lista_jogadores = tabela_jogador["Jogador"].unique()
        # print(lista_jogadores)
        return lista_jogadores
    except:
        print("Ainda não há jogadores disponíveis." + '\n')
        return False



from main import check_and_install_packages
lista_libraries = ["pandas"]
check_and_install_packages(lista_libraries)
import pandas as pd # type: ignore