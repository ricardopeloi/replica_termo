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


def processar_lista_para_X_letras():
    from processar_lista_para_X_letras import main
    main()

def jogo():
    from jogo import main
    main()


def main():
    lista_libraries = ["time"]
    check_and_install_packages(lista_libraries)
    for library in lista_libraries:
        # importlib.import_module(library)
        module_obj = __import__(library)
          # create a global object containging our module
        globals()[library] = module_obj


    var_tempo_sleep_padrao = 2

    while True:
        print(
            '\n'
            
            "=========== MENU ===========" + '\n'
            "1: começar novo jogo" + '\n'
            "2: importar novas palavras" + '\n'
            "3: ver histórico de jogos" + '\n'
            "4: adicionar e/ou remover palavras da black list" + '\n'
            '\n'
            "0: Sair" + '\n'
        )
        var_escolha = input (">>> Escolha uma opção: ")
        # print("\n")


        if var_escolha == '1':
            jogo()
            # print("Novo jogo" + '\n')

        elif var_escolha == '2':
            processar_lista_para_X_letras()
            print('\n' + "Arquivo com as palavras importado!" + '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '3':
            print("---Em construção!---" + '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '4':
            print("---Em construção!---" + '\n')
            lista_black_list = ["ábêcê", "alvar", "azibó", "cdlvi", "color", "cxxxi", "équis", "gauro", "labro", "lízia", "mdlvi", "mdxxx", "pruir", "rilar", "suruí", "úbere", "xelma", ]
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '5':
            print("---Em construção!---" + '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages

        elif var_escolha == '0':
            print('\n' + "Obrigado por jogar!" + "\n")
            break

        else:
            print('\n' + "Opção inválida!" +  '\n')
            time.sleep(var_tempo_sleep_padrao) # type: ignore # ver seção check_and_install_packages


if __name__ == "__main__":
    main()