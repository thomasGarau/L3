package exeo1;
import java.util.ArrayList;

public class ControleurJeu {
    private ihmJeu ihm;
    private Jeu jeu;

    public ControleurJeu(ihmJeu ihm){
        this.ihm = ihm;
        this.jeu = new Jeu(this);
    }

    public void displayWinner(ArrayList<String> nom){
        ihm.displayWinner(nom);
    }

    public void initGame(){
        Joueur j1= new Joueur("Pierre");
		Joueur j2= new Joueur("Jean");
		Joueur j3= new Joueur("Marie");
		this.jeu.ajouterJoueur(j3);
		this.jeu.ajouterJoueur(j2);
		this.jeu.ajouterJoueur(j1);
		this.jeu.bataille();
    }
}
