# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    data_sharing_consent = forms.ChoiceField(
        choices=[(True, 'Sí'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Autoriza que sus datos sean compartidos con empresas participantes de este evento"
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'last_name',
            'rut',
            'email',
            'phone_number',
            'company',
            'region',
            'track_of_interest',
            'data_sharing_consent',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Nombre',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Apellido',
                'class': 'form-control',
            }),
            'rut': forms.TextInput(attrs={
                'placeholder': 'RUT',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Correo electrónico',
                'class': 'form-control',
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Teléfono de contacto',
                'class': 'form-control',
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'Institución a la que representa',
                'class': 'form-control',
            }),
            'region': forms.TextInput(attrs={
                'placeholder': 'Región',
                'class': 'form-control',
            }),
            'track_of_interest': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
