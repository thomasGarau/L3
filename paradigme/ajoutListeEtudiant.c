//---------------------------------------------------------------------------
#include<stdio.h>

#include<process.h>
#include<malloc.h>
#include<ctype.h>

void ajout(void);
void visu(void);

int main(int argc, char* argv[])
{
ajout();
visu();

ajout();
visu();


return 0;
}

/*-------------------- Variables globales --------------------------------*/

struct Article {
	char Nom [20];
	char Reference [30];
	int Nombre;
	int Prix;
	struct Article * AdresseSuivant;
	} * Debut=NULL, * Precedent, * Courant;


/*----------------- Ajout d'un article ------------------------------------*/
void ajout(void)
 {
	Courant=(struct Article *) malloc(sizeof(struct Article));
	puts("\n\tEntrer le nom, la reference, le nombre et le prix.");
	scanf("%s%s%d%d",Courant->Nom,Courant->Reference,&Courant->Nombre,&Courant->Prix);

    // code a completer pour ajouter un article dans la liste
    // pensez � initialiser le pointeur "Debut" quand la liste est vide  et remarquez que le seul
    // pointeur valide au lancement du prog est le pointeur "Courant".

	if(Debut = NULL){
		Debut = Courant;
	}else{
		Precedent->AdresseSuivant = Courant;
	}
	Courant->AdresseSuivant = NULL;
	Precedent = Courant;
	
	
 }

/*-------------------- Visualisation de la liste --------------------------*/
void visu (void) {

// clrscr();
printf("\n Affichage liste\n");
 for (Courant=Debut;Courant!=NULL;Courant=Courant->AdresseSuivant)
 {
  printf("\n\n%s\n%s\n%d\n%d",  Courant->Nom,
				Courant->Reference,
				Courant->Nombre,
				Courant->Prix);
  }
//getch();
}
