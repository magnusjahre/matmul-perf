#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv){

    char* impl_input = NULL;
    int matrix_size = 32;
    int opt = 0;
    char *ms_string = NULL;
    enum { MM_NAIVE, MM_BLAS } matmul_impl = MM_NAIVE;

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

    // Now optind (declared extern int by <unistd.h>) is the index of the first non-option argument.
    // If it is >= argc, there were no non-option arguments.

    printf("Size is %d\n", matrix_size);
    if(optind >= argc){
        fprintf(stderr, "Usage: %s [-s] [matmul-implementation]\n", argv[0]);
        return -1;
    }
    impl_input = argv[optind];

    printf("Size is %d, impl %s\n", matrix_size, impl_input);

    return 0;
}