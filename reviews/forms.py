from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,label='Text')
	email = forms.EmailField(max_length=70, required=True,label='Email')
	title = forms.CharField(max_length=100, required=True, label='Text')

	review = forms.CharField(max_length=1000, required=True,label='Text')

	address = forms.CharField(max_length=70, label='Text')

	image = forms.ImageField(label='Image')

	date = forms.DateTimeField(label='Date')



	class Meta:
		model = Review
		fields = ('full_name', 'email', 'title', 'review', 'address', 'date', 'image')