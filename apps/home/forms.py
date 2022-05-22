from django import forms
import datetime
from .models import patient

class patientForm(forms.ModelForm):
	class Meta:
		model = patient
		fields = ['Firstname','Lastname', 'Age', 'Date']