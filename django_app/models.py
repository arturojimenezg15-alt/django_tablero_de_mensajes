from django.db import models

# Create your models here.

class django_app(models.Model):
    text = models.TextField() 

def __str__(self):
    return self.text[:50]  # Return the first 50 characters of the post text