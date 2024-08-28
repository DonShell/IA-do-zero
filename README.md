Bem vindo(a) ao meu projeto de Inteligencia Artificial.
Este projeto surgiu com o intuito de realizar aprendizado de maquina sem uso de bibliotecas ou metodologias prontas. Após algum tempo de filosofia elaborei meu conceito de aprendizado (analizar padrões que se repetem). este principio foi codificado em Python3 e atingiu o resultado esperado.

Este é um pequeno modelo o qual você digita manualmente uma sequancia de caracteres seguidos de Enter. o software identificará quando você iniciar uma repetição e cauculará a probabilidade da proxima letr acom base nas anteriores.

Este modelo está em branco, não possui conhecimento prévio do dicionario ou de quaisquer regras de logica ou gramatica, mas pode ser adaptado para tais análises.

!Exemplo de uso!

faremos duas sequencias simples de palavras

'codigo'

'de'

'cor'

(apague os arquivos .txt)

no Console/Shell:

```
>python3 .\nucleo.py
digite um valor de entrada '{}' para sequencia programada:
>c
>o
>d
>i
>g
>o
!- ha uma lista de previsoes de pelo menos um digito -!
precorrendo vetor prev: i =0
percorrendo vetor prev[0]: i2 = 0
adcionanto valores a lista score com indice string um padrao de resposta
1 pontos para d
pontos acomulados: 1
100.0% para 'd'
previsao: d
```

note que antes da letra 'o' se repetir o programa não havia previsões, pois ele nunca vira aquela sequencia antes, porem ao digitarmos o ultimo 'o' a previsão dele era de 100% para 'o', pois na realidade dele só foi evidenciado a letra 'd' após a letra 'o'. Vamos ensina-lo que existem outras palavras, ultilizarei um '-' (travessão) para separarmos as palavras de forma mais visivel:

```
>-
```

começaremos agora outra palavra,

```
>d
100.0% para 'i'
previsao: i
>e
>-
100.0% para 'd'
previsao: d
>c
100.0% para 'o'
previsao: o
>o
pontos acomulados: 2
50.0% para 'd'
50.0% para '-'
previsao: -
digite um valor de entrada '{}' para sequencia programada:100.0% para 'o'
100.0% para 'o'
```

percebe-se que agora ele está em duvia se a palavra sendo digitada é 'codigo' ou o final dela '-'

```
>r
>-
```

se começarmos a palavra daprimera letra ele preverá as proximas, se começarmos do meio, também:

```
>d
100.0% para 'e'
previsao: e
```

Ainda que já foi observado a letra 'i' vir após a 'd', para '-d' a sequencia '-de-' corresponde mais que a 'odig' (de 'codigo') 

```
>e
100.0% para '-'
previsao: -
>-
25.0% para 'd'
75.0% para 'c'
```

existe uma pequena chance de se voltar ao inicio da frase após terminar uma palavra, ituitivamente podemos pensar em 33,3% para cada inicio de palavra ('codigo','de','cor'), porém como a palavra 'cor' já foi evidenciada após 'de' a probabilidade é maior para 'cor'.


