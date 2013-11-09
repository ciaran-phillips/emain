from django import forms
from datetime import datetime

from django.contrib.auth.models import User
from django.utils.timezone import utc

from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['lat', 'lon', 'when']

    when = forms.DateTimeField(required=False)
    userid = forms.IntegerField(required=False)

    def clean_when(self):
        if self.cleaned_data['when'] is None:
            self.cleaned_data['when'] = datetime.utcnow().replace(tzinfo=utc)
        return self.cleaned_data['when']


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
	
	
