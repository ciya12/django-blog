from django.urls import path
from . import  views

urlpatterns = [
    path('',views.article_list,name='article_list'),
    path('<int:id>/',views.article_detail,name = 'article_detail'),
    path('category/<int:category_id>/',views.category_detail, name = 'category_detail'),
    path('redis-test/', views.redis_test, name='redis_test'),
]