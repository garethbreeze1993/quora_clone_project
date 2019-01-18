from django.db import models
from django.utils.text import slugify # if you have space in string it will fill with dashes etc so your browser can read it

class Group(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()
	slug = models.SlugField(allow_unicode=True, unique=True)
	image = models.ImageField(upload_to = 'groups/', blank=True)
	
	
	def __str__(self):
		return self.name
	
	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super().save(*args,**kwargs)

	
	