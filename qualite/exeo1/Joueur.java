package exeo1;
public class Joueur {
    private String nom;
    private static De de = new De();

    public Joueur(String nom){
        this.nom = nom;
    }

    public String getNom(){
        return this.nom;
    }
    
    public int jouerUnTour() {
		int total=0;
		for( int i=0;i<2; i++) {
			total+= de.lancerDe();
		}
		return total;
	}
}
