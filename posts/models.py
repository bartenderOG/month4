from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    image = models.ImageField(null=True, blank=True, upload_to="posts/", verbose_name="Изображение")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Категория",
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

# # Create your models here.
# # C-R-U-D

# # Create
# # SQL -> "INSERT INTO table_name (fields_name ...) VALUES (a, a, a);"
# # Django
# Post.objects.create()
# post = Post(title="title#1", description="description to blog")
# post.save()

# # Read
# # SQL -> "SELECT * FROM table_name WHERE title="title";"
# # Django
# post = Post.objects.filter(title="title").first()

# # Update
# # SQL -> "UPDATE table_name SET field_name=title WHERE title=title;"
# # Django
# post.title = "kasd asfas fasf"  # type: ignore
# post.save()  # type: ignore

# # Delete
# # SQL -> "DELETE FROM table_name WHERE title=title;"
# # Django
# post.delete()  # type: ignore