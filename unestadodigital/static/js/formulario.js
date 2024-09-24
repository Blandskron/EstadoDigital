document.addEventListener('DOMContentLoaded', function () {
    // Agrupamos los tracks por horario
    const scheduleGroups = {
        '9:00 - 9:30 Hrs': ['Inauguración'],
        '9:30 - 10:15 Hrs': ['Keynote'],
        '10:45 - 12:15 Hrs': ['Inteligencia artificial'],
        '12:20 - 13:30 Hrs': ['Gobernanza de Datos', 'Suministro de Tecnología'],
        '14:30 - 15:45 Hrs': ['Identidad Digital', 'Servicios Digitales Integrados'],
        '15:50 - 17:00 Hrs': ['Talento Global', 'Ciberseguridad'],
        '17:05 - 18:00 Hrs': ['Cierre y Premiación'],
    };

    // Iterar sobre cada grupo de tracks y agregar lógica para deseleccionar los otros
    for (const [schedule, tracks] of Object.entries(scheduleGroups)) {
        tracks.forEach(track => {
            const trackCheckbox = document.querySelector(`input[value="${track}"]`);
            if (trackCheckbox) {
                trackCheckbox.addEventListener('change', function () {
                    if (this.checked) {
                        // Desmarcar los otros checkboxes del mismo grupo horario
                        tracks.forEach(otherTrack => {
                            if (otherTrack !== track) {
                                const otherTrackCheckbox = document.querySelector(`input[value="${otherTrack}"]`);
                                if (otherTrackCheckbox) {
                                    otherTrackCheckbox.checked = false;
                                }
                            }
                        });
                    }
                });
            }
        });
    }
});