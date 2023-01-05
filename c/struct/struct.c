#include "struc.h";
#include <stdbool.h>
Maillon_int* init(){
    Maillon_int *m;
        m = malloc(sizeof(Maillon_int));
        m->val = rand() % 150;
        m->val = NULL;
    return m;
}


int main(int argc, char const *argv[])
{    
    srand(time(NULL)); 
    Maillon_int *m = init();
    printf("%p", m);
    free(m);
    return 0;
}

void insert_head_Maillon(Maillon_int **headList){
    int val = rand();
    Maillon_int *new = init();
    new->succ = *headList;
    *headList = new;
}

void insert_newMaillon(Maillon_int **headList){
    
    int new = rand();
    if (new < headList){
       insert_head_Maillon(headList);
    }else{
        Maillon_int *m = malloc(sizeof(int));
        m->val = new
        bool trouve = false;
        Maillon_int *pt = (*headList)->succ;
        while(!trouve){
            
        }
    }
}