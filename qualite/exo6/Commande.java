package exo6;

public class Commande {
	
	private double taux;
	private double montantHT;
	
	public Commande(TVA tva, double montantHT) {
		this.montantHT=montantHT;
		this.taux=tva.getTaux();
	}
	public double getTotalTTC() {
		return (taux+1)*montantHT;	
	}
}
