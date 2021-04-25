let div = document.getElementById("oeuvre_visionner");
let is_img = false;

function resize(img, bigger){
    let ratio = 0;
    if(bigger == img.height){
        ratio = (400 * 100) / img.height;
        img.height = 400;
        img.width = (img.width * ratio) / 100; 
    }else{
        ratio = (400 * 100) / img.width;
        img.width = 400;
        img.height = (img.height * ratio) / 100; 
    }
}

function display_img(url_img){
    if(is_img == true){
        stop_display();
    }
    let img = new Image();
    img.src = url_img;    
    console.log(img.width, img.height);
    bigger = Math.max(img.height, img.width);
    resize(img, bigger);
    console.log(img.width, img.height);
    div.appendChild(img)

    let button = document.createElement("button");
    button.innerHTML = "Effacer";
    button.id = "effacer";
    div.appendChild(button);
    div.style.display = "flex";
    div.style.flexDirection = "column";
    button.onclick = stop_display;
    is_img = true;
}

function stop_display(){
    div.removeChild(div.firstChild);
    div.removeChild(div.firstChild);
    is_img = false;
}