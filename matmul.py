
import numpy as np
import time

def read_matrix(filename, size):
    raw_array = np.fromfile(filename, dtype="double")
    out_matrix = [[raw_array[(i*size) +j ] for j in range(size)] for i in range(size)]
    return out_matrix

def get_matrix_fname(matrix_id, matrix_size):
    return "matrixes/matrix-"+matrix_id+"-"+str(matrix_size)

def check_correctness(reference, result, size):

    for i in range(size):
        for j in range(size):
            if abs(reference[i][j] - result[i][j]) > 0.000001:
                print("Error:", i, j, reference[i][j], result[i][j])
                assert False

def main():
    print("Naive matrix multiplication in Python")
    matrix_size = 256

    matrix_a = read_matrix(get_matrix_fname("a", matrix_size), matrix_size)
    matrix_b = read_matrix(get_matrix_fname("b", matrix_size), matrix_size)
    matrix_c = read_matrix(get_matrix_fname("c", matrix_size), matrix_size)

    matrix_res = [[0 for j in range(matrix_size)] for i in range(matrix_size)]

    print("Initialization complete, starting timer...")
    start_time = time.time() 
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                matrix_res[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    end_time = time.time()
    duration = end_time - start_time
    print("Matrix multiplication took %.1f seconds" % duration)

    print("Verifying correctness...")
    check_correctness(matrix_c, matrix_res, matrix_size)
    print("Done.")

if __name__ == "__main__":
    main()