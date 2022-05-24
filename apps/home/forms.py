from tkinter import Widget
from django import forms
from .models import patient

class patientForm(forms.ModelForm):
	class Meta:
		model = patient
		fields = ['Firstname','Lastname', 'Age', 'Date']