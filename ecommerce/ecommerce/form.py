from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(
			attrs={"class":"form-control",
			"placeholder":"Fullname",
			"id":"form_full_name"}))
		
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={"class":"form-control",
			"placeholder":"email",
			"id":"email_feild"}))

	content = forms.CharField(
		widget=forms.Textarea(
			attrs={"class":"form-control",
			"placeholder":"content",
			"id":"content_field"}))


	def clean_email(self):
		email= self.cleaned_data.get("email")

		if not "gmail.com" in email :
			raise forms.ValidationError("Email has gamil.com")
		return email

	def clean_fullname(self):
		fullname = self.cleaned_data.get("fullname")

		if len(fullname) < 5 :
			raise forms.ValidationError("name should be minmum 5 Charcter")
		return fullname

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username = forms.CharField()
	email    = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)	
	password2 = forms.CharField(label = 'confirm password' , widget=forms.PasswordInput)

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("password must be match") 
		return data

	def clean_username(self):
		username =self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username already exist")
		return username	

	def clean_email(self):
		email =self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email already exist")
		return email		