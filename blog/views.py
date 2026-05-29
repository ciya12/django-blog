from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.core.cache import cache

# Create your views here.

def redis_test(request):
    try:
        cache.set('test_key', 'Redis 连接成功！Django 和 Redis 已经成功牵手！', 60)
        value = cache.get('test_key')
        return HttpResponse(f"<h2>✅ {value}</h2><p>测试通过，Redis 工作正常。</p>")
    except Exception as e:
        return HttpResponse(f"<h2>❌ Redis 连接失败</h2><p>错误信息：{e}</p>")

def article_list(request):
    # 尝试从缓存中获取数据，缓存 key 为 'article_list_data'
    articles_data = cache.get('article_list_data')
    if not articles_data:
        print("缓存未命中，查询数据库...")
        articles_list = Article.objects.all().order_by('-created_at')
        paginator = Paginator(articles_list, 5)
        page_number = request.GET.get('page')
        articles = paginator.get_page(page_number)
        latest_articles = Article.objects.all().order_by('-created_at')[:5]
        categories = Category.objects.all()
        articles_data = {
            'articles': articles,
            'latest_articles': latest_articles,
            'categories': categories,
        }
        # 将数据存入缓存，过期时间 60 秒
        cache.set('article_list_data', articles_data, 60)
    else:
        print("缓存命中，直接返回...")
        articles = articles_data['articles']
        latest_articles = articles_data['latest_articles']
        categories = articles_data['categories']

    return render(request, 'blog/article_list.html', {
        'articles': articles,
        'latest_articles': latest_articles,
        'categories': categories,
    })

def article_list(request):
    articles_list = Article.objects.all().order_by('-created_at')
    paginator = Paginator(articles_list , 5)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    latest_articles = Article.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()
    return render(request,'blog/article_list.html',{'articles':articles,'latest_articles': latest_articles,
        'categories': categories})

def article_detail(request, id):
    articles_list = Article.objects.all().order_by('-created_at')
    paginator = Paginator(articles_list, 5)  # 每页5篇
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    latest_articles = Article.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()

    return render(request, 'blog/article_detail.html', {
        'article': articles,
        'latest_articles': latest_articles,
        'categories': categories
    })

def category_detail(request, category_id):
    category = get_object_or_404(Category , id=category_id)
    articles = Article.objects.filter(category=category).order_by('-created_at')
    latest_articles = Article.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.all()
    return render(request,'blog/category_detail.html',{
        'category' : category,
        'articles' : articles,
        'latest_articles': latest_articles,
        'categories': categories
    })