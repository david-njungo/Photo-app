from django.test import TestCase
from .models import Image,Profile,Comment
# Create your tests here.

class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comm = Comment(author = 'James', body ='Great image')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comm,Comment))

         # Testing Save Method
    def test_save_method(self):
        self.comm.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def tearDown(self):
        Comment.objects.all().delete() 