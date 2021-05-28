let p = document.getElementById("texte");

let img_1 = document.getElementById("img_1");
let img0 = document.getElementById("img0");
let img1 = document.getElementById("img1");

let url_img_1_n = document.currentScript.getAttribute('one');
let url_img0_n = document.currentScript.getAttribute('two');
let url_img1_n = document.currentScript.getAttribute('three');
let url_img_1_f = document.currentScript.getAttribute('four');
let url_img0_f = document.currentScript.getAttribute('five');
let url_img1_f = document.currentScript.getAttribute('six');


function change_texte(){
    if(choice.checked){
        p.style.color = "black";
        img_1.setAttribute("src", url_img_1_f);
        img0.setAttribute("src", url_img0_f);
        img1.setAttribute("src", url_img1_f);
    }else{
        p.style.color = "white";
        img_1.setAttribute("src", url_img_1_n);
        img0.setAttribute("src", url_img0_n);
        img1.setAttribute("src", url_img1_n);
    }
}

let choice = document.getElementById("choix");
choice.addEventListener("click", change_texte);

