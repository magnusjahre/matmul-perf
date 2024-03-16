import numpy as np
import random

def generate_matrix(size):
    
    matrix = []
    for row_id in range(size):
        row = []
        for col_id in range(size):
            row.append(random.random()*100)
        matrix.append(row)

    return matrix
    

def main():

    print("Generating matrixes...")

    matrix_sizes = [2**n for n in range(5,6)]

    for ms in matrix_sizes:
        print("Generating matrix with size", ms)
        matrix_a = generate_matrix(ms)
        matrix_b = generate_matrix(ms)
        matrix_c = np.matmul(matrix_a, matrix_b)

    print("Done")

if __name__ == "__main__":
    main()
