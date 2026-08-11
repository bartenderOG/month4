from django.shortcuts import get_object_or_404, redirect, render
from posts.forms import PostForm, CategoryForm
from posts.models import Post


def post_list(request):
    posts = Post.objects.select_related("category").order_by("-created_at")
    return render(request, "blog/posts.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/post_detail.html", {"post": post})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form, "title": "Новый пост"})



def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/create_post.html", {"form": form, "title": "Редактирование поста"})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "blog/delete_post.html", {"post": post})


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = CategoryForm()
    return render(request, "blog/create_category.html", {"form": form, "title": "Новая категория"})