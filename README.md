# Como jogar?


# Fontes das lista de palavras em português
**Essa foi a parte mais difícil do projeto!**

As listas de palavras podem conter um excesso de palavras, como verbos conjugados ([neste caso](https://www.ime.usp.br/~pf/dicios/), por exemplo) ou palavras que eu simplesmente não conheço e atrapalhariam o jogo, deixando-o excessivamente complexo e desinteressante, caso o jogador não saiba qual é a palavra. Também achei [listas bem grandes e completas](https://github.com/titoBouzout/Dictionaries/blob/master/Portuguese%20(Brazilian).txt), mas que ao mesmo tempo não continham palavras (que eu suponho que sejam) usuais, como _carta_ e _testa_.

Tentei buscar por listas de palavras que contivessem as palavras mais comuns/frequentes/usadas no idioma. Encontrei algo assim no site [Dicio](https://www.dicio.com.br/lista-de-palavras/), mas ocorreu o problema inverso: poucas palavras, uma lista muito pequena.

Por fim, a melhor solução encontrada até o momento é uma lista de palavras utilizada para a metodologia de criação de senhas chamada [**Diceware**](https://github.com/thoughtworks/dadoware/blob/master/fontes/com_acentos.txt). Inclusive essa metodologia é bem interessante, pois **usa palavras comuns para gerar senhas fortes!** Fascinante e útil para o meu projeto.



# TO-DO
- ~~Verificar se a palavra inserida é válida (usar a própria lista de palavras)~~
- ~~Verificar letras com caracteres especiais~~
    - ~~Verificar se a palavra inserida é válida, quando ela tem caracteres especiais~~
- ~~Criar condições de vitória~~
- ~~Criar condição de derrota~~
- ~~Adicionar palavras ao white list (inclusive enquanto está jogando)~~
    - ~~Criar arquivo com palavras da white list~~
    - ~~No processamento da white list, adicionar ao arquivo da lista de palavras padrão~~
    - ~~No meio do jogo, quando o jogador colocar uma palavra inválida, perguntar se o jogador quer adicioná-la à white list~~
- Adicionar resultado do jogo ao histórico
    - ~~Criar histórico por jogador (criar um arquivo com o nome do jogador)~~
    - ~~Adaptar a tabela de jogos do jogador para uma tabela geral, com as colunas~~:
        - ID do jogo
        - Timestamp
        - Nome do jogador
        - Cada um dos palpites do jogador
        - Quantidade de jogadas total
    - Corrigir problema de enconding (na palavra 'Vitória')
    - Criar uma função que identifica se o jogador ganhou ou não, com base na quantidade de palpites e quantidade de jogadas total
    - ~~Permitir ver todos os jogadores, assim como escolher quem é o usuário que está jogando~~
    - Criar um gráfico dos resultados do jogador
- Adicionar regras do jogo ao Readme

# BUGs
- Quando vai jogar com 3 letras, e coloca as palavras "CÉU" e "MAR"