//---------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

#include <string.h>

struct personne
{
int age;
char nom[20];
};

struct pile
{
int sommet;  //sommet de la pile
struct personne pers[5];
}*pilePointeur;


void CreerPile(void);
int EstVide(void);
void Empiler(int ageP,char* nomP);
void AffichePile(void);
void Depiler(void);
int EstPleine();


int main(int argc, char* argv[])
{
///// pile contenant une structure de donnees (ici, la structure personne)
CreerPile();
//ici on empile les elements internes a la structure personne 1 a 1,
// mais on pourrait empiler les instances de structure en une seule fois
// en modifiant la fonction empiler de cette facon void empiler(personne p)
// mais il faudrait pour ca renseigner au prealable les instances a empiler.
Empiler(20,"caroline");
Empiler(30,"jean");
Empiler(40,"corinne");
Empiler(50,"francois");
Empiler(60,"laurence");
AffichePile();
Empiler(25,"paul");
Depiler();
Empiler(25,"paul");
AffichePile();
///////
free (pilePointeur);
return 0;
}
//---------------------------------------------------------------------------


void CreerPile(void)
{
pilePointeur = (pile*) malloc(sizeof(pile));
pilePointeur->sommet=0;
}


void Empiler(int ageP,char* nomP)
{
if(!EstPleine()){
    pilePointeur->pers[pilePointeur->sommet].age = ageP;
    strcpy(pilePointeur->pers[pilePointeur->sommet].nom, nomP);
    pilePointeur->sommet ++;
}else{
    printf("la pile est pleine");
}
}


void Depiler()
{
if (EstVide())
    printf("La pile est vide\n");
else
    pilePointeur->sommet--;
}

int EstVide(void)
{
if (pilePointeur->sommet==0)
     return 1;
else
    return 0;
}

int EstPleine(){
    if(pilePointeur->sommet >= 5 ){
        return 1;
    }else{
        return 0;
    }
}

void AffichePile()
{
int i;
for(i=0;i<pilePointeur->sommet;i++)
    {
    printf( "%d ",pilePointeur->pers[i].age);
     printf( "%s \n",pilePointeur->pers[i].nom);
    }
printf("\n");
}





//---------------------------------------------------------------------------
 