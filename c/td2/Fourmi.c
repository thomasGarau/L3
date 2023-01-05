#include "fourmi.h"
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

Fourmi init(){
    printf("d");
    Fourmi a = {
        .x = rand() %3,
        .y = rand() %3,
        .dx = rand() %3,
        .dy = rand() %3,
        .couleur = rand() %256,
        .symbole = (char)(65 + rand() %26),
    };
    return a;
}


void avance(Fourmi *pt_sur_fourmi){
    //utilisation de modulo pour que si on dépasse les bonrne on recommence de l'autre coté de l'écran
    // on verifie avec le if de ne pas faire un modulo négatif 
    if (pt_sur_fourmi->x + pt_sur_fourmi->dx < 0){
        pt_sur_fourmi->x = BORNE_X + pt_sur_fourmi->dx;
    }else{
        pt_sur_fourmi->x =(pt_sur_fourmi->x + pt_sur_fourmi->dx) % BORNE_X;
    }
    
    if (pt_sur_fourmi->y + pt_sur_fourmi->dy < 0){
        pt_sur_fourmi->y = BORNE_Y + pt_sur_fourmi->dy;
    }else{
        pt_sur_fourmi->y = (pt_sur_fourmi->y + pt_sur_fourmi->dy) % BORNE_Y;
    }
}

void affiche_p(Fourmi fourmi){
    printf("sa position x est :%d\n sa position y est:%d\n sa vitesse de déplacement x est:%d\n sa vitesse de deplacement y est :%d\n sa couleur est :%d\n fourmi.couleur, son symbole est :%c\n fourmi.symbole", fourmi.x, fourmi.y, fourmi.dx, fourmi.dy, fourmi.couleur, fourmi.symbole);
}

int main(int argc, char const *argv[])
{
    srand(time(NULL)); 
    Fourmi f = init();
    affiche_p(f);
    return 0;
}
