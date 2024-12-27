def verificar_letra(var_palavra_escolhida, var_palpite_atual, var_posicao, dict_caracteres_especiais):

    # Como colorir texto no Terminal, em Python: https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30

    var_cod_acerto_letra_e_posicao = 42     # texto normal, fundo verde
    var_cod_acerto_letra_nao_posicao = 103  # texto normal, fundo amarelo
    var_cod_normal = 0                      # fundo sem formatação

    var_palavra_escolhida_sem_caracteres_especiais = ""
    for letra in var_palavra_escolhida:
        var_palavra_escolhida_sem_caracteres_especiais = var_palavra_escolhida_sem_caracteres_especiais + dict_caracteres_especiais.get(letra, letra)
    
    var_palpite_atual_sem_caracteres_especiais = ""
    for letra in var_palpite_atual:
        var_palpite_atual_sem_caracteres_especiais = var_palpite_atual_sem_caracteres_especiais + dict_caracteres_especiais.get(letra, letra)

    # CASO EM QUE A LETRA ESTÁ CERTA, NA POSIÇÃO CERTA
    if dict_caracteres_especiais.get(var_palavra_escolhida[var_posicao], var_palavra_escolhida[var_posicao]) == dict_caracteres_especiais.get(var_palpite_atual[var_posicao], var_palpite_atual[var_posicao]):
        return 1, '\033[' + str(var_cod_acerto_letra_e_posicao) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
    
    
    else:
        for letra in var_palavra_escolhida_sem_caracteres_especiais:
            # CASO EM QUE A LETRA ESTÁ CERTA, NA POSIÇÃO ERRADA
            if (dict_caracteres_especiais.get(var_palpite_atual[var_posicao], var_palpite_atual[var_posicao]) == dict_caracteres_especiais.get(letra, letra)): 

                # SE A LETRA SÓ APARECE UMA VEZ NA PALAVRA ESCOLHIDA, E JÁ ACERTEI, PINTAR DE BRANCO
                if var_palavra_escolhida_sem_caracteres_especiais.count(var_palpite_atual[var_posicao]) == 1:
                    for var_posicao_letra_ja_identificada in range(len(var_palavra_escolhida)):
                        if  (dict_caracteres_especiais.get(var_palavra_escolhida[var_posicao_letra_ja_identificada], var_palavra_escolhida[var_posicao_letra_ja_identificada]) == dict_caracteres_especiais.get(var_palpite_atual[var_posicao], var_palpite_atual[var_posicao])) * \
                            (dict_caracteres_especiais.get(var_palavra_escolhida[var_posicao_letra_ja_identificada], var_palavra_escolhida[var_posicao_letra_ja_identificada]) == dict_caracteres_especiais.get(var_palpite_atual[var_posicao_letra_ja_identificada], var_palpite_atual[var_posicao_letra_ja_identificada])):
                            # print("ok")
                            return 0, '\033[' + str(var_cod_normal) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' ' 
                
                    # SE A LETRA SÓ APARECE UMA VEZ NA PALAVRA ESCOLHIDA, MAS NÃO ACERTEI, PINTAR DE AMARELO
                    if var_palpite_atual_sem_caracteres_especiais.count(var_palpite_atual[var_posicao]) == 1:
                        # print("ok")
                        return 0, '\033[' + str(var_cod_acerto_letra_nao_posicao) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
                    
                    # EXCETO NO CASO EM QUE A LETRA APARECE MAIS DE UMA VEZ NA PALAVRA PALPITADA, PINTAR APENAS A PRIMEIRA DE AMARELO E O RESTO DE BRANCO
                    else:
                        lista_posicoes_letra_escolhida = []
                        for posicao_letra_palpite, letra_palpite in enumerate(var_palpite_atual):
                            if dict_caracteres_especiais.get(letra, letra) == dict_caracteres_especiais.get(letra_palpite, letra_palpite):
                                lista_posicoes_letra_escolhida.append(posicao_letra_palpite)
                        if var_posicao == lista_posicoes_letra_escolhida[0]:
                            # print("ok")
                            return 0, '\033[' + str(var_cod_acerto_letra_nao_posicao) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
                        else:
                            # print("ok")
                            return 0, '\033[' + str(var_cod_normal) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
                   
                
                # SE NÃO ACERTEI A LETRA AINDA, PINTAR DE AMARELO
                else:
                    # print("ok")
                    return 0, '\033[' + str(var_cod_acerto_letra_nao_posicao) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '
                
                
    # CASO EM QUE A LETRA ESTÁ ERRADA, NÃO TEM ELA NA PALAVRA
    # print("ok")
    return 0, '\033[' + str(var_cod_normal) + 'm'+ ' ' + var_palpite_atual[var_posicao] + ' ' + '\033[' + str(var_cod_normal) + 'm' + ' '



def criar_novo_palpite(arquivo_palavras, var_palavra_escolhida, var_palpite, var_qtd_letras, var_palpites_anteriores, dict_caracteres_especiais):

    while True:
        var_palpite_atual = input(">>> Inserir " + str(var_palpite) + "º palpite: ").lower()

        if len(var_palpite_atual) != int(var_qtd_letras):
            print("Inválido! Precisa ter " + var_qtd_letras + " letras." + '\n')

        elif var_palpite_atual not in arquivo_palavras:
            print("Palavra inválida!")
            var_escolha = input(">>> Deseja adicioná-la à white list? (\033[1mS\033[0m para sim, \033[1mR\033[0m para redigitar, qualquer tecla para não) ")  
            if (var_escolha == "S") + (var_escolha == "s"):
                from gerir_listas_manuais import adicionar_palavra
                adicionar_palavra("Lista de Palavras//white_list.txt", var_palpite_atual, print_mensagens = True)
                arquivo_palavras.append(var_palpite_atual)
                break
            if (var_escolha == "R") + (var_escolha == "r"):
                continue
            else:
                break

        else:
            break  

    var_resultado_palpite = var_palpites_anteriores + '\n'
    var_pontos = 0
    var_resultado_jogo = False
    
    for var_posicao in range(len(var_palpite_atual)):
        var_ponto_letra, var_resultado_palpite_letra = verificar_letra(var_palavra_escolhida, var_palpite_atual.upper(), var_posicao, dict_caracteres_especiais)
        var_resultado_palpite = var_resultado_palpite + var_resultado_palpite_letra
        var_pontos = var_pontos + var_ponto_letra

        # print(str(var_pontos) + " pontos")
        if var_pontos == int(var_qtd_letras):
            var_resultado_jogo = "Vitória"
        else:
            var_resultado_jogo = "Derrota"
    

    var_resultado_palpite = var_resultado_palpite + '\n'
    print(var_resultado_palpite)
    
    return var_resultado_jogo, var_resultado_palpite, var_palpite_atual



def jogar_termo(var_nome_jogador = "jogador0"):
    from gerir_listas_manuais import consultar_palavras
    from gerir_historico import criar_novo_resultado

    from main import check_and_install_packages
    lista_libraries = ["datetime", "random"]
    check_and_install_packages(lista_libraries)
    import datetime
    import random

    var_escolha_jogador = input(">>> O jogador atual é o \033[1m'" + var_nome_jogador + "\033[0m'. Deseja alterar? (\033[1mS\033[0m para Sim, qualquer tecla para Não) ")
    if (var_escolha_jogador == "S") + (var_escolha_jogador == "s"):
        while True:
            var_nome_jogador = input(">>> Insira seu \033[1mnome de jogador\033[0m: ")
            if len(var_nome_jogador) <= 2:
                print("Nome inválido! Insira um nome maior.")
            else:
                break
    
    while True:
        var_qtd_letras = input(">>> Quer jogar com quantas letras? (\033[1mM\033[0m para voltar ao Menu, ou \033[1mum número de 3 a 15\033[0m, ou qualquer tecla para jogar com \033[1m5 letras\033[0m) ")
        if (var_qtd_letras == 'M') + (var_qtd_letras == 'm'):
            return False
        
        elif var_qtd_letras.isdigit(): # verifica se é um dígito > 0
            if (int(var_qtd_letras) < 3) + (int(var_qtd_letras) > 15) :
                print("O número de letras deve ser entre 3 e 15!" + '\n')
            else:
                break
        else:
            var_qtd_letras = 5
            break
        
    try:
        arquivo_palavras = consultar_palavras("Lista de Palavras//Listas de Palavras para o Jogo//lista_palavras_" + var_qtd_letras + "_letras.txt")
    except:
        from processar_listas import processar_lista_para_X_letras
        arquivo_palavras = processar_lista_para_X_letras(var_X = int(var_qtd_letras)).split('\n')

    
    dict_caracteres_especiais = {
        "Á": "A",
        "Â": "A",
        "Ã": "A",
        "É": "E",
        "Ê": "E",
        "Í": "I",
        "Î": "I",
        "Ó": "O",
        "Ô": "O",
        "Õ": "O",
        "Ú": "U",
        "Û": "U",
        "Ç": "C",
    }

    arquivo_palavras_com_e_sem_caracteres_especiais = arquivo_palavras.copy()
    for palavra in arquivo_palavras:
        palavra_sem_caracteres_especiais = ""
        for letra in palavra.upper():
            palavra_sem_caracteres_especiais = palavra_sem_caracteres_especiais + dict_caracteres_especiais.get(letra, letra)
        if palavra_sem_caracteres_especiais.lower() != palavra.lower():
            # var_lista_palavras_com_X_letras = var_lista_palavras_com_X_letras + palavra_sem_caracteres_especiais.lower() + '\n'
            arquivo_palavras_com_e_sem_caracteres_especiais.append(palavra_sem_caracteres_especiais.lower())
    
    # print(arquivo_palavras)


    var_palavra_escolhida = arquivo_palavras[random.randint(0, len(arquivo_palavras)-2)]
    
    # print(var_palavra_escolhida)


    qtd_max_palpites = min(15, int(var_qtd_letras) + 1)
    var_palpites_anteriores = ""
    lista_palpites = []
    for var_num_palpite in range(1, qtd_max_palpites+1):
        print("Você tem "+ "\033[1m" + str(qtd_max_palpites + 1 - var_num_palpite) + " palpites" + "\033[0m." + '\n')
        var_resultado_jogo, var_palpites_anteriores, var_palpite_atual = criar_novo_palpite(
            arquivo_palavras_com_e_sem_caracteres_especiais,
            var_palavra_escolhida.upper(),
            var_num_palpite,
            var_qtd_letras,
            var_palpites_anteriores,
            dict_caracteres_especiais)
        
        lista_palpites.append(var_palpite_atual.upper())
        
        if var_resultado_jogo == "Vitória":
            print("PARABÉNS 🎉, VOCÊ ACERTOU EM " + str(var_num_palpite) + " PALPITE(S)." + '\n')
            break

    if var_resultado_jogo == "Derrota":
        print("Você perdeu 😢. A palavra era \033[1m'" + var_palavra_escolhida.upper() +"'\033[0m.")

    var_num_palpite_resultado = var_num_palpite
    while var_num_palpite < 15:
        lista_palpites.append(None)
        var_num_palpite = var_num_palpite + 1

    # Data, Jogador, Palavra, Qtd palpites, Resultado, Palpite 1,  Palpite 2, Palpite 3,  Palpite 4, Palpite 5,  Palpite 6, Palpite 7,  Palpite 8, Palpite 9,  Palpite 10, Palpite 11,  Palpite 12, Palpite 13,  Palpite 14, Palpite 15  
    criar_novo_resultado([datetime.datetime.now(), var_nome_jogador, var_palavra_escolhida.upper(), var_num_palpite_resultado, var_resultado_jogo] + lista_palpites)
    
    return var_nome_jogador

    

if __name__ == "__main__":
    jogar_termo()