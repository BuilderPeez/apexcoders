let body = document.querySelector("body");
let rash = document.querySelector(".rash");
let icon = document.querySelector(".bi-moon-fill");

rash.addEventListener('click', () => {
    body.classList.toggle("dark")
    if(body.classList.contains("dark")){
        icon.classList.replace("bi-moon-fill", "bi-sun-fill");
    }
    else{
        icon.classList.replace("bi-sun-fill", "bi-moon-fill");
    }
});