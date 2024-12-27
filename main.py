import importlib
import subprocess
import sys



def check_and_install_packages(packages):

    # FONTE: https://stackoverflow.com/questions/76386461/how-to-use-python-to-check-for-and-install-librarys

    for package in packages:
        try:
            importlib.import_module(package)
            # print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} installed successfully.")



def gerir_listas_manuais(var_caminho, var_tipo_lista, var_tempo_sleep_padrao):
    from gerir_listas_manuais import consultar_palavras, adicionar_palavra, remover_palavra

    while True:
        var_escolha_black_list = input(">>> Deseja adicionar \033[1m(A)\033[0m, remover \033[1m(R)\033[0m, ver \033[1m(V)\033[0m palavras da " + var_tipo_lista + ", ou sair \033[1m(S)\033[0m? ")

        if (var_escolha_black_list == "A") + (var_escolha_black_list == "a"):
            var_palavra_adicionar = input(">>> Qual palavra adicionar? ")
            adicionar_palavra(var_caminho, var_palavra_adicionar, print_mensagens = True)

        elif (var_escolha_black_list == "R") + (var_escolha_black_list == "r"):
            var_palavra_remover = input(">>> Qual palavra remover? ")
            remover_palavra(var_caminho, var_palavra_remover, print_mensagens = True)

        elif (var_escolha_black_list == "V") + (var_escolha_black_list == "v"):
            print("Esta é a lista de palavras presente na \033[1m" + var_tipo_lista + "\033[0m:")
            print(consultar_palavras(var_caminho))
            print()

        elif (var_escolha_black_list == "S") + (var_escolha_black_list == "s"):
            break

        else:
            print('\n' + "Opção inválida!" +  '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages



def main():
    lista_libraries = ["time", "pandas"]
    check_and_install_packages(lista_libraries)
    for library in lista_libraries:
        # importlib.import_module(library)
        module_obj = __import__(library)
          # create a global object containging our module
        globals()[library] = module_obj

    var_tempo_sleep_padrao = 2

    from gerir_historico import criar_novo_historico, ver_historico, ver_jogadores, gerar_grafico
    criar_novo_historico(sobrescrever = False)
    var_nome_jogador = "jogador0"

    # MENU
    while True:
        print(
            '\n'
            "=========== MENU ===========" + '\n'
            "\033[1m1\033[0m: começar novo jogo" + '\n'
            "\033[1m2\033[0m: importar novas palavras" + '\n'
            "\033[1m3\033[0m: ver histórico de jogos" + '\n'
            "\033[1m4\033[0m: adicionar e/ou remover palavras da black list" + '\n'
            "\033[1m5\033[0m: adicionar e/ou remover palavras da white list" + '\n'
            '\n'
            "\033[1mS\033[0m: Sair" + '\n'
        )
        var_escolha = input (">>> Escolha uma opção: ")
        # print("\n")

        if var_escolha == '1':
            from jogo import jogar_termo
            var_nome_jogador = jogar_termo(var_nome_jogador)
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '2':
            from processar_listas import processar_lista_para_X_letras
            processar_lista_para_X_letras()
            print('\n' + "Arquivo com as palavras importado!" + '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '3':
            var_lista_jogadores = ver_jogadores()
            if var_lista_jogadores.any() != False:
                print("Os jogadores com histórico disponível são: ")
                print(var_lista_jogadores)
                print()
                while True:
                    var_nome_jogador_historico = input(">>> Deseja ver o Histórico de qual jogador? (\033[1mH\033[0m para ver Histórico geral) ")
                    if (var_nome_jogador_historico == "H") + (var_nome_jogador_historico == "h"):
                        tabela_jogador = ver_historico(False)
                        break
                    elif var_nome_jogador_historico in var_lista_jogadores:
                        tabela_jogador = ver_historico(var_nome_jogador_historico)
                        break
                    else:
                        print("Jogador indisponível!")
                        pass
                # print(tabela_jogador)
                gerar_grafico(tabela_jogador, var_nome_jogador_historico)
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '4':
            gerir_listas_manuais("Lista de Palavras//black_list.txt", "black list", var_tempo_sleep_padrao)
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages
            
        elif var_escolha == '5':
            gerir_listas_manuais("Lista de Palavras//white_list.txt", "white list", var_tempo_sleep_padrao)
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif (var_escolha == 'S') + (var_escolha == 's'):
            print('\n' + "Obrigado por jogar!" + "\n")
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages
            break


        else:
            print('\n' + "Opção inválida!" +  '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages



if __name__ == "__main__":
    main()