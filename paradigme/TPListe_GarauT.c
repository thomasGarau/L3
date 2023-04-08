#include<stdio.h>
#include<process.h>
#include<malloc.h>
#include<ctype.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>


void inserer(char *nom, int clef);
void supprimerDernier();
void afficherListe();
insererAt(int indice, char *nom, int clef);

struct element {
    int clef;
    char *nom;
    struct element * pSuivant;
    struct element * pPredecesseur;
} * tete=NULL, * pPrecedent, * courant;

void inserer(char* nom, int clef){
    courant = (struct element*) malloc(sizeof(struct element));
    courant->clef = clef;
    courant->nom = strdup(nom);
    if(tete != NULL){
        pPrecedent->pSuivant = courant;
    }else{
        tete = courant;
    }
    courant->pPredecesseur = pPrecedent;
    pPrecedent = courant;
    courant->pSuivant = NULL;
}

void afficherListe(){
    struct element *p = (struct element*) malloc(sizeof(struct element));
    p = tete;
    while (p != NULL){
        printf("%d%s\n", p->clef, p->nom);
        p = p->pSuivant;
    }
}

void supprimerDernier(){
    struct element *p = (struct element*) malloc(sizeof(struct element));
    p = tete;
    while(p->pSuivant->pSuivant != NULL){
        p = p->pSuivant;
    }
    free(p->pSuivant);
    p->pSuivant = NULL;
}

insererAt(int indice, char *nom, int clef){
    courant = (struct element*) malloc(sizeof(struct element));
    struct element *p = (struct element*) malloc(sizeof(struct element));
    p = tete;
    int i = 1;
    courant->clef = clef;
    courant->nom = strdup(nom);
    if(indice = 0){
        courant->pPredecesseur = NULL;
        courant->pSuivant = tete;
        tete->pPredecesseur = courant;
    }else{
        while(p->pSuivant !=NULL && i != indice){
            p = p->pSuivant;
            i++;
        }
        courant->pSuivant = p;
        courant->pPredecesseur = p->pPredecesseur;
        p->pPredecesseur = courant;
    }
}

int main(int argc, char const *argv[])
{
    inserer("bonjour", 76);
    inserer("salut", 92);
    inserer("aa", 34);
    inserer("aabzd", 65);
    //insererAt pas fonctionnel
    insererAt(1, "insertionIndice1", 1);
    supprimerDernier();
    afficherListe();
    return 0;
}

/* 
Question3 proposition : changement de la struct en struct doublement chainer pour pouvoir
modifié l'élement précédent en le faisant pointé sur l'élement que l'on souhaite ajouter.
modifié la fonction d'insertion pour qu'elle prenent l'ancien derniElement en temps que prédécesseur.

la fonction prendras donc en paramètres l'indice auquel on souhaite l'ajouté.
une fois l'indice atteint on affecteras à p_suivant de notre nouvelle élement element[i]->psuivant
puis on affecteras notre nouvelle élement à psuivant de élement[i] pour qu'il pointe sur notre nouvelle élement
 
*/


