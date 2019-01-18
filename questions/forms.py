from django import forms
from questions.models import Question,Answer

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('group','name','body',)
	
class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('body','question', 'author')
		widgets = {'question': forms.HiddenInput(), 'author': forms.HiddenInput()}
				        

