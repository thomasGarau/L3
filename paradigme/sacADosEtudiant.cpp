//---------------------------------------------------------------------------
#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <stdio.h>
// declarations globales


struct Objets
{
int vi,pi;
float ratio;
int numeroObjet; // pour identifier l objet
};

Objets hObjetsInitiaux[4];
Objets hObjetsRanges[4];


void initialiseObjets(int numObjet,int a,int b); // pour donner des valeurs de depart aux objets
void triBulles();// pour ranger les objets dans l ordre decroissant du ratio
void afficheTableau(Objets t[4]);
void remplirLeSac(); //  c est ce qui nous interesse ici
void bienRemplirSac();

int main(int argc, char* argv[])
{
initialiseObjets(0,7,13);
initialiseObjets(1,4,12);
initialiseObjets(2,3,8);
initialiseObjets(3,3,10);
//afficheTableau(hObjetsInitiaux);
triBulles();
//afficheTableau(hObjetsInitiaux);

bienRemplirSac();

//afficheTableau(hObjetsRanges);

    return 0;
}
//---------------------------------------------------------------------------

void remplirLeSac()
{/*
  int poidsMax = 30;
  int poidsActuel = 0;
  int i = 0;
  int j = 0;
  while(poidsActuel < poidsMax && i < (sizeof(hObjetsInitiaux)/sizeof(hObjetsInitiaux[0])) ){
    if(poidsActuel + hObjetsInitiaux[i].pi < poidsMax){
      hObjetsRanges[j] = hObjetsInitiaux[i];
      poidsActuel += hObjetsInitiaux[i].pi;
      j++;
    }
    i++;
  }*/
}

void bienRemplirSac(){
  int curseur = 1;
  int valeur = 0;
  int poids = 0;
  int index = 0;
  int meilleurIndex = 0;
  int meilleurValeur = 0;
  int meilleurPoids = 0;
  for(int i=0; i<16; i++){
    do{
      if(i&curseur != 0){
        valeur += hObjetsInitiaux[index].vi;
        poids += hObjetsInitiaux[index].pi;
      }
      curseur = curseur << 1;
      index ++;    
    }while(curseur < 16);
    curseur = 1;
    index = 0;
    printf("blblbl=%d", valeur);
    if(valeur > meilleurValeur && poids < 30){
      meilleurValeur = valeur;
      meilleurPoids = poids;
      meilleurIndex = i;
    }
    printf("index =%d; valeurTotal=%d; poidsTotal=%d", i, valeur, poids);
    valeur = 0;
    poids = 0;
  }
  printf("\n\nmeilleur solution : index =%d; valeurTotal=%d; poidsTotal=%d", meilleurIndex, meilleurValeur, meilleurPoids);
}

void initialiseObjets(int numObjet,int a,int b)
{
hObjetsInitiaux[numObjet].vi=a;
hObjetsInitiaux[numObjet].pi=b;
hObjetsInitiaux[numObjet].ratio=(float)a/(float)b;
hObjetsInitiaux[numObjet].numeroObjet=numObjet+1;
}

void triBulles()
{
int i,j;
Objets swapObjet;
  for (i=0 ; i < 3; i++)
  {
    for (j=0 ; j< 3-i; j++)
    {
      if (hObjetsInitiaux[j].ratio < hObjetsInitiaux[j+1].ratio )
      {
        swapObjet.ratio = hObjetsInitiaux[j].ratio ;
        swapObjet.pi = hObjetsInitiaux[j].pi ;
        swapObjet.vi  = hObjetsInitiaux[j].vi ;
        swapObjet.numeroObjet = hObjetsInitiaux[j].numeroObjet ;
            hObjetsInitiaux[j].ratio=hObjetsInitiaux[j+1].ratio ;
            hObjetsInitiaux[j].pi=hObjetsInitiaux[j+1].pi ;
            hObjetsInitiaux[j].vi=hObjetsInitiaux[j+1].vi ;
            hObjetsInitiaux[j].numeroObjet=hObjetsInitiaux[j+1].numeroObjet ;
        hObjetsInitiaux[j+1].ratio=swapObjet.ratio;
        hObjetsInitiaux[j+1].pi=swapObjet.pi;
        hObjetsInitiaux[j+1].vi=swapObjet.vi;
        hObjetsInitiaux[j+1].numeroObjet=swapObjet.numeroObjet;
      }
    }
  }
}

void afficheTableau(Objets t[4])
{
int i;
for (i=0;i<4;i++)
    {
    if ( t[i].numeroObjet!=0) // pour n'afficher que les objets rang�s dans le sac
        {
        printf("Pour l objet numero : %d\n", t[i].numeroObjet);
        printf("\tvi = : %d ", t[i].vi);
        printf("pi = %d ", t[i].pi);
        printf("ratio= : %f \n", t[i].ratio);
        }
    }
printf("\n\n");
}
