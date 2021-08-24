from django.shortcuts import render,redirect
from myPlog.models import Post
from .models import Profile
from django.contrib  import  messages 
from .forms import UserRegisterForm
# Create your views here.
from django.contrib.auth.decorators import login_required


def user_profile(request):
    ob1=Profile.objects.all()
    
    context={"ob1":ob1}
    
    return render(request, "base/profile.html", context)

@login_required  
def about_page(request):
    context={}
    template_name="base/about.html"
    return render(request, template_name, context)


 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to navigate the website')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, "base/register.html", {'form': form})