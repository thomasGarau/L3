#include <stdlib.h>
#include <stdio.h>

typedef struct maillon_int {
    int val;
    struct maillon_int* succ;
}Maillon_int;

Maillon_int* init();
void insert_newMaillon(Maillon_int **headList);