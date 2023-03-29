package exeo1;
import java.util.ArrayList;

class Jeu
{
	private ArrayList<String> nomsGagnants = new ArrayList<String>(); 
	private ArrayList<Joueur> listJoueur = new ArrayList<Joueur>();
	private ControleurJeu ctrlJeu;

	public Jeu(ControleurJeu ctrlJeu) {
		this.ctrlJeu = ctrlJeu;
	}

	public void ajouterJoueur(Joueur joueur) {
		listJoueur.add(joueur);
	}
	
	public void bataille() {
		int score,max=0;
		for (Joueur joueur:listJoueur) {
			score = joueur.jouerUnTour();
			if (score>max) {
				max=score;
				this.nomsGagnants.clear();
				this.nomsGagnants.add(joueur.getNom());
			}
			else if (score==max) {
				this.nomsGagnants.add(joueur.getNom());
			}
		}
		ctrlJeu.displayWinner(this.nomsGagnants);
	}
    
}
