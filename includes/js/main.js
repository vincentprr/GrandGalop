const HEADER_LOGO = document.getElementById("infos");

function dynamicScrollLogo(){
    if (window.scrollY > 30){
        HEADER_LOGO.classList.add("fade-out")
    }
}

window.onscroll = function(){
    dynamicScrollLogo();
};

document.onload = function(){
    console.log("11");
    dynamicScrollLogo();
};