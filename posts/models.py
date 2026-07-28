from django.db import models

# Create your models here.




class Post(models.Model):
    
    title = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to="posts/")








# #C-R-U-D
# # --CREATE--
# # SQL -> "INSERT INTO table_name (fields_name ...) VALUES (a, a, a);"
# # Django
# Post.objects.create()
# post = Post(title="title#1", description="description to blog")
# post.save()


# # --READ--
# # SQL -> "SELECT * FROM table_name WHERE title="title";"
# # DJango
# post = Post.objects.filter(title="title").first()

# # --UPDATE--
# # SQL -> "UPDATE table_name SET field_name=title WHERE title=title;"
# # Django
# post.title = "sal djaspd akdmak" # type: ignore
# post.save() # type: ignore

# # --DELETE--
# # SQL -> "DELETE FROM table_name WHERE title=title;"
# # Django
# post.delete() # type: ignore
