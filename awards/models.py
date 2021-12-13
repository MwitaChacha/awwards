from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.db.models import Q
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.user 
    
class Project(models.Model):   
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='project_user')
    title = models.CharField(max_length=100)
    image = CloudinaryField('image') 
    description = HTMLField()
    link = models.CharField(max_length=250)
    posted_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, default="")
  
    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(Q(user__username=search_term) | Q(title__icontains=search_term))
        return projects  
      
    
    def __str__(self):
        return self.title        
    