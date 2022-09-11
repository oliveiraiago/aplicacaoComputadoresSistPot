class EliminacaoGauss:

    def __init__(self, matrizA, matrizb):
        self.matrizA = matrizA
        self.matrizb = matrizb

        # N° de colunas da matriz A
        self.nColA = len(matrizA[0])

        # N° de linhas da matriz b e A
        self.nLinhasA = len(matrizA)
        self.nLinhasb = len(matrizb)

        # Vetor de zeros responsável por armazenar a solução
        self.x = [0] * self.nLinhasb

        if self.nLinhasA == self.nColA:
            matrizA_equivalente, vetorb_equivalente = self.eliminacao()
            resultado = self.substituicao(matrizA_equivalente, vetorb_equivalente)
            print(resultado)
        else:
            print("A matriz A não é quadrada. As operações não podem ser realizadas.")

    # Função para resolver o sistema triangular superior, ou seja, a parte final do algoritmo
    def substituicao(self, matriz_triangular_superior, matrizb):
        x = self.x
        n = self.nLinhasb
        matrizA = matriz_triangular_superior
        vetorb = matrizb

        # etapa da solução do problema
        x[n - 1] = vetorb[n - 1] / matrizA[n - 1][n - 1]
        for i in list(range(n - 1, 0, -1)):
            soma = 0
            for j in list(range(i + 1, n + 1, 1)):
                soma += matrizA[i - 1][j - 1] * x[j - 1]
            x[i - 1] = (vetorb[i - 1] - soma) / matrizA[i - 1][i - 1]
        return x

    # Resolve a parte da eliminação dos elementos abaixo do pivo
    def eliminacao(self):
        n = self.nLinhasb
        matrizA = self.matrizA
        vetorb = self.matrizb

        # calcula os pivos
        for k in list(range(1, n, 1)):
            # calcula os multiplicadores
            for i in list(range(k + 1, n + 1, 1)):
                m = matrizA[i - 1][k - 1] / matrizA[k - 1][k - 1]
                matrizA[i - 1][k - 1] = 0
                vetorb[i - 1] = vetorb[i - 1] - m * vetorb[k - 1]

                # Atualizar os demais valores das linhas
                for j in list(range(k + 1, n + 1, 1)):
                    matrizA[i - 1][j - 1] = matrizA[i - 1][j - 1] - m * matrizA[k - 1][j - 1]
        return matrizA, vetorb


A = [[4, -9, 2],
     [2, -4, 4],
     [-1, 2, 2]]
b = [2, 3, 1]
objeto = EliminacaoGauss(A, b)
