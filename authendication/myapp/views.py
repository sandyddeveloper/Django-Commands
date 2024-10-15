from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(home)
        
    else:
        form = SignupForm()
    return render(request, "signup.html" ,{'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None :
            login(request, user) 
            return redirect(home)
    return render(request , 'login.html')


def home(request):
    return render(request, "index.html")
        