from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import PostForm, CategoryForm
from posts.models import Post


def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello world!</h1>")


def post_list(request: HttpRequest):
    posts = Post.objects.select_related("category").order_by("-created_at")
    return render(request, "posts/posts.html", {"posts": posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})


def create_post(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "posts/create_post.html", {"form": form, "title": "Новый пост"})


def create_category(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = CategoryForm()

    return render(request, "posts/create_category.html", {"form": form, "title": "Новая категория"})


def update_post(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "posts/create_post.html", {"form": form, "title": "Редактирование поста"})


def delete_post(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "posts/delete_post.html", {"post": post})