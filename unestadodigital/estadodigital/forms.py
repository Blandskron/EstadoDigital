from django import forms
from .models import Contact

# Lista de tracks con horarios reales cargados directamente
TRACKS = [
    ('Inauguración', 'Inauguración (8:30 - 9:30 Hrs)'),
    ('Keynote', 'Keynote speaker (9:30 - 10:15 Hrs)'),
    ('Inteligencia artificial', 'Inteligencia artificial (10:45 - 12:15 Hrs)'),
    ('Gobernanza de Datos', 'Gobernanza de Datos (12:20 - 13:30 Hrs)'),
    ('Suministro de Tecnología', 'Suministro de Tecnología y Compras Públicas (12:20 - 13:30 Hrs)'),
    ('Identidad Digital', 'Identidad Digital (14:30 - 15:45 Hrs)'),
    ('Servicios Digitales Integrados', 'Servicios Digitales Integrados (14:30 - 15:45 Hrs)'),
    ('Talento Global', 'Talento Global (15:50 - 17:00 Hrs)'),
    ('Ciberseguridad', 'Ciberseguridad (15:50 - 17:00 Hrs)'),
    ('Cierre y Premiación', 'Cierre y Premiación (17:05 - 18:00 Hrs)'),
]

# Horarios agrupados para validación
SCHEDULE_GROUPS = {
    '8:30 - 9:30 Hrs': ['Inauguración'],
    '9:30 - 10:15 Hrs': ['Keynote'],
    '10:45 - 12:15 Hrs': ['Inteligencia artificial'],
    '12:20 - 13:30 Hrs': ['Gobernanza de Datos', 'Suministro de Tecnología'],
    '14:30 - 15:45 Hrs': ['Identidad Digital', 'Servicios Digitales Integrados'],
    '15:50 - 17:00 Hrs': ['Talento Global', 'Ciberseguridad'],
    '17:05 - 18:00 Hrs': ['Cierre y Premiación'],
}

# Lista de regiones de Chile
REGIONS = [
    ('Arica y Parinacota', 'Arica y Parinacota'),
    ('Tarapacá', 'Tarapacá'),
    ('Antofagasta', 'Antofagasta'),
    ('Atacama', 'Atacama'),
    ('Coquimbo', 'Coquimbo'),
    ('Valparaíso', 'Valparaíso'),
    ('Región Metropolitana', 'Región Metropolitana'),
    ('O\'Higgins', 'O\'Higgins'),
    ('Maule', 'Maule'),
    ('Ñuble', 'Ñuble'),
    ('Biobío', 'Biobío'),
    ('La Araucanía', 'La Araucanía'),
    ('Los Ríos', 'Los Ríos'),
    ('Los Lagos', 'Los Lagos'),
    ('Aysén', 'Aysén'),
    ('Magallanes', 'Magallanes'),
]

class ContactForm(forms.ModelForm):
    data_sharing_consent = forms.ChoiceField(
        choices=[(True, 'Sí'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Autoriza que sus datos sean compartidos con empresas participantes de este evento"
    )

    # Menú desplegable para regiones
    region = forms.ChoiceField(
        choices=REGIONS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Región"
    )

    # Campo de checkboxes para seleccionar tracks
    track_of_interest = forms.MultipleChoiceField(
        choices=TRACKS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label="Track de su interés"
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
            'position',
            'region',
            'track_of_interest',
            'data_sharing_consent',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'placeholder': 'RUT', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Teléfono de contacto', 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'placeholder': 'Institución a la que representa', 'class': 'form-control'}),
            'position': forms.TextInput(attrs={'placeholder': 'Cargo', 'class': 'form-control'}),
        }

    def clean_track_of_interest(self):
        selected_tracks = self.cleaned_data['track_of_interest']
        
        # Validar que solo se seleccione un track por bloque horario
        for schedule, tracks in SCHEDULE_GROUPS.items():
            selected_in_group = [track for track in selected_tracks if track in tracks]
            if len(selected_in_group) > 1:
                raise forms.ValidationError(f"Solo puede seleccionar un track en el bloque horario de {schedule}.")
        
        return selected_tracks

"""
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
"""