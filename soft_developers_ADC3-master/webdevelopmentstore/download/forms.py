from django import forms
#from .models import software
from software.models import Software

class OForm(forms.ModelForm):
	class Meta:
		model = Software
		fields = ('title', 'name','stw')