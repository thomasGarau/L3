package exo4;

public class Stylo extends Crayon {	
	private final int limiteEncre;
	private int quantiteEncre;	
	public Stylo(int quantiteEncre ) {
		  super();
		  this.quantiteEncre = quantiteEncre;
		  this.limiteEncre = quantiteEncre / 2;
	}
	public void ecrire(String texte) {
	  if ( !estPlein() )
	    throw new RuntimeException("Presque plus d'encre! ");		  
	  ecrire0(texte);
	  diminuerEncre();   
	 } 
	public void remplir() {
		quantiteEncre = limiteEncre * 2;
	} 
	private boolean estPlein() {
		return quantiteEncre > limiteEncre;
	}
	private void ecrire0( String texte ) {
		System.out.println(texte);
	} 
	private void diminuerEncre() {
	 quantiteEncre--;
	} 
}
