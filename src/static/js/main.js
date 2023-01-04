const HEADER_LOGO = document.getElementById("infos");
const HEADER = document.querySelector("header");
const HEADER_NAV = document.getElementById("navigation_menu");
const BACKGROUND_COLOR = "linear-gradient(rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 80%)";
const POPUP = document.getElementById("popup");
const POPUP_CONTENT = document.getElementById("popup_content");

const LOGIN_FORM = `

`;

function currentScrollYPercentage()
{
    let scrollTop = window.scrollY;
    let docHeight = document.body.offsetHeight;
    let winHeight = window.innerHeight;
    let scrollPercent = scrollTop / (docHeight - winHeight);

    return Math.round(scrollPercent * 100);
}

function dynamicScroll(){
    if (window.scrollY > 5 && window.scrollY > HEADER.offsetHeight / 3 - HEADER_NAV.offsetHeight){
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

function popUp(content, tagName, width = null){
    if(POPUP != null && POPUP_CONTENT != null){
        // TO DO Change content if not the same source otherwise just print handle it with a tag
        POPUP.style.display = "flex";

        if(POPUP.getAttribute("type") != tagName){
            if(width != null)
                POPUP_CONTENT.style.width = width;

            POPUP.setAttribute("type", tagName);

            POPUP_CONTENT.innerHTML = content;
        }

        document.body.style.overflow = "hidden";
    }
}

function closePopUp(){
    if(POPUP != null){
        POPUP.style.display = "none";
        document.body.style.overflow = "";
    }
}

function loginPopUp(){
    popUp(LOGIN_FORM, "login", "40%");
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