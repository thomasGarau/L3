#include "random.h"
int randomu(){
    return rand();
}

int randomMax(int max){
    return rand() % max;
}

int randomMinMax(int min, int max){
    return min + rand() % max;
}

float randomDec(){
    return (float) rand() / (float) RAND_MAX;
}

float randomFloat(int min, int max){
    return min + (float)rand() / (float)(RAND_MAX) * (max-min) ;
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));
    printf("%d\n",randomu());
    printf("%d\n", randomMax(19));
    printf("%d\n", randomMinMax(4, 8));
    printf("%f\n", randomDec());
    printf("%f\n", randomFloat(0.1, 2.0));
    return 0;
}
