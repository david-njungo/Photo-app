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

@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)          
        return redirect('myprofile')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/') 
def comment(request,image_id):
        current_user=request.user
        image =Image.objects.get(id=image_id)
        profile = User.objects.get(username=current_user.username)
        comments = Comment.objects.all()
        
        if request.method == 'POST':
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.image = image
                        comment.user = request.user
                        comment.save()
            
                       
                return redirect('home')
        else:
                form = CommentForm()
        return render(request, 'comment.html',locals())