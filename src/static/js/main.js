const HEADER_LOGO = document.getElementById("infos");
const HEADER = document.querySelector("header");
const HEADER_NAV = document.getElementById("navigation_menu");
const BACKGROUND_COLOR = "linear-gradient(rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 80%)";
const POPUP = document.getElementById("popup");

function currentScrollYPercentage()
{
    return ((document.documentElement.scrollTop + document.body.scrollTop) / (document.documentElement.scrollHeight - document.documentElement.clientHeight) * 100);
}

function dynamicScroll(){
    let scroll = currentScrollYPercentage();
    if (scroll > 50){
        HEADER_LOGO.classList.remove("fade-in");
        HEADER_LOGO.classList.add("fade-out");
    }
    else{
        HEADER_LOGO.classList.remove("fade-out");
        HEADER_LOGO.classList.add("fade-in");
    }

    if(document.documentElement.scrollTop + document.body.scrollTop > HEADER.offsetHeight - HEADER_NAV.offsetHeight)
        HEADER_NAV.style.background = BACKGROUND_COLOR;
    else
        HEADER_NAV.style.background = "";
}

function popUp(){
    if(POPUP != null){
        // TO DO Change content if not the same source otherwise just print handle it with a tag
        POPUP.style.display = "flex";
        document.body.style.overflow = "hidden";
    }
}

function closePopUp(){
    if(POPUP != null){
        POPUP.style.display = "none";
        document.body.style.overflow = "";
    }
}

function dynamicalRenders(){
    dynamicScroll();
}

window.onscroll = function(){
    dynamicalRenders();
};

document.onload = function(){
    dynamicalRenders();
};