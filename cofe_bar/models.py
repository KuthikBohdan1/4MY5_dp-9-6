from django.db import models
from django.contrib.auth.models import AbstractUser

class Review(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\nPublished: {self.pub_date}"
    


class Register(models.Model):
    name = models.CharField(max_length=100)
    password = models.TextField()
    return_password = models.TextField()
    user_birth_date = models.DateField()



class Standart(models.Model):
    pass