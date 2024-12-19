def criar_arquivo(caminho_arquivo, lista_palavras):
    try:
        arquivo = open(caminho_arquivo, "x", encoding="utf-8")
    except:
        arquivo = open(caminho_arquivo, "w", encoding="utf-8")

    lista_arquivo = ""

    for palavra in lista_palavras:
        lista_arquivo = lista_arquivo + palavra.lower() + '\n'


    # print(lista_arquivo)
    arquivo.write(lista_arquivo[:-1])
    arquivo.close()



def adicionar_palavra(caminho_arquivo, palavra, print_mensagens = False):
    arquivo = open(caminho_arquivo, "a", encoding="utf-8")
    
    arquivo.write('\n' + palavra)
    arquivo.close()

    if print_mensagens == True:
        print("Palavra \033[1m'" + palavra + "'\033[0m adicionada!" + '\n')

    from processar_listas import processar_lista_para_X_letras
    processar_lista_para_X_letras(var_X = len(palavra))

    return True



def consultar_palavras(caminho_arquivo):
    arquivo = open(caminho_arquivo, "r", encoding="utf-8")
    lista_palavras = arquivo.read().split("\n")
    lista_palavras.sort()
    # print(lista_palavras)
    
    arquivo.close()

    return list(filter(None, lista_palavras))



def remover_palavra(caminho_arquivo, palavra, print_mensagens = False):
    lista_palavras = consultar_palavras(caminho_arquivo)

    if palavra not in lista_palavras:
        if print_mensagens == True:
            print("Palavra \033[1m'" + palavra + "'\033[0m não existe na lista." + '\n')
    
    else:
        lista_palavras.remove(palavra)
        criar_arquivo(caminho_arquivo, lista_palavras)
        
        from processar_listas import processar_lista_para_X_letras
        processar_lista_para_X_letras(var_X = len(palavra))

        if print_mensagens == True:
            print("Palavra \033[1m'" + palavra + "'\033[0m removida!" + '\n')
    
    return lista_palavras



# # INICIALIZAÇÃO DA BLACK LIST
# lista_black_list = ["zaida", "zinir", "xaile"]
# caminho_arquivo_black_list = "Lista de Palavras//black_list.txt"
# # criar_arquivo(caminho_arquivo_black_list, lista_black_list)
# print(consultar_palavras(caminho_arquivo_black_list))

# # INICIALIZAÇÃO DA WHITE LIST
# lista_white_list = ["costas", "pó", "lá", "pé", "raios", "risos", "risão", "bisão", "praça", "sunga", "cunha", "cubar", "vezes"]
# caminho_arquivo_white_list = "Lista de Palavras//white_list.txt"
# criar_arquivo(caminho_arquivo_white_list, lista_white_list)
# print(consultar_palavras(caminho_arquivo_white_list))