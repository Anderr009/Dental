//Calculando la pantalla
var div = document.getElementById("sidebar");
var img = document.getElementById("img-main")
div.style.height = window.innerHeight + "px";
img.style.height = (window.innerHeight - 1) + "px";