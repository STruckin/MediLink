document.addEventListener('DOMContentLoaded', () => {

    //Pasos registro de pacientes
    var Form1 = document.getElementById("form1");
    var Form2 = document.getElementById("form2");
    var Form3 = document.getElementById("form3");
    var Form4 = document.getElementById("form4");
    var Form5 = document.getElementById("form5");

    var Next1 = document.getElementById("next1");
    var Next2 = document.getElementById("next2");
    var Next3 = document.getElementById("next3");
    var Next4 = document.getElementById("next4");

    var Back1 = document.getElementById("back1");
    var Back2 = document.getElementById("back2");
    var Back3 = document.getElementById("back3");
    var Back4 = document.getElementById("back4");

    var progress = document.getElementById("progress");


    Next1.addEventListener('click', () => {
        Form1.style.left = "-100%";
        Form2.style.left = "40px";
        progress.style.width = "450px";
    });

    Back1.addEventListener('click', () => {
        Form1.style.left = "40px";
        Form2.style.left = "-100%";
        progress.style.width = "225px";
    });

    Next2.addEventListener('click', () => {
        Form2.style.left = "-100%";
        Form3.style.left = "40px";
        progress.style.width = "675px";
    })


    Back2.addEventListener('click', () => {
        Form2.style.left = "40px";
        Form3.style.left = "-100%";
        progress.style.width = "450px";
    });

    Next3.addEventListener('click', () => {
        Form3.style.left = "-100%";
        Form4.style.left = "40px";
        progress.style.width = "900px";
    })


    Back3.addEventListener('click', () => {
        Form3.style.left = "40px";
        Form4.style.left = "-100%";
        progress.style.width = "675px";
    });

    Next4.addEventListener('click', () => {
        Form4.style.left = "-100%";
        Form5.style.left = "40px";
        progress.style.width = "1175px";
    })


    Back4.addEventListener('click', () => {
        Form4.style.left = "40px";
        Form5.style.left = "-100%";
        progress.style.width = "900px";
    });
});