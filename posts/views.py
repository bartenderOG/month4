from django.shortcuts import render, redirect # type: ignore
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from posts.models import Post, Category
# Create your views here.

def hello_world(request: HttpRequest):
    return HttpResponse('<h1>Hello world!</h1>')

s = Category.objects.order_by("name").all()
def my_name(request: HttpRequest):
    return HttpResponse('<h1>Bekzhan</h1>')


def post_list(request: HttpRequest):
    posts = Post.objects.order_by("-created_at").all()

    return render(request, "posts/posts.html", {"posts": posts})

def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = Post.objects.get(id=id)

    return render(request, "posts/post_detail.html", {"post": post})



def create_post(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.order_by("name").all()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category_id = request.POST.get("category")
        new_category_name = request.POST.get("new_category", "").strip()

        category = None
        if category_id:
            category = Category.objects.filter(id=category_id).first()
        if not category and new_category_name:
            category, _ = Category.objects.get_or_create(name=new_category_name)

        post = Post.objects.create(title=title, description=description, image=image, category=category)
        return redirect('post_detail', id=post.id) #type: ignore

    return render(request, "posts/create_post.html", {"categories": categories})