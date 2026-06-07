from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Contact
from .forms import ContactForm

class ContactModelTest(TestCase):
    def test_contact_creation(self):
        contact = Contact.objects.create(
            name="Juan",
            last_name="Pérez",
            rut="12345678-9",
            email="juan.perez@example.com",
            phone_number="+56912345678",
            company="Universidad de Chile",
            position="Desarrollador",
            region="Región Metropolitana",
            track_of_interest=["Inauguración", "Keynote"],
            data_sharing_consent=True
        )
        self.assertEqual(str(contact), "Juan Pérez")
        self.assertEqual(contact.rut, "12345678-9")

class ContactFormTest(TestCase):
    def test_valid_form_multiple_tracks(self):
        # Different time slots: Inauguración (8:30 - 9:30) and Keynote (9:30 - 10:15)
        form_data = {
            'name': 'Juan',
            'last_name': 'Pérez',
            'rut': '12345678-9',
            'email': 'juan.perez@example.com',
            'phone_number': '+56912345678',
            'company': 'Universidad de Chile',
            'position': 'Desarrollador',
            'region': 'Región Metropolitana',
            'track_of_interest': ['Inauguración', 'Keynote'],
            'data_sharing_consent': 'True'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_overlapping_tracks(self):
        # Same time slot: Gobernanza de Datos (12:20 - 13:30) and Suministro de Tecnología (12:20 - 13:30)
        form_data = {
            'name': 'Juan',
            'last_name': 'Pérez',
            'rut': '12345678-9',
            'email': 'juan.perez@example.com',
            'phone_number': '+56912345678',
            'company': 'Universidad de Chile',
            'position': 'Desarrollador',
            'region': 'Región Metropolitana',
            'track_of_interest': ['Gobernanza de Datos', 'Suministro de Tecnología'],
            'data_sharing_consent': 'True'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('track_of_interest', form.errors)
        self.assertIn("Solo puede seleccionar un track en el bloque horario de 12:20 - 13:30 Hrs.", form.errors['track_of_interest'][0])

