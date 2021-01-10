from django.db import models

# Create your models here.
class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	thum=models.FileField(upload_to='books/thum/', default=None)
	pdf=models.FileField(upload_to='books/pdfs/', default=None)


	def __str__(self):
		return str(self.pdf)

	def pdf_path(self):
		return self.pdf

'''	
class SingleVideo(models.Model):
	video_file = models.FileField(upload_to='video_store/videos/')
	
	def __str__(self):
		return str(self.video_file)'''
				
class ListModel(models.Model):
	videos = models.FileField(upload_to='videos/pdfs/', default=None)
	
	def __str__(self):
		return str(self.videos)

	def __len__(self):
		return len(self.videos)

class UploadedVideos(models.Model):
	video_name = models.CharField(max_length=100)
	video_path = models.CharField(max_length=500)
	video_thum = models.FileField(upload_to='output/thumb/', default=None)
	def __str__(self):
		return str(self.video_name)