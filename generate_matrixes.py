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

def write_matrix_to_file(matrix, filename):
    output_path = "matrixes/"

    file = open(output_path+filename, "w")
    file.write(str(matrix))
    file.close()

def main():

    print("Generating matrixes...")

    matrix_sizes = [2**n for n in range(5,6)]

    for ms in matrix_sizes:
        print("Generating matrix with size", ms)
        matrix_a = generate_matrix(ms)
        matrix_b = generate_matrix(ms)
        matrix_c = np.matmul(matrix_a, matrix_b)

        write_matrix_to_file(matrix_a, "matrix-a-"+str(ms))
        write_matrix_to_file(matrix_b, "matrix-b-"+str(ms))
        write_matrix_to_file(matrix_c, "matrix-c-"+str(ms))

    print("Done")

if __name__ == "__main__":
    main()
