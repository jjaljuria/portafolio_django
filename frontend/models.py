from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.fields.CharField(max_length=100)
	description = models.fields.TextField()
	image = models.fields.files.ImageField(upload_to="")
	url = models.fields.URLField(blank=True)