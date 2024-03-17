
CC=gcc
DEPS=matmul.c

all: debug opt

debug: $(DEPS)
	$(CC) -o matmul-dbg matmul.c

opt: $(DEPS)
	$(CC) -o matmul-opt -O3 matmul.c

disasm: debug opt
	objdump 

clean:
	rm matmul-dbg matmul-opt matmul.o