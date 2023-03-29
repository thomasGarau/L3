//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused


#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <stdlib.h>

int *PointeurBase, *PointeurHaut, *PointeurTete, *PointeurQueue;

/*------------------ Initialisation -------------------------------*/
int  init ( int Taille) {
if (PointeurBase=(int *)(malloc(Taille*sizeof(int))))
	return 0;
	else return 1;}

/*------------------ Affichage ------------------------------------*/
void affiche(void) {
int *PointeurCourant, i=0;
//gotoxy(25,5);
puts("\nFile actuelle\n");
PointeurCourant=PointeurQueue;
   while (PointeurCourant!=PointeurTete)
	{
    //gotoxy(30,6+i++);
	//cprintf("\n%d",*PointeurCourant++);
    printf("\n%d",*PointeurCourant++);
	if (PointeurCourant>PointeurHaut)
		PointeurCourant=PointeurBase;}
		   }

/*-------------------- Ajout Valeur --------------------------------*/
void Enfile( int Valeur )
{
*PointeurTete = Valeur;
PointeurTete ++;
if(PointeurTete > PointeurHaut){
  PointeurTete = PointeurBase;
}
if(PointeurTete = PointeurQueue){
  PointeurQueue ++;
}



}

/*static compteur = 0;
PointeurBase[compteur % taille];
compteur ++
*/
/*---------------------- Enleve Valeur ------------------------------*/
int Defile(int *Valeur) 
{
if(PointeurTete = PointeurQueue){
  return -1;
}else{
  *PointeurQueue = *PointeurQueue +1;
  *Valeur = *PointeurQueue;
  if(PointeurQueue >= PointeurHaut){
    PointeurQueue = PointeurBase;
  }
  return 0;
}

	
}

/*-------------------- Fonction Principale ------------------------*/
int main(int argc, char const *argv[])
{
int Valeur,Taille;
char c;
  //clrscr();
  puts("\nGestion d'une File circulaire ...");
  puts("\nD�finir la taille de la file circulaire");
  scanf("%d",&Taille);
  if (init(Taille))
	{printf("\nAllocation m�moire impossible ...");
	exit(0);}
  PointeurHaut=PointeurBase+(unsigned int)Taille; 
  PointeurTete=PointeurQueue=PointeurBase;
  do
  { puts("\n\n\nMenu: Enfiler, Defiler, Visualiser, Quitter ");
  c=(toupper(getch()));
  //clrscr();
    switch(c) {
    case 'E':  	{puts("Saisie de la valeur � enfiler");
		scanf("%d",&Valeur);
		Enfile (Valeur);
		affiche();
		break;}

    case 'D':  {if(Defile(&Valeur))
		{//clrscr();
		puts("\nFile vide");}
		else {printf("\n\nLa valeur defil�e: %d",Valeur);
		affiche();}
		break;}

   case 'V':  {affiche();
	       break;}

   default: puts("Choix incorrect ..."); }

  }while(c!='Q');
  return 0;
}


