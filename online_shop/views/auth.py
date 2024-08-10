from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from online_shop.forms import LoginForm
from django.contrib import messages


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                messages.error(request,
                               'Wrong password or username')
                pass
    else:
        form = LoginForm()
    return render(request, 'online_shop/auth/login.html', {'form': form})


def register_page(request):
    return render(request, 'online_shop/auth/register.html')


def logout_page(request):
    logout(request)
    return redirect('product_list')
