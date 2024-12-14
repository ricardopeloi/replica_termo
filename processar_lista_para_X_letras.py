def main():
    # arquivo_todas_as_palavras = open("Lista de Palavras//br-utf8.txt", "r", encoding="utf-8") # contém conjugações, o que deixa o jogo excessivamente complexo e desinteressante
    arquivo_todas_as_palavras = open("Lista de Palavras//portuguese.txt", "r", encoding="utf-8")
    conteudo = arquivo_todas_as_palavras.read()
    # print(content)

    lista_palavras = conteudo.split('\n')
    # print(lista_palavras)
    
    try:
        var_X = int(input(">>> Quantas letras nas palavras? "))
        if var_X <= 0 :
            print("O número deve ser maior ou igual a 0!")
            return False
    except:
        print("O número deve ser inteiro!")
        return False

    var_lista_palavras_com_X_letras = ""

    for palavra in lista_palavras:
        # print("'" + palavra.strip() + "', qtd letras: " + str(len(palavra.strip())))

        # var_continuar = input("Continuar? (Y para sim) ")
        # if (var_continuar == "y") | (var_continuar == "Y"):
        if len(palavra.strip()) == var_X:
            # print("Palavra '" + palavra + "' adicionada")
            # lista_palavras_com_X_letras.append(palavra)
            var_lista_palavras_com_X_letras = var_lista_palavras_com_X_letras + palavra + '\n'
        # else:
            # print("Palavra '" + palavra + "' NÃO adicionada" + '\n')

    # print(lista_palavras_com_X_letras)    # Imprime o arquivo
    # print(var_lista_palavras_com_X_letras)    # Imprime o arquivo

    try:
        arquivo_palavras_com_X_letras = open("Lista de Palavras//lista_palavras_"+str(var_X)+"_letras.txt", "x", encoding="utf-8")
    except:
        arquivo_palavras_com_X_letras = open("Lista de Palavras//lista_palavras_"+str(var_X)+"_letras.txt", "w", encoding="utf-8")
    
    arquivo_palavras_com_X_letras.write(var_lista_palavras_com_X_letras)
    arquivo_palavras_com_X_letras.close()


if __name__ == "__main__":
    main()
