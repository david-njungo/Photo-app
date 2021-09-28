from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30) 
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment',on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']   

class Profile(models.Model):
    prof_photo = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =30)
    
    def __str__(self):
        return self.bio
    class Meta:
        ordering = ['bio'] 

class Comments(models.Model):
    author = name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)