def main():
    arquivo_todas_as_palavras = open("br-utf8.txt", "r", encoding="utf-8")
    conteudo = arquivo_todas_as_palavras.read()
    # print(content)

    lista_palavras = conteudo.split('\n')
    
    var_X = 5
    # var_X = input("Quantas letras nas palavras? ")
    # lista_palavras_com_X_letras = []

    var_lista_palavras_com_X_letras = ""

    for palavra in lista_palavras:
        # print("'" + palavra.strip() + "', qtd letras: " + str(len(palavra.strip())))

        # var_continuar = input("Continuar? ")
        # if (var_continuar == "y") | (var_continuar == "Y"):
        if len(palavra.strip()) == var_X:
            # print("Palavra '" + palavra + "' adicionada")
            # lista_palavras_com_X_letras.append(palavra)
            var_lista_palavras_com_X_letras = var_lista_palavras_com_X_letras + palavra + '\n'
        # else:
            # print("Palavra '" + palavra + "' NÃO adicionada" + '\n')
        # else:
            # break

    # print(lista_palavras_com_X_letras)    # Imprime o arquivo
    # print(var_lista_palavras_com_X_letras)

    try:
        arquivo_palavras_com_X_letras = open("lista_palavras_"+str(var_X)+"_letras.txt", "x")
    except:
        arquivo_palavras_com_X_letras = open("lista_palavras_"+str(var_X)+"_letras.txt", "w")
    
    arquivo_palavras_com_X_letras.write(var_lista_palavras_com_X_letras)
    arquivo_palavras_com_X_letras.close()


if __name__ == "__main__":
    main()
