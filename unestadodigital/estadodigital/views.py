from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.conf import settings


def custom_404(request, exception=None):
    return redirect('home')

def send_confirmation_email(contact):
    """
    Función para enviar el correo electrónico de confirmación
    """
    subject = '¡Tu registro UN ESTADO DIGITAL 2024 ha sido completado con éxito!'
    message = (
        f'Estimado/a {contact.name} {contact.last_name},\n\n'
        '¡Gracias por inscribirte en el evento de UN ESTADO DIGITAL 2024! Tu registro ha sido confirmado y estamos emocionados de contar con tu valiosa asistencia.\n\n'
        'En breve, recibirás más información sobre el evento en tu correo electrónico. \n\n'
        'Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en contactarnos.\n\n'
        'Saludos cordiales,\n'
        'El equipo de UN ESTADO DIGITAL 2024'
    )
    html_message = (
        f'<p>Estimado/a {contact.name} {contact.last_name},</p>'
        '<p>¡Gracias por inscribirte en el evento de <strong>UN ESTADO DIGITAL 2024</strong>! Tu registro ha sido confirmado y estamos emocionados de contar con tu valiosa asistencia.</p>'
        '<p>En breve, recibirás más información sobre el evento en tu correo electrónico.</p>'
        '<p>Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en contactarnos.</p>'
        '<p>Saludos cordiales.</p>'
    )
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [contact.email]

    try:
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    except BadHeaderError:
        return HttpResponse('Encabezado inválido en el correo electrónico.')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            form.save_m2m()  # Guardar los ManyToMany relationships como los tracks de interés

            # Enviar correo de confirmación
            send_confirmation_email(contact)

            # Redirigir a la página de confirmación (PRG)
            return redirect('confirmation')
    else:
        form = ContactForm()

    return render(request, 'estadodigital/contact.html', {'form': form})

def confirmation_view(request):
    return render(request, 'estadodigital/confirmation.html')
