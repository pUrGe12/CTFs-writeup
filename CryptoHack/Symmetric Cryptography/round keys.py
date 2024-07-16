def matrix2bytes(matrix):
    return ''.join([chr(i[j]) for i in matrix for j in range(0,4)])

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    output_matrix = [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]
    return output_matrix

print(matrix2bytes(add_round_key(state, round_key)))            # this gives the flag

