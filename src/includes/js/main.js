const HEADER_LOGO = document.getElementById("infos");

function currentScrollYPercentage()
{
    return ((document.documentElement.scrollTop + document.body.scrollTop) / (document.documentElement.scrollHeight - document.documentElement.clientHeight) * 100);
}

function dynamicScrollLogo(){
    if (currentScrollYPercentage() > 50){
        HEADER_LOGO.classList.remove("fade-in");
        HEADER_LOGO.classList.add("fade-out");
    }
    else{
        HEADER_LOGO.classList.remove("fade-out");
        HEADER_LOGO.classList.add("fade-in");
    }
}

function dynamicalRenders(){
    dynamicScrollLogo();
}

window.onscroll = function(){
    dynamicalRenders();
};

document.onload = function(){
    dynamicalRenders();
};