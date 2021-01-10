from .models import PostImage,Post
from django import forms

class PostImageForm(forms.ModelForm):
	class Meta:
		model = PostImage
		fields = ('videos',)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','desp','videos',)