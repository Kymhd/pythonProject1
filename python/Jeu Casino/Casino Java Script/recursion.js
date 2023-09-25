// Programme debutant !!!!!!
var continuePartie = true;
var depot = 0;

while (continuePartie){
    var numeroGagnat = Math.floor(Math.random() * (49 - 1 + 1)) + 1; //Valeur que l'utilisateur va essayer de deviner
    while (depot <= 0) {
        var montant = prompt("Saississez votre montant: ");
        // Convertir la chaîne en nombre
        montant = Number(montant);
        if (isNaN(montant)) {
            console.log("Vous n'avez pas saisi du chiffre");
        } else if (montant === 0) {
            console.log("Vous avez saisi: 0");
        } else {
            depot = montant;
            break;
        }
    }
    console.log("Vous avez deposé", depot, "KMF");

    var numeroUser = -1;

    while (numeroUser <= 0 || numeroUser > 49) {
        var numero = prompt("Entrez votre numéro: ");

        numero = Number(numero);
        if (isNaN(numero)) {
            console.log("Vous n'avez pas saisi un chiffre");
        } else {
            numeroUser = numero;
        }
    }

    console.log("Votre numero est", numeroUser);


    //Boucle qui va gerer la mise de l'utilisateur

    var mise = 0;

    while (mise > depot || mise <= 0) {
        var miseJoueur = prompt("Entrez votre mise: ")

        miseJoueur = Number(miseJoueur)
        if (isNaN(miseJoueur)) {
            console.log("Vous n'avez pas saisir un chiffre ")
        } else if (miseJoueur > depot) {
            console.log(
                "Vous ne pouvez pas miser plus, vous disposez de ",
                depot, "KMF !")
        } else if (miseJoueur === 0) {
            console.log("Vous mise est égale à 0")
        } else {
            mise = miseJoueur
        }
        
    }

    console.log(mise)



    if (numeroGagnat === numeroUser) {
        console.log("BINGO Vous avez gagné, le numéro est", numeroGagnat, mise * 3);
        depot = depot + mise * 3
    } else if  (numeroGagnat % 2 == numeroUser % 2){
        console.log("Vous avez misé sur la bonne couleur"
        ,numeroGagnat, "vous avez gnagné ", mise * 0.5)
        depot = depot + mise * 0.5
    } else {
        console.log(
            "Vous aurez de la cahnce au prochain tour, le numéro etait",
            numeroGagnat
        );
        depot -= mise
    }



    console.log("")

    if (depot <= 0){
        console.log("Vous ne disposez plus de fonds", depot);
        continuePartie = false
    } else {
        console.log("vous disposez à présent", depot, " KMF")
        var quitter = prompt ("Souhaitez-vous quitter le casinon ?")

        if (quitter === 'o' || quitter === 'O'){
            console.log("Vous quiitez le casino avec", depot, "KMF")
            continuePartie = false
        }
    } 

}
