#define BORNE_X 400; 
#define BORNE_Y 200; 

typedef struct
{
    int x,y;
    int dx,dy;
    int couleur;
    char symbole;

}Fourmi;

Fourmi init();
void avance(Fourmi *pt_Fourmi);
void affiche_p(Fourmi fourmi);
Fourmi affiche_c(Fourmi fourmi);

