from django.shortcuts import render
from .forms import UserForm

def home(request):
    return render(request, "users/home.html")

def user_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return render(request, 'users/result.html', {'name': name, 'age': age})
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})
from django.shortcuts import render

# Create your views here.
