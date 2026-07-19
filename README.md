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

### Exemplo 2

**Entrada:**
```
4 3
john 3
richard 0
greg 100
rupert 20
```

**Saída:**
```
Time 1
greg
richard

Time 2
rupert

Time 3
john

```

---

## 💡 Como o programa resolve isso (a ideia por trás do código)

A parte mais importante para entender é esta: **não precisamos simular a
escolha um aluno de cada vez**. Dá pra calcular o resultado final direto,
com um raciocínio em 3 passos:

**Passo 1 — Colocar todo mundo em ordem de quem seria escolhido primeiro**

Como cada escolhedor sempre pega o melhor aluno disponível, isso significa
que a *ordem de escolha* é simplesmente a lista de alunos ordenada da maior
habilidade para a menor. O primeiro da lista é escolhido primeiro, o
segundo é escolhido em segundo lugar, e assim por diante.

**Passo 2 — Descobrir para qual time cada aluno vai, usando o resto da divisão**

Os times se revezam em um ciclo fixo: time 1, time 2, time 3, time 1, time
2, time 3... Ou seja, se numerarmos as posições da lista ordenada
começando do zero (posição 0, 1, 2, 3...), dá pra descobrir o time de cada
aluno com o **resto da divisão por T** (o operador `%` em Python):

| Posição na lista ordenada | Time (posição % T, com T=3) |
|---|---|
| 0 | 0 → Time 1 |
| 1 | 1 → Time 2 |
| 2 | 2 → Time 3 |
| 3 | 0 → Time 1 |
| 4 | 1 → Time 2 |
| ... | ... |

**Passo 3 — Organizar e imprimir**

Depois de saber quem está em cada time, só falta ordenar os nomes de cada
time em ordem alfabética e imprimir no formato pedido.

---

## 🧩 Explicando o código, parte por parte

```python
def pega_habilidade(aluno):
    return aluno[1]
```
Essa função recebe um aluno (que é guardado como uma dupla `(nome,
habilidade)`) e devolve só a habilidade. Ela existe para ser usada como
critério de ordenação mais adiante — sem ela, o Python não saberia se deve
ordenar pelo nome ou pela habilidade.

```python
n, t = map(int, input().split())
```
Lê a primeira linha da entrada (`N` e `T`) e já converte os dois valores
para números inteiros.

```python
alunos = []

for _ in range(n):
    nome, habilidade = input().split()
    habilidade = int(habilidade)
    alunos.append((nome, habilidade))
```
Lê as `N` linhas seguintes, uma por aluno, e guarda cada uma como uma dupla
`(nome, habilidade)` dentro da lista `alunos`.

```python
alunos.sort(key=pega_habilidade, reverse=True)
```
Ordena a lista de alunos da **maior** habilidade para a **menor**
(`reverse=True`), usando a função `pega_habilidade` para saber o que
comparar. Essa é a ordem de escolha do Passo 1.

```python
times = []
for i in range(t):
    times.append([])
```
Cria `T` listas vazias, uma para cada time — é onde vamos guardar os nomes
dos jogadores de cada time.

```python
for i in range(n):
    nome_aluno = alunos[i][0]
    numero_do_time = i % t
    times[numero_do_time].append(nome_aluno)
```
Percorre a lista de alunos já ordenada (posição `i` = ordem de escolha) e
usa `i % t` para saber em qual time (índice de 0 a T-1) aquele aluno cai —
é exatamente o Passo 2.

```python
for i in range(t):
    jogadores = times[i]
    jogadores.sort()

    print("Time", i + 1)
    for jogador in jogadores:
        print(jogador)
    print()
```
Para cada time, ordena os nomes em ordem alfabética (`.sort()` sem
parâmetro já ordena texto de A a Z), imprime o cabeçalho `"Time N"` (`i +
1` porque o time 0 da lista é o "Time 1" pro usuário), imprime cada
jogador numa linha, e por fim imprime uma linha em branco (`print()`) —
que é exigida pelo enunciado depois de cada time, inclusive o último.

---

## 🗂️ Estrutura do repositório

```
.
├── README.md          # este arquivo
├── 2370 Times.py       # código-fonte da solução
├── nomes.txt            # exemplo de entrada para testar localmente
└── Prints/               # capturas de tela do processo de entrega
    ├── 01-aceite-beecrowd.png
    ├── 02-repositorio-remoto-github.png
    ├── 03-codigo-aberto-github.png
    ├── 04-vscode-execucao-local.png
    ├── 05-git-init-status-config.png
    ├── 06-git-commit-add-status.png
    ├── 07-github-quick-setup.png
    └── 08-git-remote-push-sucesso.png
```

## ▶️ Como testar localmente

Com Python 3 instalado, rode no terminal (dentro da pasta do projeto):

```bash
python3 "2370 Times.py" < nomes.txt
```

Isso alimenta o programa com o conteúdo de `nomes.txt` automaticamente,
sem precisar digitar nada na mão. A saída esperada é:

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
