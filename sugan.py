converter_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'u': 18, 'v': 19, 'r': 20, 's': 21, 't': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}
def get_key(val):
    for key, value in converter_dict.items():
        if val == value:
            return key

def product_of_two_matrix(matrix1, matrix2):
    m = len(matrix1)
    n = len(matrix2)
    res = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix1[i][k]*matrix2[k][j]
    return res