from django.test import TestCase

# Create your tests here.

from django.urls import reverse

from posts.models import Category, Post


class CategoryAndPostCreationTests(TestCase):
    def test_create_category_and_post_linked_to_it(self):
        category_response = self.client.post(reverse("create_category"), {"name": "Технологии"})
        self.assertEqual(category_response.status_code, 302)
        self.assertTrue(Category.objects.filter(name="Технологии").exists())

        category = Category.objects.get(name="Технологии")
        post_response = self.client.post(
            reverse("create_post"),
            {
                "title": "Новый пост",
                "description": "Описание поста",
                "category": str(category.id),
            },
        )

        self.assertEqual(post_response.status_code, 302)
        post = Post.objects.get(title="Новый пост")
        self.assertEqual(post.category, category)

    def test_create_post_with_new_category_from_form(self):
        response = self.client.post(
            reverse("create_post"),
            {
                "title": "Пост с новой категорией",
                "description": "Описание",
                "new_category": "Блог",
            },
        )

        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(title="Пост с новой категорией")
        self.assertEqual(post.category.name, "Блог")

    def test_filter_posts_by_category(self):
        category = Category.objects.create(name="Python")
        other_category = Category.objects.create(name="Django")
        Post.objects.create(title="Python post", description="Описание", category=category)
        Post.objects.create(title="Django post", description="Описание", category=other_category)

        response = self.client.get(reverse("post_list"), {"category": category.id})

        self.assertContains(response, "Python post")
        self.assertNotContains(response, "Django post")