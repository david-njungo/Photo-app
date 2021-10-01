from django.test import TestCase
from .models import Image,Profile,Comment
# Create your tests here.

class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comm = Comment(author = 'James', body ='Great image')