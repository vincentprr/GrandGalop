const HEADER_LOGO = document.getElementById("infos");
const HEADER = document.querySelector("header");
const HEADER_NAV = document.getElementById("navigation_menu");
const BACKGROUND_COLOR = "linear-gradient(rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 80%)";
const POPUP = document.getElementById("popup");
const POPUP_CONTENT = document.getElementById("popup_content");

const LOGIN_FORM = `
<div class="popup_illus">
    <img src="{{ url_for('static', filename='img/horse_riding.png') }}" alt="user_illus">
</div>
<form class="login_form" method="post" action="{{ url_for('main_js') }}">
    {{ loginForm.hidden_tag() }}

    {{ loginForm.login(placeholder=loginForm.login.label.text) }}
    <div class="input_separator_login"></div>
    {{ loginForm.password(placeholder=loginForm.password.label.text) }}
    <div class="input_separator_login"></div>

    <div class="input_submit_container"><button class="input_submit">Se connecter</button></div>
    <p class="login_register_txt">Pas encore de compte ? <a href="{{ url_for('register') }}">Inscrivez vous.</a></p>
</form>
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

function popup(content, tagName, width = null){
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

function closePopup(){
    if(POPUP != null){
        POPUP.style.display = "none";
        document.body.style.overflow = "";
    }
}

function loginPopup(){
    {% if not current_user.is_authenticated %}
        popup(LOGIN_FORM, "login", "30%");
    {% endif %}
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