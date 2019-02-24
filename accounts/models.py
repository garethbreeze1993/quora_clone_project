from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify # if you have space in string it will fill with dashes etc so your browser can read it

class User(AbstractUser):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	bio = models.CharField(max_length=240, blank=True)
	image = models.ImageField(blank = True, upload_to = 'avatars/')
	location = models.CharField(max_length=30, blank=True)
	slug = models.SlugField(allow_unicode=True, unique=True)
	
	REQUIRED_FIELDS = ['first_name', 'last_name','email']

	
	def display_name(self):
		return self.first_name + ' ' + self.lastname
		

	def __str__(self):
		return self.username

	def save(self,*args,**kwargs):
		self.slug = slugify(self.first_name+self.last_name) # when person types in group name with spaces this slugify will
	# change the name so it can be used in URL by browser	
		super().save(*args,**kwargs)

	
	

	

























































'''
#Now this is where the magic happens: we will now define signals so our Profile model will be automatically created/updated 
#when we create/update User instances.
from django.db.models.signals import post_save
from django.dispatch import receiver
class User(auth.models.User,auth.models.PermissionsMixin):
	
	def display_name:
		return self.first_name.title() + ' ' + self.lastname
		
	def __str__(self):
		return self.display_name()
		
		
class Profile(models.Model):
	user = models.OnetoOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=240)
	image = models.ImageField(upload_to = 'accounts/images/')
	location = models.CharField(max_length=30)
	

	
# Basically we are hooking the create_user_profile and save_user_profile methods to the User model, whenever a save event occurs. 
# This kind of signal is called post_save.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

'''
