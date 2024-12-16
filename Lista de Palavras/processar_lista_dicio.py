def main():
    arquivo_todas_as_palavras = open("Lista de Palavras//lista_dicio.txt", "r", encoding="utf-8")
    conteudo = arquivo_todas_as_palavras.read()
    lista_palavras = conteudo.split('\n')

    # print(len(lista_palavras))

    lista_completa = ""
    for sub_lista in lista_palavras:
        sub_lista = sub_lista.split(", ")
        for palavra in sub_lista:
            lista_completa = lista_completa + palavra + '\n'

    lista_completa = list(dict.fromkeys(lista_completa.split('\n')))
    
    # print(lista_completa)
    # print(len(lista_completa))

    lista_exportacao = ""
    for palavra in lista_completa:
        lista_exportacao = lista_exportacao + palavra + '\n'
        
    try:
        arquivo_tratado_dicio = open("Lista de Palavras//lista_tratada_dicio.txt", "x", encoding="utf-8")
    except:
        arquivo_tratado_dicio = open("Lista de Palavras//lista_tratada_dicio.txt", "w", encoding="utf-8")
        
    arquivo_tratado_dicio.write(lista_exportacao)
    arquivo_tratado_dicio.close()


if __name__ == "__main__":
    main()