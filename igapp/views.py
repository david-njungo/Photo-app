from django.shortcuts import render
from .models import Image
# Create your views here.

def home(request):
    images = Image.get_image
    return render(request,'home.html',{"images":images}) 