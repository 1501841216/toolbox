import numpy as np
import codecs

block_size = 64
rounds = 14
P_permutation = [58, 17, 50, 32, 54, 13, 41, 33,
                 12, 59, 38, 25, 11, 45, 1, 44,
                 62, 48, 40, 49, 35, 0, 51, 29,
                 28, 5, 37, 31, 14, 39, 36, 6,
                 2, 26, 21, 18, 27, 4, 52, 46,
                 7, 3, 16, 20, 47, 19, 30, 43,
                 55, 10, 34, 56, 8, 63, 42, 24,
                 61, 9, 60, 22, 57, 15, 23, 53]
inverse_P_permutation = [P_permutation.index(i) for i in range(block_size)]
print(inverse_P_permutation)