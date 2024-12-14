import random

def main():
    var_qtd_letras = input(">>> Quer jogar com quantas letras? ")
    
    arquivo_palavras = open("Lista de Palavras//lista_palavras_" + var_qtd_letras + "_letras.txt", "r", encoding="latin-1") \
        .read() \
        .split('\n')

    # print(arquivo_palavras)

    palavra_escolhida = arquivo_palavras[random.randint(0, len(arquivo_palavras)-2)]
    print(palavra_escolhida)

    var_palpite = 1
    palpite_atual = input(">>> Inserir " + str(var_palpite) + "º palpite: ")
    if len(palpite_atual) != int(var_qtd_letras):
        print("Inválido! Precisa ter " + var_qtd_letras + " letras.")
        palpite_atual = input(">>> Inserir " + str(var_palpite) + "º palpite: ")

    var_cod_acerto_letra_e_posicao = 42 # texto branco, fundo verde
    var_cod_acerto_letra = 103          # texto branco, fundo amarelo
    var_cod_normal = 0                  # fundo sem formatação
    
    
    # Como colorir texto no Terminal, em Python: https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30
    
    print(
        '\033[' + str(var_cod_acerto_letra) + 'm'+ ' ' + 'A' + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
        '\033[' + str(var_cod_acerto_letra_e_posicao) + 'm'+ ' ' + 'B' + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
        ' _ '
        ' _ '
        ' _ '
    )

    print(
        '\033[' + str(var_cod_acerto_letra_e_posicao) + 'm'+ ' ' + 'A' + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
        '\033[' + str(var_cod_acerto_letra) + 'm'+ ' ' + 'B' + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
        ' _ '
        ' _ '
        ' _ '
    )



if __name__ == "__main__":
    main()