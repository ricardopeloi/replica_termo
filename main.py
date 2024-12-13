def instalar_bibliotecas():
    # !pip install 
    return True

def main():
    # instalar_bibliotecas()

    # print("Hello World!")

    while True:
        print(
            "1: começar novo jogo" + '\n'
        )
        var_escolha = input ("Escolha uma opção: ")
        # print("\n")


        if var_escolha == '1':
            print("Novo jogo" + '\n')

        else:
            print("Obrigado por jogar!" + "\n")
            break
        

if __name__ == "__main__":
    main()
