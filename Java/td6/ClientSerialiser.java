package td6;
import java.io.*;
import java.net.*;

public class ClientSerialiser {
    
    public static void main(String[] args) throws IOException {

        final BufferedReader in;
        final PrintWriter out;
        try{
            while (true){
                Socket socket = new Socket(InetAddress.getLocalHost(), 2000);
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                Personne personne1 = new Personne("susiBaka", "anthony", 8);
                ObjectOutputStream ois = new ObjectOutputStream(socket.getOutputStream());
                ois.writeObject(personne1);
                socket.close();
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
