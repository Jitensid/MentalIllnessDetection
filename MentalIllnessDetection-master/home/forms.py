from django import forms
from django.contrib.auth.models import User
from .models import Feedback, cbt 


class MessageForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields= ["message"]
			

class cbtForm(forms.ModelForm):
	class Meta:
		model = cbt
		fields = ["age","name","country","gender"]#create forms over here