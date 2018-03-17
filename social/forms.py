from django.contrib.auth.models import User
from django import forms
from .models import Question,post_question,answer
from django.forms import Textarea,ModelForm 


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	def __init__(self, *args, **kwargs):          
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = u'First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = u'Last Name'
		self.fields['email'].widget.attrs['placeholder'] = u'E-mail Id'
		self.fields['username'].widget.attrs['placeholder'] = u'Username'
		self.fields['password'].widget.attrs['placeholder'] = u'Password'
		self.fields['first_name'].widget.attrs['style'] = "width:300px"
		self.fields['last_name'].widget.attrs['style'] = "width:300px"
		self.fields['email'].widget.attrs['style'] = "width:300px"
		self.fields['username'].widget.attrs['style'] = "width:300px"
		self.fields['password'].widget.attrs['style'] = "width:300px"
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password')



class question_form(forms.ModelForm):
	question = forms.CharField(
        max_length=10000,
        widget=forms.Textarea(),
        help_text='Write here your question!'
    )
	def __init__(self, *args, **kwargs):          
		super(question_form, self).__init__(*args, **kwargs)
		self.fields['question'].widget.attrs['placeholder'] = u'ENTER YOUR QUESTION'
	class Meta:
		model=Question
		fields=('question','topic','user_name')



class discuss_form(forms.ModelForm):
	ask = forms.CharField(
	max_length=10000,
	widget=forms.Textarea(),
	help_text='Write here your question!'
	)
	def __init__(self, *args, **kwargs):          
		super(discuss_form, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder'] = u'Write your name'
		self.fields['ask'].widget.attrs['placeholder'] = u'Write your question'
	class Meta:
		model=post_question
		fields=('name','ask')

class comment_form(forms.ModelForm):
	def __init__(self, *args, **kwargs):          
		super(comment_form, self).__init__(*args, **kwargs)
		self.fields['comment'].widget.attrs['placeholder'] = u'Write your comments'
	class Meta:
		model = answer
		fields = ['user_name', 'comment']
		widgets = {
    	'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
		}

