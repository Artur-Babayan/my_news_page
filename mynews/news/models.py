from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    is_main_category = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='articles')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.categories.filter(is_main_category=True).exists():
            self.categories.first().is_main_category = True
        super().save(*args, **kwargs)

