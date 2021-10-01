from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30) 

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name'] 

    def save_image(self):
        self.save()
    @classmethod
    def get_image(cls):
        images = cls.objects.all()
        return images  
    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(image_name__icontains=search_term)
        return images

    

class Profile(models.Model):
    prof_photo = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =30)
    image = models.ForeignKey('Image',on_delete=models.CASCADE) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.save()

    

class Comment(models.Model):
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    image = models.ForeignKey('Image',on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    class Meta:
        ordering = ['created_on']
    

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.author

class Likes(models.Model):
    image = models.ForeignKey(Picture, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_likes(self):
        self.save()

    def delete_like(self):
        self.delete()

    def count_likes(self):
        likes = self.likes.count()
        return likes