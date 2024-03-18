
import numpy as np
import time
import argparse

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

def dump_matrix(matrix, size):
    print("Dumping matrix...")
    for i in range(size):
        for j in range(size):
            print(i,j,matrix[i][j])
    print("Done.")

def parse_args():
    parser = argparse.ArgumentParser(description='Multiply matrixes')
    parser.add_argument('implementation', type=str,
                    help='The matrix implementation to use (naive, numpy)')
    parser.add_argument('-s', dest='matrix_size', type=int, default=4,
                        help='Matrix dimension (default: 4)')

    return parser.parse_args()

def naive_matmul(matrix_a, matrix_b, matrix_res, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                matrix_res[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix_res

def main():
    args = parse_args()
    matrix_size = args.matrix_size

    print("Matrix multiplication in Python")
    print("Implementation:", args.implementation)
    print("Matrix size:", matrix_size)

    matrix_a = read_matrix(get_matrix_fname("a", matrix_size), matrix_size)
    matrix_b = read_matrix(get_matrix_fname("b", matrix_size), matrix_size)
    matrix_c = read_matrix(get_matrix_fname("c", matrix_size), matrix_size)
    
    matrix_res = [[0 for j in range(matrix_size)] for i in range(matrix_size)]

    print("Initialization complete, starting timer...")
    start_time = time.time() 

    if args.implementation == "naive":
        matrix_res = naive_matmul(matrix_a, matrix_b, matrix_res, matrix_size)
    elif args.implementation == "numpy":
        matrix_res = np.matmul(matrix_a, matrix_b)
    else:
        print("Unknown matmul implementation", args.implementation," (should be naive or numpy)")
        return

    end_time = time.time()
    duration = end_time - start_time
    print("Matrix multiplication took %.3f seconds" % duration)

    print("Verifying correctness...")
    check_correctness(matrix_c, matrix_res, matrix_size)
    print("Done.")

if __name__ == "__main__":
    main()