# Regras do jogo
Bem vindo(a) ao jogo **_Replica Termo_**!

Caso pareça familiar para você, é porque me inspirei fortemente no queridíssimo [Term.ooo](https://term.ooo/). Esse é um joguinho com regras específicas, na qual o jogador deve acertar qual é a palavra do dia a partir dessas regras.

O jogo é atualizado diariamente, todas as palavras possuem 5 letras, e são 3 modos de jogo:
1. Acertar _uma_ palavra apenas, em 6 tentativas, o que é chamado de _Termo_
2. Acertar _duas_ palavras ao mesmo tempo, em 7 tentativas, o que é chamado de _Dueto_
3. Acertar _quatro_ palavras ao mesmo tempo, em 9 tentativas, o que é chamado de _Quarteto_

No meu jogo **_Replica Termo_**, temos apenas a opção de jogar a opção de uma palavra, contudo, não é necessário aguardar atualizações diárias: você pode jogar quantas vezes quiser! E se você quiser jogar com uma quantidade diferente de 5 letras, você pode!

Ao executar o jogo, o jogador se depara com 5 opções. Toda a interação é feita via Terminal, e todos os textos que o jogador precisa interagir são antecedidos por **>>>**.

## <a name="regras1"></a>1: começar novo jogo
Esse é o modo padrão, em que o jogador inicia um novo jogo.

O jogo te dá a opção de escolher o nome do jogador (o que é bacana caso você queira ver o [Histórico de resultados de jogos passados, por jogador](#regras2)). Caso não queira ver histórico, ou você seja o único jogador, basta usar a opção padrão (_jogador0_), e digitar _qualquer tecla_ (incluindo _Enter_) para começar a jogar.

Em seguida, o jogo pergunta quantas letras o jogador quer usar no jogo. Se o jogador apertar _Enter_, o jogo começa com **5 letras**. Caso queira especificar, o jogador por escolher **entre 3 e 15 letras**!

Uma vez iniciado, o jogo escolherá uma palavra. Agora devemos adivinhá-la. Basta escrever uma palavra (com a quantidade de letras escolhida). O jogo vai pintando as letras do palpite do jogador. 

Por exemplo, na imagem abaixo vemos a letra **_E_**, que está na posição correta. Já a letra **_A_** existe na palavra, mas está na posição errada. As demais letras (L, S e O) não existem na palavra.

<p align="center">
  <img src="https://github.com/ricardopeloi/replica_termo/blob/main/Imagens%20Readme/Como_jogar_01.png?raw=true" width="200" title="Exemplo de 1 acerto na posição, e outro acerto fora de posição">
</p>

Os acentos e caracteres especiais (como o til na letra **_Ã_**) não fazem diferença, isto é, nesse caso, a letra A e a letra Ã são equivalentes.

Além disso, o jogo também indica quantos palpites restantes o jogador tem.

Caso o jogador use todos os seus palpites e não acerte a palavra, ele perde o jogo 😢

Se acertar a palavra dentro do número de palpites disponíveis, você ganhou 🎉!

<p align="center">
  <img src="https://github.com/ricardopeloi/replica_termo/blob/main/Imagens%20Readme/Como_jogar_02.png?raw=true" width="300" title="Resultado positivo de um jogo">
</p>

No final do jogo, todos os palpites usados e os dados do jogo (incluindo o nome do jogador escolhido)[são salvos em um arquivo CSV](#regras2).


## <a name="regras2"></a>2: ver histórico de jogos
Conforme o jogador vai jogando, um arquivo salva o histórico de resultados, sejam positivos ou não.

[Este arquivo é um CSV](https://github.com/ricardopeloi/replica_termo/blob/main/Hist%C3%B3rico%20dos%20jogadores/Hist%C3%B3rico.csv), e que pode ser utilizado para fazer a análise que você quiser!

A análise mais básica e presente no jogo é ver um gráfico com os resultados. O jogo pergunta de qual jogador se deseja ver os resultados, ou todos (digitando **_H_**).

Por exemplo, esse é o meu histórico até o momento:

<p align="center">
  <img src="https://github.com/ricardopeloi/replica_termo/blob/main/Imagens%20Readme/Como_jogar_03.png?raw=true" width="300" title="Exemplo de gráfico com os resultados dos jogos">
</p>


## <a name="regras3e4"></a>3: adicionar e/ou remover palavras da black list; e 4: adicionar e/ou remover palavras da white list
Ao construir o jogo, [um dos maiores desafios foi criar a lista de palavras](#listaspalavras).

Eu reparei que seria necessário incluir ferramentas para adicionar ou remover palavras que estejam presentes no jogo. Porque assim fica mais divertido, jogar com palavras conhecidas e não muito mirabolantes. Palavras conhecidas, não necessariamente fáceis!

No caso das palavras adicionadas ao jogo, trata-se da **white list**. E as removidas, a **black list**.

Em ambos os casos, o jogador pode adicionar palavras às listas, remover palavras da lista, ou simplesmente ver as listas. Por exemplo, olha só as palavras que tive que **remover do jogo** (adicionando-as à black list), até o momento:

<p align="center">
  <img src="https://github.com/ricardopeloi/replica_termo/blob/main/Imagens%20Readme/Como_jogar_04.png?raw=true" width="500" title="Exemplo de palavras presentes na black list, ou seja, removidas do jogo">
</p>

O jogador também consegue, **durante o jogo, adicionar palavras ao jogo** (via white list). Por exemplo, se ele adicionar uma palavra e acha que ela deveria estar presente na lista de palavras do jogo, basta escrever **_S_**! Caso tenha escrito uma palavra inválida de fato, pode escrever **_R_** para redigitar. O jogo também permite usar palavras inválidas para jogar, apertando qualquer outra tecla (mas eu não recomendo, e o Termo original, também não).

<p align="center">
  <img src="https://github.com/ricardopeloi/replica_termo/blob/main/Imagens%20Readme/Como_jogar_05.png?raw=true" width="500" title="Adicionando palavras à white list">
</p>


# <a name="listaspalavras"></a>Fontes das lista de palavras em português
**Essa foi a parte mais difícil do projeto!**

As listas de palavras podem conter um excesso de palavras, como verbos conjugados ([neste caso](https://www.ime.usp.br/~pf/dicios/), por exemplo) ou palavras que eu simplesmente não conheço e atrapalhariam o jogo, deixando-o excessivamente complexo e desinteressante, caso o jogador não saiba qual é a palavra. Também achei [listas bem grandes e completas](https://github.com/titoBouzout/Dictionaries/blob/master/Portuguese%20(Brazilian).txt), mas que ao mesmo tempo não continham palavras (que eu suponho que sejam) usuais, como _carta_ e _testa_.

Tentei buscar por listas de palavras que contivessem as palavras mais comuns/frequentes/usadas no idioma. Encontrei algo assim no site [Dicio](https://www.dicio.com.br/lista-de-palavras/), mas ocorreu o problema inverso: poucas palavras, uma lista muito pequena.

Por fim, a melhor solução encontrada até o momento é uma lista de palavras utilizada para a metodologia de criação de senhas chamada [**Diceware**](https://github.com/thoughtworks/dadoware/blob/master/fontes/com_acentos.txt). Inclusive essa metodologia é bem interessante, pois **usa palavras comuns para gerar senhas fortes!** Fascinante e útil para o meu projeto.

## Como jogar
Atualmente, a única forma de jogar é utilizando o meu [repositório do Github](https://github.com/ricardopeloi/replica_termo), isto é, fazer um clone do repositório e rodar na sua máquina. Isto exige algum nível de conhecimento técnico, [mas nada absurdo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

Uma alternativa é usar o **Codespaces do Github**, que é muitíssimo simples e exige apenas uma conta no Github. Esse artigo [aqui](https://agnieszkapasieka.medium.com/run-python-scripts-directly-from-github-repository-using-codespaces-902468f50b0a), que é excelente e muito objetivo, explica como fazer isso.

Em ambos os casos, basta rodar o arquivo _main.py_ para iniciar o jogo e ver o menu:

<p align="center">
  <img src="https://github.com/ricardopeloi/replica_termo/blob/main/Imagens%20Readme/Como_jogar_06.png?raw=true" width="300" title="Adicionando palavras à white list">
</p>

Daí em diante, é só curtir o jogo! 💗

Caso queira ter seu próprio histórico, lembre-se de apagar o arquivo _Histórico.csv_, na pasta _Histórico dos jogadores_.

# O que aprendi com esse projeto
1. Tudo que eu havia feito em Python, na minha vida, até então, foi através de **Jupyter notebooks** ([veja minha biblioteca de funções de Data Science, por exemplo](https://github.com/ricardopeloi/minha_biblioteca_python/tree/main)). Nesse projeto usei arquivos em .py, e interações (do jogador) pelo Terminal. Isso demandou que eu configurasse um ambiente;
2. Integrar as funções de diferentes arquivos .py entre eles, ou seja, um arquivo para a função principal, outro para o jogo, outro para o histórico, etc. Todas as integrações de código que havia feito até então eram bibliotecas "padrão" do Python, como Pandas, Matplotlib, Keras, etc. Agora tenho como usar meus próprios pacotinhos, e talvez até eu consiga transformar minha biblioteca de funções em algo mais robusto do que um notebook que eu sempre fico picotando. Inclusive, usei uma das minhas funções já prontas para [criar o gráfico aqui do jogo](#regras2);
3. Pratiquei muito o uso de versionamento em Git, mantendo sempre meus arquivos atualizados e compartilhando a evolução do projeto aqui no Github, passo a passo. Até a conclusão do projeto (27/12/2024), foram quase 30 commits;
4. [Colorir o Terminal](#regras1). Achei que não seria possível e teria que criar uma interface gráfica para o jogo, mas o Terminal permitiu atender perfeitamente o que eu imaginava no início. Ainda não aprendi a fazer uma interface gráfica, fica para o próximo projeto;
5. Uso de Markdown, com esse Readme. Aprendi a usar links internos (_âncoras_), diversos tipos de formatação, inserção de imagens e links, bullet points (numerados ou não) e criar minha [To-Do list](#to_do) (cujos itens foram sobreescritos conforme avancei no projeto).


# <a name="to_do"></a>TO-DO
## Concluído até 27/12/2024
- ~~Verificar se a palavra inserida é válida (usar a própria lista de palavras)~~
- ~~Verificar letras com caracteres especiais~~
    - ~~Verificar se a palavra inserida é válida, quando ela tem caracteres especiais~~
- ~~Criar condições de vitória~~
- ~~Criar condição de derrota~~
- ~~Adicionar palavras ao white list (inclusive enquanto está jogando)~~
    - ~~Criar arquivo com palavras da white list~~
    - ~~No processamento da white list, adicionar ao arquivo da lista de palavras padrão~~
    - ~~No meio do jogo, quando o jogador colocar uma palavra inválida, perguntar se o jogador quer adicioná-la à white list~~
- ~~Adicionar resultado do jogo ao histórico~~
    - ~~Criar histórico por jogador (criar um arquivo com o nome do jogador)~~
    - ~~Adaptar a tabela de jogos do jogador para uma tabela geral, com as colunas~~:
        - ~~ID do jogo~~
        - ~~Timestamp~~
        - ~~Nome do jogador~~
        - ~~Cada um dos palpites do jogador~~
        - ~~Quantidade de jogadas total~~
    - ~~Corrigir problema de enconding (na palavra 'Vitória')~~
    - ~~Permitir ver todos os jogadores, assim como escolher quem é o usuário que está jogando~~
    - ~~Criar um gráfico dos resultados do jogador~~
- ~~Adicionar regras do jogo ao Readme~~

## Em aberto (30/12)
- Publicar no Linkedin
- Adicionar uma forma de jogar online
  - ~~Testes no Codespaces do Github~~
  - Streamlit?