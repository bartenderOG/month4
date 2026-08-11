"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from posts.views import create_post, hello_world, post_detail, post_list
from users.views import register, login_view, logout_view
from . import views
from users.views import register, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello_world),
    path("posts/", views.post_list, name="post_list"),
    path("users/register/", register, name="register"),
    path("posts/<int:id>/", views.post_detail, name="post_detail"),
    path("posts/create/", views.create_post, name="post_create"),
    path("users/login/", login_view, name="login"),
    path("users/logout/", logout_view, name="logout"), #type: ignore
    path("posts/<int:id>/update/", views.update_post, name="post_update"),
    path("posts/<int:id>/delete/", views.delete_post, name="post_delete"),
    path("categories/create/", views.create_category, name="category_create"),
    path("", include("posts.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)