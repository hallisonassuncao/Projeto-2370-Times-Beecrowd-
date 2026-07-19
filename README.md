# Beecrowd 2370 - Times

✅ Status: Accepted (Python 3.11)

Nas aulas de educação física, os times de futebol costumam ser formados
assim: define-se quantos times vão existir e quem vai montar cada um
deles. Essas pessoas escolhem os alunos alternadamente — uma de cada vez,
em rodízio — e cada uma, na sua vez, sempre pega o aluno com o **melhor
nível de habilidade** dentre os que ainda não foram escolhidos. Como
resultado, os times acabam relativamente equilibrados na soma da
habilidade dos jogadores.

O programa recebe a lista de alunos disponíveis com seus respectivos
níveis de habilidade, além da quantidade de times a formar, e precisa
mostrar **como os times ficaram ao final** desse processo de seleção — sem
precisar considerar quem é a pessoa que escolhe, só o resultado final.

### Entrada

```
N T
nome_1 habilidade_1
nome_2 habilidade_2
...
nome_N habilidade_N
```

- `N`: quantidade de alunos, entre 2 e 10.000
- `T`: quantidade de times a formar, entre 2 e 1.000, sempre menor ou
  igual a `N`
- cada uma das `N` linhas seguintes traz o nome de um aluno (sempre em
  letras minúsculas) e um número inteiro `H` de 0 a 1.000.000
  representando sua habilidade
- não existem dois alunos com o mesmo nome, nem dois com a mesma
  habilidade (ou seja, nunca há empate na hora de decidir quem é
  escolhido)
- é possível que, no final, alguns times fiquem com menos jogadores que
  outros (quando `N` não é múltiplo de `T`)

### Saída

Para cada time, na ordem 1, 2, 3...:

```
Time <número do time>
<nomes dos jogadores desse time, um por linha, em ordem alfabética>
```

seguido de uma **linha em branco** — inclusive depois da descrição do
último time.

### Exemplo 1

**Entrada:**
```
14 3
felipe 4
alvaro 8
thiago 1
rodrigo 3
robson 2
fabio 9
ricardo 11
rodolfo 0
andre 14
arthur 12
ronaldo 55
rogerio 30
lucas 7
rafael 17
```

**Saída:**
```
Time 1
andre
fabio
felipe
ronaldo
thiago

Time 2
alvaro
arthur
rodolfo
rodrigo
rogerio

Time 3
lucas
rafael
ricardo
robson

```



## ✅ Resultado no Beecrowd

Submissão aceita (**Accepted**), em Python 3.11 — ver
`Prints/01-aceite-beecrowd.png`.
