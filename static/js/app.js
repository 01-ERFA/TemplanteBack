
const menu = document.getElementById("menuCompress")
const navbar_menu = document.getElementById("navbar_menu")


menu.addEventListener("click", ()=>{
    if (navbar_menu.style.display === "" || navbar_menu.style.display === "none") {
        navbar_menu.style.display = "block"
    } else {
        navbar_menu.style.display = "none"
    }
})