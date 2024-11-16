document.addEventListener('DOMContentLoaded', function() {
    // Asegúrate que flatpickr está disponible
    if (typeof flatpickr !== 'undefined') {
        const calendar = flatpickr("#calendar", {
            locale: "es",
            inline: true,
            dateFormat: "Y-m-d",
            defaultDate: "today",
            enableTime: false,
            monthSelectorType: "dropdown",
            
            onChange: function(selectedDates, dateStr, instance) {
                console.log('Fecha seleccionada:', dateStr);
                // Aquí irá tu código para manejar el cambio de fecha
            }
        });
        
        // Verifica que el calendario se inicializó
        console.log('Calendario inicializado:', calendar);
    } else {
        console.error('Flatpickr no está cargado');
    }
});