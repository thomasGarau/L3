package exo5;

public class Test {
    public static void main(String[] args) {
        Personne personne = new Personne(false, "didier");
        Personne personne2 = new Personne(true, "jean");
        PresencesCours pc = new PresencesCours();
        pc.arriveEnCours(personne);
        pc.arriveEnCours(personne2);
        System.out.println(pc.toString());
    }
}
