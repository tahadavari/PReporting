from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from account.forms.login_form import LoginForm


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
                context = {'form': form}
                return render(request, 'login.html', context)
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
