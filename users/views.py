from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from users.forms import UserForm, LoginForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect, get_object_or_404
from django import forms


def register(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    if request.method.lower() == "post": # type: ignore
        form = UserForm(request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data["password"])
            form.instance.save()
            login(request, form.instance)
            return redirect("post_list")
        

    return render(request, "users/registr.html", {"form": form})

def login_view(request: HttpRequest) -> HttpResponse:
    form =LoginForm(request.POST)

    if request.method.lower() == "post": # type: ignore
        form = LoginForm(request.POST)

        if form.is_valid():
            user = get_object_or_404(User, username=form.cleaned_data["username"])

            if user.check_password(form.cleaned_data["password"]):
                login(request, user)
                return redirect("post_list")
            form.add_error("password", forms.ValidationError("Invalid password"))
            
    return render(request, "users/login.html", context={"form": form})



def logout_view(request: HttpRequest):
    if request.method.lower() == "post":  # type: ignore
        logout(request)

        return redirect("post_list")



