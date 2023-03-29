package exeo1;
public class De {
    private  int valeur; 

    public De(){
    }

    public int lancerDe() {
    	this.valeur = (int) (6*Math.random()) + 1;
    	return this.valeur;
    }
}
