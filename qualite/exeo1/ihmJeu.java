package exeo1;
import java.util.ArrayList;

public class ihmJeu {
    private ControleurJeu ctrlJeu;

    public ihmJeu(){
        this.ctrlJeu = new ControleurJeu(this);
    }

    public void displayWinner(ArrayList<String> listWinner){
        String res = "";
        if(listWinner.size() > 1){
            res += "Il y a " + listWinner.size() + " vainqueur"; 
            for (String string : listWinner) {
                res += string;
            }
        }else{
            res = "Il y a un seule vainqueur " + listWinner.get(0);
        }
        System.out.println(res);
    }

    public void startGame(){
        this.ctrlJeu.initGame();
    }
}
