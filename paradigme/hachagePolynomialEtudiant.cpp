//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

#include <conio.h>
#include <stdio.h>
#include <string.h>
// void test();
/*int puissance(int x, int i);
int hache(char chaine[]);
int hachePolynomiale(char chaine[]);
int hachePolynomialeCompresseeQuiMarcheMal(char chaine[]);
int hachePolynomialeCompresseeQuiMarcheBien(char chaine[]);
int tailleTable = 500; // valeur arbitraire*/
void cyclique();
int recursif(int i);
int dicothomique(int tab[10], int min, int max, int key);
int main(int argc, char *argv[])
{
    //cyclique();
    //recursif(0);
    int tab[10] = {1,4,8,9,81,176,189,278,780,952};
    int taille = sizeof(tab) / sizeof(tab[0]);
    int a = dicothomique(tab, 0, taille, 278);
    printf("%d", a);
    return 1;
    /*
    char chaine[500];
    int h, hp, hpc;
    // test();
    printf("Saisissez une chaine ce caractere\n");
    // scanf("%s", chaine);   // pas d espace dans le scanf, preferez gets
    gets(chaine);
    h = hache(chaine);
    printf("\nle hachage est : %d\n\n", h);
    hp = hachePolynomiale(chaine);
    printf("\nle hachage polynomial est : %d\n\n", hp);
    hpc = hachePolynomialeCompresseeQuiMarcheMal(chaine);
    printf("\nle hachage polynomial compresse qui marche mal est : %d\n", hpc);
    hpc = hachePolynomialeCompresseeQuiMarcheBien(chaine);
    printf("\nle hachage polynomial compresse qui marche bien est : %d\n", hpc);
    getch();*/
}

/*int hache(char chaine[])
{
    int i, h = 0;
    for (i = 0; i < strlen(chaine); i++)
    {
        h = h + (int)chaine[i];
        printf("%d\t ", h);
    }
    return (h);
}

int hachePolynomiale(char chaine[])
{
    int i, hp = 0, x = 37;
    for (i = 0; i < strlen(chaine); i++)
    {
        hp = hp + ((int)chaine[i] * puissance(x, i));
        printf("%d\t ", hp);
    }
    return (hp);
}

int hachePolynomialeCompresseeQuiMarcheMal(char chaine[])
{
    int hp = 0,  // le meme hp que ds la fonction hachePolynomiale(..) ci-dessus
        hpc = 0, // contiendra (ou pas ...) le hachage polynomial compresse
        i, x = 37;
    for (i = 0; i < strlen(chaine); i++)
        hp = hp + ((int)chaine[i] * puissance(x, i));
         hpc = hp % 500;
    return hpc;
}

int hachePolynomialeCompresseeQuiMarcheBien(char chaine[])
{
    int hpc = 0;
    hpc = 0;
    int i = 0;
    int x = 37;
    for (i = 0; i < strlen(chaine); i++){
        hpc = hpc + (((int)chaine[i] * puissance(x,i)) % tailleTable)
    }
    // A VOUS DE JOUER

    return hpc;
    return 1;
}

int puissance(int x, int i) // x^i
{
    int j, puiss = 1;
    for (j = 0; j < i; j++)
        puiss = puiss * x;
    return puiss;
}
void test()
{
    int x0, x1, x2, x3;
    x0 = (109 * 37 + 97) % 500;
    printf("%d ", x0);
    x1 = (37 * x0 + 114) % 500;
    printf("%d ", x1);
    x2 = (37 * x1 + 105) % 500;
    printf("%d ", x2);
    x3 = (37 * x2 + 101) % 500;
    printf("%d ", x3);
}*/

void cyclique(){
    char maChaine[5] = "juju";
    int h =0;
    int h1 = 0;
    int h2 = 0;
    int n = 5;
    int taille = strlen(maChaine);
    for(int i = 0; i < taille; i++ ){
        h1 = h >> (32-n);
        h2 = h << (n);
        h = h1|h2;
        h = h + (int)maChaine[i];
    }
    printf("%d", h);
}

int iteratif(){
    int tab[10] = {1,4,8,9,81,176,189,278,780,952};
    int myKey = 176;
    for(int i =0; i< sizeof(tab) /sizeof(tab[0]); i++){
        if(tab[i] == myKey){
            printf("%d", i);
            return i;
        }
    }
}

int recursif(int i){
    int tab[10] = {1,4,8,9,81,176,189,278,780,952};
    int myKey = 176;
    if(i > sizeof(tab) / sizeof(tab[0])){
        return -1;
    }
    if(i < sizeof(tab) / sizeof(tab[0]) && tab[i] == myKey){
        printf("%d", i);
    }else{
        recursif(i+1);
    }
}

//2 le prie cas correspond à n => autrement dit la clés ce trouve au dernier index du tableau il doit donc être parcourus en entier
//2 le meilleur cas correspond à 1 => la valeur ce trouve au premier index du tableau;
//si la clé appartient pas au tableau on va ce prendre un index out of bounds est ca c'est pas foux foux
//modification ajouté une vérification que i n'est pas suppérieur à i 

int dicothomique(int tab[10], int min, int max, int key){
    printf("%d\n", (min + max) /2);
    if(max - min == 0 ){
        return (min + max) / 2;
    }
    if(tab[(min + max) / 2] == key ){
        return (min+ max) / 2;
    }else if(tab[(min + max) / 2] > key ){
        return dicothomique(tab, min, (min + max) / 2, key);
    }else{
        return dicothomique(tab, (min + max) /2, max, key);
    }
    
}