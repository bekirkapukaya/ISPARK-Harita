from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username,password=password)

            if user is None:
                messages.warning(request,"Kullanıcı adı veya parola hatalı...")
                return render(request,"login.html",context)

            messages.success(request,"Başarıyla giriş yaptınız...")
            login(request, user)
            return redirect("/map")

        messages.warning(request,"Giriş sırasında hata ile karşılaşıldı...")
        return render(request, "login.html", context)
        

        return render(request, "login.html", context)
    else:
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "login.html", context)


def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username, password=password)
            newUser.set_password(password)

            newUser.save()
            login(request, newUser)
            messages.success(request,"Başarıyla kayıt oldunuz...")
            return redirect("/map")
        messages.warning(request,"Kayıt sırasında hata ile karşılaşıldı...")

        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context)

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context)


def logout(request):
    pass
