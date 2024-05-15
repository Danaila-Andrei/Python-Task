import numpy as np
import random

def generare_matrice(num_matrices, min_rows, max_rows, min_cols, max_cols):
    with open('mat.in.py', 'w') as file:
        for _ in range(num_matrices):
            rows = random.randint(min_rows, max_rows)
            cols = random.randint(min_cols, max_cols)
            matrix = [[random.choice(['0', '1']) for _ in range(cols)] for _ in range(rows)]
            file.write(f"{rows}x{cols}:")
            for row in matrix:
                file.write(''.join(row))
            file.write('\n')


generare_matrice(100000,5,10,5,10)


def numara_unuuri_isolate(matrice):
    numar = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == '1':
                if (i == 0 or matrice[i - 1][j] == '0') and (i == len(matrice) - 1 or matrice[i + 1][j] == '0') \
                        and (j == 0 or matrice[i][j - 1] == '0') and (j == len(matrice[0]) - 1 or matrice[i][j + 1] == '0') \
                        and (i == 0 or j == 0 or matrice[i - 1][j - 1] == '0') and \
                        (i == 0 or j == len(matrice[0]) - 1 or matrice[i - 1][j + 1] == '0') and \
                        (i == len(matrice) - 1 or j == 0 or matrice[i + 1][j - 1] == '0') and \
                        (i == len(matrice) - 1 or j == len(matrice[0]) - 1 or matrice[i + 1][j + 1] == '0'):
                    numar += 1
    return numar
def numara_clustere(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def dfs(i, j, cluster):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != '1' or (i, j) in visited:
            return cluster
        visited.add((i, j))
        cluster.add((i, j))
        if len(cluster) > 2:
            return set()
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            cluster = dfs(x, y, cluster)
            if len(cluster) > 2:
                return set()
        return cluster

    def is_isolated(cluster):
        for i, j in cluster:
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == '1' and (x, y) not in cluster:
                    return False
        return True

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1' and (i, j) not in visited:
                cluster = dfs(i, j, set())
                if len(cluster) == 2 and is_isolated(cluster):
                    count += 1
    return count



def numara_clustere_de_trei(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def dfs(i, j, cluster):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != '1' or (i, j) in visited:
            return cluster
        visited.add((i, j))
        cluster.add((i, j))
        if len(cluster) > 3:
            return set()
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),
                     (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
            cluster = dfs(x, y, cluster)
            if len(cluster) > 3:
                return set()
        return cluster

    def is_isolated(cluster):
        for i, j in cluster:
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),
                         (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == '1' and (x, y) not in cluster:
                    return False
        return True

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1' and (i, j) not in visited:
                cluster = dfs(i, j, set())
                if len(cluster) == 3 and is_isolated(cluster):
                    count += 1
    return count

def proceseaza_matricea(dimensiuni, matrice_str):
    randuri, coloane = map(int, dimensiuni.split('x'))
    matrice = [list(matrice_str[i:i+coloane]) for i in range(0, len(matrice_str), coloane)]
    unuuri_isolate = numara_unuuri_isolate(matrice)
    clustere_doua = numara_clustere([rand[:] for rand in matrice])
    clustere_trei = numara_clustere_de_trei([rand[:] for rand in matrice])
    return unuuri_isolate, clustere_doua, clustere_trei

def main():
    with open('mat.in.py', 'r') as f_in, open('mat.out.py', 'w') as f_out:
        for linie in f_in:
            dimensiuni, matrice_str = linie.strip().split(':')
            rezultate = proceseaza_matricea(dimensiuni, matrice_str)
            print(*rezultate, file=f_out)

if __name__ == "__main__":
    main()
