from django import forms
from .models import GetCity

class theCity(forms.ModelForm):
	class Meta:
		model =GetCity
		fields=['city']
	def __init__(self,*args,**kwargs):
		super(theCity, self).__init__(*args, **kwargs)
		self.fields['city'].label = ""