from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.ImageField(upload_to = 'images/')
    image = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30) 

