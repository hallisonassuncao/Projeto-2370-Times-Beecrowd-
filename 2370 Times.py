def pega_habilidade(aluno):
    return aluno[1]


def main():
    n, t = map(int, input().split())

    alunos = []

    for _ in range(n):
        nome, habilidade = input().split()
        habilidade = int(habilidade)
        alunos.append((nome, habilidade))

    alunos.sort(key=pega_habilidade, reverse=True)

    times = []
    for i in range(t):
        times.append([])

    for i in range(n):
        nome_aluno = alunos[i][0]
        numero_do_time = i % t
        times[numero_do_time].append(nome_aluno)

    for i in range(t):
        jogadores = times[i]
        jogadores.sort()

        print("Time", i + 1)
        for jogador in jogadores:
            print(jogador)
        print()


if __name__ == "__main__":
    main()