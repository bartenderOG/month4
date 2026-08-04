from django.shortcuts import render, redirect # type: ignore
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from posts.models import Post
# Create your views here.

def hello_world(request: HttpRequest):
    return HttpResponse('<h1>Hello world!</h1>')


def my_name(request: HttpRequest):
    return HttpResponse('<h1>Bekzhan</h1>')


def post_list(request: HttpRequest):
    posts = Post.objects.order_by("-created_at").all()

    return render(request, "posts/posts.html", {"posts": posts})

def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = Post.objects.get(id=id)

    return render(request, "posts/post_detail.html", {"post": post})


def create_post(request: HttpRequest) -> HttpResponse:
    
    if request.method.lower() == "post": #type: ignore
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        post = Post.objects.create(title=title, description=description, image=image)
        return redirect("post_list")
    return render(request, "posts/create_post.html")
