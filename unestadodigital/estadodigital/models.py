from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellido", max_length=100)
    rut = models.CharField("RUT", max_length=20)
    email = models.EmailField("Correo electrónico")
    phone_number = models.CharField("Teléfono de contacto", max_length=20)
    company = models.CharField("Institución a la que representa", max_length=100)
    region = models.CharField("Región", max_length=100)
    track_of_interest = models.ForeignKey(
        Track,
        verbose_name="Track de su interés",
        on_delete=models.CASCADE
    )
    data_sharing_consent = models.BooleanField(
        "Autoriza que sus datos sean compartidos con empresas participantes de este evento",
        default=False
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"
