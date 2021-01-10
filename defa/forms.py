from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title','author','thum','pdf')

'''
class VideoForm(forms.ModelForm):
	class Meta:
		model = SingleVideo
		fields = ('video_file',)

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))	'''	