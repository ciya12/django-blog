from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'personal/home.html')

def about(request):
    return HttpResponse("""
        <h1>关于我</h1>
        <p>技能：Python、Django、机器学习</p>
        <a href='/'>返回首页</a>
    """)

def project(request):
    return HttpResponse(
        """
        <h1>我的项目</h1>
        <ul>
            <li>门禁识别系统</li>
            <li>ROS机器人</li>
            <li>个人博客</li>
        </ul>
        <a href='/'>返回首页</a>
        """
    )

def contact(request):
    return HttpResponse(
        """
        <h1>联系我</h1>
        <p>邮箱：1106646901@qq.com</p>
        <p>GitHub：github.com/xxx</p>
        <a href='/'>返回首页</a>
        """
    )

def projects(request):
    return render(request, 'personal/projects.html')