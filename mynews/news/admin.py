from django.contrib import admin
from .models import NewsArticle, Category


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_category', 'created_date')
    search_fields = ('title', 'content')
    list_filter = ('created_date', 'categories')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(Category, CategoryAdmin)
