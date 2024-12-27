def criar_novo_historico(sobrescrever = False):
    lista_campos = "Data,Jogador,Palavra,Qtd palpites,Resultado,Palpite 1,Palpite 2,Palpite 3,Palpite 4,Palpite 5,Palpite 6,Palpite 7,Palpite 8,Palpite 9,Palpite 10,Palpite 11,Palpite 12,Palpite 13,Palpite 14,Palpite 15"

    try:
        # arquivo = open("Histórico dos jogadores//Histórico.csv", "x", encoding="utf-8")
        arquivo = open("Histórico dos jogadores//Histórico.csv", "x", encoding="ISO-8859-2")
        arquivo.write(lista_campos)
        arquivo.close()
    
    except: # Se o histórico já existir, vai dar um erro. Será que é para sobrescrever?
        if sobrescrever == True:
            print("Histórico já existe!")
            var_escolha = input(">>> Deseja recriar histórico do zero? 🛑 \033[41m NÃO PODE SER DESFEITO \033[0m🛑 (\033[1mS\033[0m para sim, qualquer tecla para não) ")

            if (var_escolha == "S") + (var_escolha == "s"):
                # arquivo = open("Histórico dos jogadores//Histórico.csv", "w", encoding="utf-8")
                arquivo = open("Histórico dos jogadores//Histórico.csv", "w", encoding="ISO-8859-2")
                arquivo.write(lista_campos)
                arquivo.close()

            else:
                pass



def criar_novo_resultado(resultado):
    try:
        # tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")
        tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="ISO-8859-2")
    except:
        criar_novo_historico()
        # tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="utf-8")
        tabela_jogador = pd.read_csv("Histórico dos jogadores//Histórico.csv", encoding="ISO-8859-2")


    tabela_jogador = pd.concat(
        [
            tabela_jogador if not tabela_jogador.empty else None, 
            pd.DataFrame([resultado], columns = tabela_jogador.columns)
        ],
        ignore_index = False
    )
    
    tabela_jogador.to_csv("Histórico dos jogadores//Histórico.csv", index = False, encoding="utf-8")
    # tabela_jogador.to_csv("Histórico dos jogadores//Histórico.csv", index = False, encoding="ISO-8859-2")
    

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


# https://github.com/ricardopeloi/minha_biblioteca_python/blob/main/Biblioteca.ipynb
def grafico_com_rotulos(
    dados, coluna_x, coluna_y, 
    tipo_grafico = "bar", titulo_grafico = "", tamanho_grafico = (20, 8),
    fig = None, ax = None, 
    tamanho_fonte = 12, grossura_barra = 1,
    cor_x = "b", rotacao_x = 0, 
    formato_y = ":.2f", rotacao_y = 0, limite_min_y = None, limite_max_y = None,
    xytext_label_y = (0,10),
    ):
  
    import matplotlib.pyplot as plt
    from matplotlib import ticker
    import numpy as np
    

    if fig is None:
      fig = plt.figure(figsize = tamanho_grafico)
  
    plt.clf()
    plt.rcParams.update({'font.size': tamanho_fonte})


    ys = dados[coluna_y]
    xs = np.arange(len(dados[coluna_x]))

    if (tipo_grafico == "bar") | (tipo_grafico == "line"):
      if (tipo_grafico == "bar"):
        plt.bar(
            x = xs,
            height = ys,
            width = grossura_barra,
            label = coluna_y,
        )
      elif (tipo_grafico == "line"):
        plt.plot(
          xs,
          ys,
          cor_x + "o-",
          label = coluna_y,
        )

      # display(cor_x + "o-")


      ax1 = plt.gca()
      if (limite_min_y is not None) & (limite_max_y is not None):
        ax1.set_ylim([min(dados[coluna_y])*limite_min_y, max(dados[coluna_y])*limite_max_y])

      ax1.set_ylabel(coluna_y, color = cor_x)
      ax1.set_xlabel(coluna_x)

      for x,y in zip(xs,ys):
          formato_y_rotulo = "{" + formato_y + "}"
          label = formato_y_rotulo.format(y)

          plt.annotate(label, # this is the text
                      (x,y), # these are the coordinates to position the label
                      textcoords="offset points", # how to position the text
                      xytext = xytext_label_y, # distance from text to points (x,y)
                      ha='center', # horizontal alignment can be left, right or center
                      color = cor_x,
                      rotation = rotacao_y)


      ax1.xaxis.set_tick_params(rotation = rotacao_x)

      # fig.legend()
      plt.xticks(xs, dados[coluna_x])
      formato_y_eixo = "{x" + formato_y + "}"
      ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter(formato_y_eixo))
      ax1.axes.get_yaxis().set_visible(False)

    elif tipo_grafico == "barh":
      plt.barh(
          y = xs,
          width = ys,
          height = grossura_barra,
          # label = coluna_y,
      )
      ax1 = plt.gca()
      ax1.set_yticks(xs, dados[coluna_x])

      ax1.set_ylabel(coluna_x)
      ax1.set_xlabel(coluna_y, color = cor_x)
      ax1.invert_yaxis()

      if (limite_min_y is not None) & (limite_max_y is not None):
        ax1.set_xlim([min(dados[coluna_y])*limite_min_y, max(dados[coluna_y])*limite_max_y])

      for x,y in zip(xs,ys):
        label = formato_y.format(y)

        plt.annotate(label, # this is the text
                  (y, x), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext = (xytext_label_y[1], xytext_label_y[0]), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  color = cor_x,
                  rotation = rotacao_y)

    plt.title(titulo_grafico)
    plt.show()



def gerar_grafico(tabela_dados_jogador, var_nome_jogador):
   
    # print(tabela_dados_jogador.T)
    tabela_resultados = tabela_dados_jogador[["Qtd palpites", "Jogador"]].groupby("Qtd palpites").count().reset_index() \
        .rename(columns = {"Jogador": "Qtd partidas"})
    # print(tabela_resultados)

    if (var_nome_jogador == "H") + (var_nome_jogador == "h"):
        var_titulo_grafico = "Resultados de todos os jogadores"
    else:
        var_titulo_grafico = "Resultados do jogador " + var_nome_jogador

    grafico_com_rotulos(
        tabela_resultados, "Qtd palpites", "Qtd partidas", 
        tipo_grafico = "bar", titulo_grafico = var_titulo_grafico, tamanho_grafico = (5, 3),
        fig = None, ax = None, 
        tamanho_fonte = 12, grossura_barra = 0.8,
        cor_x = "b", rotacao_x = 0, 
        formato_y = ":.0f", rotacao_y = 0, limite_min_y = 0, limite_max_y = 1.2,
        xytext_label_y = (0,5),
    )



from main import check_and_install_packages
lista_libraries = ["pandas", "matplotlib", "numpy"]
check_and_install_packages(lista_libraries)
import pandas as pd # type: ignore