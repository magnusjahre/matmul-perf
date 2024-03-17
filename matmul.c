#include "matmul.h"

double* read_matrix(int matrix_size, char matrix_id){
    FILE* fptr = NULL;
    double* matrix = (double*) malloc(matrix_size*matrix_size*sizeof(double));

    //TODO: This is a potential buffer overflow if we do not check bounds
    char file_path[100];
    sprintf(file_path, "matrixes/matrix-%c-%d", matrix_id, matrix_size);
    printf("Reading matrix file: %s\n", file_path);

    fptr = fopen(file_path, "r");
    if(fptr == NULL){
        printf("Cannot open matrix file\n");
        return NULL;
    }
    fread(matrix, sizeof(double), matrix_size*matrix_size, fptr);
    fclose(fptr);

    return matrix;
}

void dump_matrix(double* matrix, int matrix_size){
    for(int i=0;i<matrix_size;i++){
        for(int j=0;j<matrix_size;j++){
            printf("%d %d %f\n", i, j, matrix[i*matrix_size + j]);
        }
    }
}

int main(int argc, char** argv){

    int matrix_size = 32;
    int opt = 0;
    while ((opt = getopt(argc, argv, "s:")) != -1) {
        switch (opt) {
        case 's': 
            sscanf(optarg, "%d", &matrix_size); 
            break;
        default:
            fprintf(stderr, "Usage: %s [-s] [matmul-implementation]\n", argv[0]);
            return -1;
        }
    }

    if(optind >= argc){
        fprintf(stderr, "Usage: %s [-s] [matmul-implementation]\n", argv[0]);
        return -1;
    }

    char* impl_input = argv[optind];

    printf("Running matrix multiply for size %d and implementation %s\n", matrix_size, impl_input);

    double* matrix_a = read_matrix(matrix_size, 'a');
    double* matrix_b = read_matrix(matrix_size, 'b');    
    double* matrix_c = read_matrix(matrix_size, 'c');    

    //TODO: Multiply matrixes A and B and time it

    //TODO: Check that the output matches matrix C

    return 0;
}