from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    images = Image.get_image
    return render(request,'home.html',{"images":images}) 

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
