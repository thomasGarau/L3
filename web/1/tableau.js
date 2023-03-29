let sequence = [1, 1, 2, 3, 5, 8, 13];

const tab2 = sequence.map(e => e*2);
// for(i=0; i<sequence.length; i++){
//     sequence[i] = sequence[i] * 2;
// }
let total = 0;
const tableauPaire = sequence.filter((e) => e%2 === 0)
const tableauImPaire = sequence.filter((e) => e%2 !== 0)
const tableauSomme = sequence.reduce((sum,e) => sum+e);
const isPaire = sequence.filter(e => e % 2 != 0).length != 0;

const football = [ 
    {club: "SCB", joueur:"SANTELLI", but:2},
    {club: "SCB", joueur:"MAGRI", but:1},
    {club: "HAC", joueur:"KITALA", but:3},
    {club: "SCB", joueur:"ROBIC", but:3},
    {club: "BORDEAUX", joueur:"MAJA", but:4}
]

let max = 0;
//const nbBute = football.filter((e) => e.club === "SCB").map(e => max += e.but +1);
const map = football.map((e) => {
    if (e.club === "SCB"){
        max += e.but + 1;
    }
})
console.log(max);

