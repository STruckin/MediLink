document.addEventListener('DOMContentLoaded', () => {
    // Secciones
    const forms = {
        form1: document.getElementById("form1"),
        form2: document.getElementById("form2"),
        form3: document.getElementById("form3"),
        form4: document.getElementById("form4"),
        form5: document.getElementById("form5")
    };

    const progress = document.getElementById("progress");

    // Función para navegar a una sección específica
    window.navigateToSection = function (formId) {
        // Ocultar todas las secciones
        for (let form in forms) {
            if (forms[form]) forms[form].style.left = "-100%";
        }

        // Mostrar la sección seleccionada
        if (forms[formId]) {
            forms[formId].style.left = "40px";

            // Actualizar el progreso según la sección
            switch (formId) {
                case 'form1':
                    progress.style.width = "20%";
                    break;
                case 'form2':
                    progress.style.width = "35%";
                    break;
                case 'form3':
                    progress.style.width = "60%";
                    break;
                case 'form4':
                    progress.style.width = "80%";
                    break;
                case 'form5':
                    progress.style.width = "95%";
                    break;
            }
        }
    };

    // Lógica existente para botones "Siguiente" y "Atrás"
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

    Next1.addEventListener('click', () => {
        Form1.style.left = "-100%";
        Form2.style.left = "40px";
        progress.style.width = "35%";
    });

    Back1.addEventListener('click', () => {
        Form1.style.left = "40px";
        Form2.style.left = "-100%";
        progress.style.width = "20%";
    });

    Next2.addEventListener('click', () => {
        Form2.style.left = "-100%";
        Form3.style.left = "40px";
        progress.style.width = "60%";
    });

    Back2.addEventListener('click', () => {
        Form2.style.left = "40px";
        Form3.style.left = "-100%";
        progress.style.width = "35%";
    });

    Next3.addEventListener('click', () => {
        Form3.style.left = "-100%";
        Form4.style.left = "40px";
        progress.style.width = "80%";
    });

    Back3.addEventListener('click', () => {
        Form3.style.left = "40px";
        Form4.style.left = "-100%";
        progress.style.width = "60%";
    });

    Next4.addEventListener('click', () => {
        Form4.style.left = "-100%";
        Form5.style.left = "40px";
        progress.style.width = "95%";
    });

    Back4.addEventListener('click', () => {
        Form4.style.left = "40px";
        Form5.style.left = "-100%";
        progress.style.width = "80%";
    });
});

document.addEventListener("input", function (event) {
    if (event.target.classList.contains("auto-expand")) {
        autoExpand(event.target);
    }
});

function autoExpand(field) {    //Logica para expandir los inputs
    field.style.height = "auto";
    field.style.height = field.scrollHeight + "px";
}