int main()
{
    unsigned char cR,cV,cB;   // contient les taux de rouge de vert et de bleu
    unsigned int cRVB;   //couleur à saisir au clavier (en hexa)
    unsigned int valeurDuGris;   // valeur du gris : à  calculer à partir de la formule donnée
    unsigned int nouvelleCouleurEnGris=0;   // valeur de la couleur, une fois convertie en gris
    printf("Saisissez un entier en hexa : ");
    scanf("%x",&cRVB);
    // Récupérer les taux de rouge, de vert et de bleu
    cR= cRVB;
    cV= cRVB>>8;
    cB= cRVB>>16;
    printf("Couleur saisie rouge:%x vert:%x bleu:%x\n",cR,cV,cB);
    // Conversion de chaque taux en utilisant la formule donnée, puis calcul de la valeur du niveau de gris
    cR= cR * .299;
    cV= cV * .587;
    cB= cB * .114;
    valeurDuGris = cR + cV + cB;
    printf("Le niveau de gris vaut :%x\n",valeurDuGris);
    // construire la nouvelle couleur en niveau de gris
    nouvelleCouleurEnGris= (valeurDuGris<<16) | (valeurDuGris<<8) | valeurDuGris;
    printf("Couleur convertie en niveau de gris  %0.8x ",nouvelleCouleurEnGris);
}