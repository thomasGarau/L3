#include <stdio.h>

int main(int argc, char const *argv[])
{
    char C = 'a';
    int A = 256;
    int B = 129;
    char *pt_sur_un_char = &C; 
    int *pt_sur_un_int = &A;
    int *pt_sur_un_int2 = &B;
    printf("Adresse de a= %p\n", *pt_sur_un_char);
    printf("Adresse de b= %p\n", *pt_sur_un_int);
    printf("Adresse de c= %p\n", *pt_sur_un_int2);
    printf("ascii de c= %i",C);

}

