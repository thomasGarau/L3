//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <stdio.h>
#include<conio.h>
#include<stdlib.h>
using namespace std;
int hache(int clef);
int compresse(int hh);
void insereClef(int indice,int clef);
void supprimeClef(int clef);
int collision(int indice);
void afficheTab();
void recherche();
int tab[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}; // -1 signifie vide, -2 signifie libre
//int choix;
int main()
{
afficheTab();
int clef,choix;
 do
 {
    printf("\n\n1 ... inserer une clef\n");
    printf("2 ... supprimer une clef\n");
    printf("3 ... Quitter\n");
    scanf("%d",&choix);

       switch(choix)
        {
            case 1:
                    printf("Numero de clef a inserer ?");
                    scanf("%d",&clef);
                    insereClef(compresse(hache(clef)),clef);
                    break;
            case 2 :
                    printf("Numero de clef a supprimer ?");
                    scanf("%d",&clef);
                    supprimeClef(clef);
                    break;

            case 3 :
            default :
                    choix=3;
        }
system("cls");
afficheTab();
}while(choix!=3);

}

void insereClef(int indice,int clef)
{
    if (tab[indice]==-1)
        tab[indice]=clef;
    else 
       tab[collision(indice)] = clef;
        
}

void supprimeClef(int clef)
{
// recherche sequentielle sur un tableau de 10 entiers
// on ne gere pas l inexistence de la clef

int taille = sizeof(tab) / sizeof(tab[0]);
for (int i=compresse(hache(clef));i< taille;i++){
    if (tab[i]==clef){
        if(tab[i+1] = -1){
            tab[i] = -1;
        }else{
            tab[i]=-2;
        }
    }else if (tab[i] == -1){
        printf("bheu");
        break;
    }
}

afficheTab();    
}

void recherche(int clef){
    int taille = sizeof(tab) / sizeof(tab[0]);
    for (int i=compresse(hache(clef));i< taille;i++){
        if (tab[i]==clef){
            if(tab[i+1] = -1){
                printf("%d", tab[i]);
            }
        }else if (tab[i] == -1){
            printf("bheu");
            break;
        }
    }
}


int collision(int indice)
{

int i = 0;
int taille = sizeof(tab) / sizeof(tab[0]);
do {
    printf("%d", tab[indice]);
    if(i > taille -1){
        if(tab[indice] >= taille -1){;
            tab[indice] = 0;
        }else{ 
            indice++; 
        }
    }else{
        printf("%d", -1);
        return -1;
    }
    i++;
}while(tab[indice] != -1);

printf("\nCollision a l indice %d\n",indice);
system("PAUSE");
return -1;



}

int hache(int clef)
{
    return(3*clef+14);
}

int compresse(int hh)
{
    return(hh%10);
}

void afficheTab()
{
    for (int i=0;i<10;i++)
        printf("%d\t",i);
    printf("\n");
    for (int i=0;i<10;i++)
        printf("%d\t",tab[i]);
}

//---------------------------------------------------------------------------
 