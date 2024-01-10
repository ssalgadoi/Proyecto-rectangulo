from django.db import models

# Create your models here.

class Contacto(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    
    def __str__(self):
        return self.name