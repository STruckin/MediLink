document.addEventListener('DOMContentLoaded', () => {

    //Pasos registro
    var Form1 = document.getElementById("form1");
    var Form2 = document.getElementById("form2");

    var Next1 = document.getElementById("next1");

    var Back1 = document.getElementById("back1");



    Next1.addEventListener('click', () => {
        Form1.style.left = "-100%";
        Form2.style.left = "40px";
    });

    Back1.addEventListener('click', () => {
        Form1.style.left = "40px";
        Form2.style.left = "-100%";
    });
});