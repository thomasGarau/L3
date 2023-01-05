package td6;

import java.io.*;

public class Deserialiser {
    private Personne personne;

    public Deserialiser(String path) throws ClassNotFoundException, IOException{
        FileInputStream file = new FileInputStream(path);
        ObjectInputStream ois = new ObjectInputStream(file);
        this.personne = (Personne) ois.readObject();
    }

    public Personne getPersonne() {
        return personne;
    }
   
}
