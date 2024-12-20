def processar_lista_para_X_letras(var_X = None):
    from gerir_listas_manuais import consultar_palavras

    # lista_palavras = consultar_palavras("Lista de Palavras//br-utf8.txt")
    # lista_palavras = consultar_palavras("Lista de Palavras//portuguese.txt")
    # lista_palavras = consultar_palavras("Lista de Palavras//lista_tratada_dicio.txt")
    lista_palavras = consultar_palavras("Lista de Palavras//com_acentos.txt")

    lista_white_list = consultar_palavras("Lista de Palavras//white_list.txt")
    lista_black_list = consultar_palavras("Lista de Palavras//black_list.txt")

    lista_palavras = lista_palavras + lista_white_list
    for palavra_black_list in lista_black_list:
        lista_palavras.remove(palavra_black_list)

    # print(lista_palavras)
    
    try:
        if var_X is None:
            var_X = int(input(">>> Quantas letras nas palavras? "))
        
        if (var_X <= 0) * (var_X > 15) :
            print("O número de letras deve ser entre 1 e 15!")
            return False
        
    except:
        print("O número de letras deve ser inteiro!")
        return False

    var_lista_palavras_com_X_letras = ""

    for palavra in lista_palavras:
        # print("'" + palavra.strip() + "', qtd letras: " + str(len(palavra.strip())))

    # var_continuar = input("Continuar? (Y para sim) ")
    # if (var_continuar == "y") | (var_continuar == "Y"):
        if len(palavra.strip()) == var_X:
            # print("Palavra '" + palavra + "' adicionada")
            # lista_palavras_com_X_letras.append(palavra)
            var_lista_palavras_com_X_letras = var_lista_palavras_com_X_letras + palavra.lower() + '\n'


    # else:
        # print("Palavra '" + palavra + "' NÃO adicionada" + '\n')


    # print(lista_palavras_com_X_letras)    # Imprime o arquivo
    # print(var_lista_palavras_com_X_letras)    # Imprime o arquivo

    try:
        arquivo_palavras_com_X_letras = open("Lista de Palavras//Listas de Palavras para o Jogo//lista_palavras_"+str(var_X)+"_letras.txt", "x", encoding="utf-8")
    except:
        arquivo_palavras_com_X_letras = open("Lista de Palavras//Listas de Palavras para o Jogo//lista_palavras_"+str(var_X)+"_letras.txt", "w", encoding="utf-8")
    
    arquivo_palavras_com_X_letras.write(var_lista_palavras_com_X_letras)
    arquivo_palavras_com_X_letras.close()

    return var_lista_palavras_com_X_letras



if __name__ == "__main__":
    processar_lista_para_X_letras()