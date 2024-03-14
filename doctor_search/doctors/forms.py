from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'email', 'phone_number', 'address', 'website',
                  'description']
