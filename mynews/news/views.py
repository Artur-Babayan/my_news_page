from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NewsArticle, Category
from .forms import CategoryForm


def home(request):
    categories = Category.objects.all()
    article_list = NewsArticle.objects.all().order_by('-created_date')
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator


def category(request, pk):
    categories = Category.objects.all()
    selected_category = get_object_or_404(Category, pk=pk)
    articles = selected_category.articles.all().order_by('-created_date')[:10]
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'news/category.html', {'categories': categories, 'selected_category': selected_category, 'articles': articles, 'form': form})


def news_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    return render(request, 'news/news_detail.html', {'article': article})
