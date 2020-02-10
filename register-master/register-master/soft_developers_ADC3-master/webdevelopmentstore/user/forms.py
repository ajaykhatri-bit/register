from django import forms
from software.models import User

#from django.contrib.auth.models import User



class OurForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('user_fname','user_lname', 'email', 'password',)


	def save(self, commit=True):
		user = super(OurForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

		return user
					



