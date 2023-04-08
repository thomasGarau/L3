#include<stdio.h>

#include<process.h>
#include<malloc.h>
#include<ctype.h>


int hachage(int clef);
int compressage(int hash);
int insererClef(int hashCode);
int colision(int indice);
void affichage();
int tab[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
int taille = sizeof(tab) / sizeof(tab[0]);

int CONSTANTE_H_1 = 0;
int CONSTANTE_H_2 = 1;

//retourne le hash de la cle 
int hachage(int clef){
    return(3*clef+14);
}

//retourne l'indice de base(sans tenir compte des colision) d'un hash
int compressage(int hash){
    return(hash % taille);
}

// inserre à un indice donné une clef donné
void insereClef(int indice,int clef)
{
    //si l'indice == -1 alors celui-ci est libre on insére donc la clef
    if (tab[indice]==-1)
        tab[indice]=clef;
    //si non on execute la fonction collision qui retourne l'index libre ou -1 si le tableau est plein.
    else
       tab[collision(indice)] = clef; 
}

//permet de retourner l'indice auquel une clef est stocké ou une clef doit être inséré.
int collision(int indice){
    //on commence à i = 1 car si non c1* 0 + c1 * 0² bien ca fait tjr 0. et qu'on incrémente i après avoir déterminé l'indice
    int i = 1;
    do{
        //si l'indice est à -1 ou -2 alors celui si est vide ou libre est on peut insérer l'élement
        if(tab[indice] == -1 ){
            return indice;
        }
        //on modifie l'indice pour parcourir le tableau de manière quadratique
        //en lui ajoutant c1*i + c2*i² le tout modulo taille pour ne pas sortir des bornes du tableau.
        indice = (indice + (CONSTANTE_H_1 * i) + (CONSTANTE_H_2 * (i * i))) % taille;
        i++;
        
    //si i est supérieur à la taille du tableau cela signifie que le tableau est plein et que donc aucun élement ne peut y être inséré.
    //puisque i commence à 1 pas besoin de retirer 1 à taille.
    }while(i < taille);
    // on retourne donc null.
    printf("%s", "Erreur Liste pleine");
    return -1;
}

void afficheTab()
{
    for (int i=0;i<taille;i++)
        printf("%d\t",i);
    printf("\n");
    for (int i=0;i<taille;i++)
        printf("%d\t",tab[i]);
}

int main(int argc, char const *argv[])
{
    //48 doit être ajouté à l'indice 8
    int clef = 48;
    insereClef(compressage(hachage(clef)), clef);
    afficheTab();
    // 28 doit égaleemnt être ajouté à l'indice 8 cela permettra de tester les colision.
    clef = 28;
    printf("\n\n");
    insereClef(compressage(hachage(clef)), clef);
    afficheTab();
    // de même pour 38
    clef = 38;
    printf("\n\n");
    insereClef(compressage(hachage(clef)), clef);
    afficheTab();


    /* résultat final doit être 
    48 * 3 + 14 % 10 = 8
    48 doit donc être insérer à l'indice 8 

    puis 28 * 3 + 14 % 10 = 8
    l'indexe 8 étant pris alors on fait
    8 + c1 * i + c2 * i2 =
    8 + 0 + 1 % 10 = 9
    28 doit donc être insérer à l'indice 9

    puis 38 devant être lui aussi insérer à l'indice 8 mais celui-ci étant pris on fait
    8 + c1 * i + c2 * i2 =
    8 + 0 + 1 % 10 = 9
    mais 9 est lui aussi occupé donc : 
    9 + c2 * 2 + c2 * 2² =
    9 + 0 + 4 % 10 = 3
    38 doit être à l'indice 3
    */
    return 0;
}
