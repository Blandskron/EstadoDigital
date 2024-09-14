from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings


def custom_404(request, exception=None):
    return redirect('home')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Enviar correo de confirmación
            subject = '¡Tu registro TECH AWARDS 2024 ha sido completado con éxito!'
            message = (
                f'Estimado/a {contact.name} {contact.last_name},\n\n'
                '¡Gracias por inscribirte en el evento de TECH AWARDS 2024! Tu registro ha sido confirmado y estamos emocionados de contar con tu valiosa asistencia.\n\n'
                'En breve, recibirás más información sobre el evento en tu correo electrónico. \n\n'
                'Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en contactarnos.\n\n'
                '¡Nos vemos el 28 de agosto a las 9:00 AM!\n\n'
                'Saludos cordiales,\n'
                'El equipo de TECH AWARDS 2024'
            )
            html_message = (
                f'<p>Estimado/a {contact.name} {contact.last_name},</p>'
                '<p>¡Gracias por inscribirte en el evento de <strong>TECH AWARDS 2024</strong>! Tu registro ha sido confirmado y estamos emocionados de contar con tu valiosa asistencia.</p>'
                '<p>En breve, recibirás más información sobre el evento en tu correo electrónico.</p>'
                '<p>Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en contactarnos.</p>'
                '<p>¡Nos vemos el 28 de agosto a las 9:00 AM!</p>'
                '<p>Saludos cordiales.</p>'
                '<img src="https://img.techawards2024.cl/var/albums/Firma.png?m=1722292354" alt="Firma de TECH AWARDS 2024" style="width: 100%;">'
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [contact.email]
            send_mail(subject, message, from_email, recipient_list, html_message=html_message)

            return redirect('confirmation')
    else:
        form = ContactForm()
    return render(request, 'estadodigital/contact.html', {'form': form})

def confirmation_view(request):
    return render(request, 'estadodigital/confirmation.html')