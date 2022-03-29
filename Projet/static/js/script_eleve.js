/* Affiche et masque les éléments de ma section du fichier eleve.html*/

let clique_ici = document.getElementById("clique_ici");
let autre = document.querySelectorAll(".parfait");
let control_classe = document.getElementById("controlclasse");
let debute_appel = document.getElementById("debutappel");
let affiche_liste_classe = document.querySelector(".affichelisteclasse");


/* *************Controle du bouton clique ici*************  */
autre.forEach((item) => 
{  
    clique_ici.addEventListener('click', () =>
    {
        debute_appel.style.display = "none";

        affiche_liste_classe.style.display = "none";

        if(getComputedStyle(item).display != "none") 
        {
            item.style.display = "none";
        } 
        else 
        {
            item.style.display = "block";
        } 
          
    }) 
})

/* *************Controle du bouton clique ici*************  */


/*  *****************Controle du bouton vérifie si l'élève fait partie de la classe**********   */
control_classe.addEventListener("click", () =>
    { 
        if (getComputedStyle(debute_appel).display != "none")
        {
            debute_appel.style.display = "none";
        } 
        else 
        {
            debute_appel.style.display = "block";

            autre.forEach((item) => 
            { 
                item.style.display = "none";

            })       
        }      
    }) 

/*  ***********Controle du bouton vérifie si l'élève fait partie de la classe**********  */


/* ****************Controle du bouton debute appel***************  */

debute_appel.addEventListener("click", () => 
{

    if (getComputedStyle(affiche_liste_classe).display != "none")

    {
        affiche_liste_classe.style.display = "none";
    } 
    else 
    {
        affiche_liste_classe.style.display = "block";

        debute_appel.style.display = "none";               
    } 

})



/* ****************Controle du bouton debute appel***************  */





 /*  *******************code non utilisé*****************  /

for(let i = 0; i < autre.length; i++)
{
    clique_ici.addEventListener("click", () => {

        if (getComputedStyle(autre[i]).display != "none")
        {
            autre[i].style.display = "none";
        } 
        else 
        {
            autre[i].style.display = "block";
        } 
        
        }) 
} 


clique_ici.addEventListener("click", () =>{
    for(let i = 0; i < parag1.length; i++){

        let af = parag1[i]
            
        if( getComputedStyle(af).display != "none"){
            
            af.style.display = "none";
        } else {
            af.style.display = "block";  
        }
    }       
    }) 


for(let i = 0; i < parag1.length; i++){

    let af = parag1[i]
    let disparaitre =function () {
        
       if( this.style.display != "none"){
        
        this.style.display = "none";
       } else {
        this.style.display = "block";  
       }
    }
    clique_ici.addEventListener('click', disparaitre)
} 
   ******************* Code non utilisé********************** */  

