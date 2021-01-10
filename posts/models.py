from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	desp = models.CharField(max_length=100)
	videos = models.FileField(blank=True)

	def __str__(self):
		return self.title
class PostImage(models.Model):
	post = models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
	videos = models.FileField(upload_to='videos/sample')

	def __str__(self):
		return self.post.title