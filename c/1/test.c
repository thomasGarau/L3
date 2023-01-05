#include <stdio.h>

int main(int argc, char const *argv[]){
    int intu = 5;
    int *sardoche = &intu;
    *sardoche = 17;
    printf("%d", *sardoche);
    return 0;
}
