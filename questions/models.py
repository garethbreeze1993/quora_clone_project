from django.db import models
from django.conf import settings
from django.utils.text import slugify # if you have space in string it will fill with dashes etc so your browser can read it
from django.urls import reverse
from groups.models import Group
from accounts.models import User

class Question(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'questions', on_delete=models.PROTECT)
	group = models.ForeignKey(Group, related_name = 'questions', on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	body = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now=True) 
	solved = models.BooleanField(default=False)
	slug = models.SlugField(allow_unicode=True, unique=True)
	
	def __str__(self):
		return self.name
		
	def question_solved(self):
		self.solved = True
		self.save()	
		
	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super().save(*args,**kwargs)	
		
	def get_absolute_url(self):
		return reverse('questions:question_single',kwargs={'slug':self.slug})
		
	class Meta:
		ordering = ['-created_date']		


class Answer(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'answers', on_delete=models.PROTECT)
	question = models.ForeignKey('questions.Question', related_name = 'answers', on_delete = models.CASCADE)
	body = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	created_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body
		
	def get_absolute_url(self):
		return reverse('question:question_detail', kwargs = {'slug':self.question.slug})
		
	class Meta:
		ordering = ['-likes']	
	
	
	