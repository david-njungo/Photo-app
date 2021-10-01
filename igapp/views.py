from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    images = Image.get_image
    return render(request,'home.html',{"images":images}) 

@login_required(login_url='/accounts/login/')