function main(choix, s){
    console.log(choix, s);
    let randomValue = Math.floor(Math.random() * 6);
    let randomSomme = Math.floor(Math.random() * 11);
    let somme = randomValue + parseInt(choix);
    let joueurGuess = parseInt(s);
    const regex = /^\d/;
    if(choix.match(regex) && s.match(regex)){
        console.log("aa");
        if(Math.abs(somme - joueurGuess) === Math.abs(somme - randomSomme)){
            document.getElementById("response").value = "egalité";
            document.getElementById("valueBot").value = randomValue;
            document.getElementById("sommeBot").value = randomSomme;
        }
        else if(Math.abs(somme - joueurGuess) < Math.abs(somme - randomSomme)){
            document.getElementById("response").value = "gagné";
            document.getElementById("valueBot").value = randomValue;
            document.getElementById("sommeBot").value = randomSomme;
            document.getElementById("score").value = document.getElementById("score").value.parseInt + 1
            document.getElementById("score_joueur").value = document.getElementById("score").value;
        }
        else{
            document.getElementById("response").value = "perdu";
            document.getElementById("valueBot").value = randomValue;
            document.getElementById("sommeBot").value = randomSomme;
        }
    }else{
        alert("seule les nombre sont autorisé"); 
    }
    return false;
}

function save(pseudo, score){
    console.log(pseudo, score);
}