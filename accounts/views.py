from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    pass


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Nazwa użytkownika zajęta')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Ten e-mail jest już użyty')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name)
                user.save()
                messages.info(request,'Konto utworzone, zaloguj się')
                return redirect('/login/')
        else:
            messages.info(request, 'Hasła nie pasują do siebie')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')
