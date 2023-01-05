package td6;
import java.io.*;
import java.net.*;

public class Serveur {
    private static int nbFile;
    public static void main(String[] args) throws ClassNotFoundException, IOException {
        BufferedReader in;
        PrintWriter out;
        try{
            ServerSocket server = new ServerSocket(2000);
            Socket socket = server.accept();
            System.out.println("Nouvel utilisateur connecté");
            while (true){

                //créer et écrit dans un fichier le contenu recu du client 
                String path = String.format("./td6/fichierSerialiser/file%s", nbFile);
                File file = new File(path);
                FileOutputStream fos = new FileOutputStream(file);

                //recois le flux
	            ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
                ObjectOutputStream oos = new ObjectOutputStream(fos);          
                
                oos.writeObject((Personne)ois.readObject());
                oos.close();
                nbFile++;

	            socket.close();
	            server.close(); 

                //creer le nouvel objet 
                Deserialiser d = new Deserialiser(path);
                Personne personne1 = d.getPersonne();
                System.out.print(personne1);
            }
           
        }catch(IOException e){
            e.printStackTrace();
        }
    }

}
