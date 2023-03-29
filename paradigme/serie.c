#include <stdbool.h>
#include <math.h>
#include <stdio.h>

int calSerie(){
    int n = 0;
    int somme = 0; 
    for(int i = 1; i<7; i++){
        somme += n * pow(-1,n-1);
    }
    return somme;
}


int main(int argc, char const *argv[])
{
    int a = calSerie();
    printf("%d", a);
    return 0;
}
