from django.test import TestCase
from .models import Image,Profile,Comment
# Create your tests here.

class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comm = Comment(author = 'James', body ='Great image')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comm,Image))