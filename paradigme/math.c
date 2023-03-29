#include <stdbool.h>
#include <math.h>
#include <stdio.h>

bool maBoucle(){
    bool monBool = true;
    int puissance = 1;
    int c = 2;
    for(int i =0; i<10;i++){
        puissance = puissance + (int) pow(3,i+1);   
    }
    c = c * ( (int) pow(3,10) );
    if(c <= puissance){
        monBool = false;
    }
    printf("%d",  monBool);
    printf("\n%d", puissance);
    return monBool;
}

int calPuissance(){
    int n = 10;
    int puissance = 1;
    for(int i=0; i<n; i ++){
        puissance = puissance + (int) pow(3,i+1);
    }
}

int calC(puissance){
    int a = 0;
    int pas = 0.1;
    int c = 1;
    int i = 0;
    while (c > puissance)
    {
        c = c* (int) pow(3,10);
        i++;
        c = 1 + (i * pas);
        
    }return c;
}


int main(int argc, char const *argv[])
{
    int a = puissance();
    int res = calC(a);
    printf("%d", res);
    return 0;
}

