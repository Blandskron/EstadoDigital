function downloadICS() {
    // Datos del evento
    const eventName = "Evento en Universidad de Chile";
    const eventLocation = "Casa Central, Universidad de Chile";
    const eventStart = "20241009T113000Z"; // UTC (8:30 AM en Chile es 11:30 UTC)
    const eventEnd = "20241009T213000Z";   // UTC (6:30 PM en Chile es 21:30 UTC)
    const reminder = "-P1D";  // Recordatorio 1 día antes

    // Contenido del archivo .ics
    const icsContent = `
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Your Organization//Your App//EN
BEGIN:VEVENT
UID:${new Date().toISOString().replace(/[-:]/g, '').slice(0, 15)}@yourdomain.com
DTSTAMP:${new Date().toISOString().replace(/[-:]/g, '').slice(0, 15)}
DTSTART:${eventStart}
DTEND:${eventEnd}
SUMMARY:${eventName}
LOCATION:${eventLocation}
DESCRIPTION:Evento en la Universidad de Chile - Casa Central
BEGIN:VALARM
TRIGGER:${reminder}
ACTION:DISPLAY
DESCRIPTION:Recordatorio: ${eventName} en ${eventLocation} mañana.
END:VALARM
END:VEVENT
END:VCALENDAR`;

    // Crear un archivo Blob para la descarga
    const blob = new Blob([icsContent], { type: 'text/calendar' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'evento_universidad_de_chile.ics';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}