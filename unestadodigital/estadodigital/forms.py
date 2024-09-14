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
            'track_of_interest',  # Asegúrate de incluir este campo
            'data_sharing_consent',
        ]
        widgets = {
            'track_of_interest': forms.Select(attrs={'class': 'form-control'}),
        }
