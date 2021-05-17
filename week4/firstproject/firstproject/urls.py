"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from firstapp import views as first #view.firstapp.~~ 이렇게 들어갈 거를 first.~~ 이렇게 편하게
from wordcount import views as wc
from assignmentBlog import views as blog

#'' -> 최초의 페이지
#두번째 인자 -> 연결할 view
#세번째 인자 -> 편의를 위해 이렇게 부르겠다~

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', first.welcome, name="welcome"),
    path('hello/', first.hello, name="hello"),

    path('wc/', wc.home, name="wc"),
    path('wc/result/', wc.result, name="result"),

    path('blog/', blog.home, name="home"),
    path('blog/<str:id>', blog.detail, name="detail")


]
