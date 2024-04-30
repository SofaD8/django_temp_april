"""
URL configuration for django_temp_april project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app_1 import views as views_1
from app_2 import views as views_2
from articles import views as articles

urlpatterns = [
    path('admin/', admin.site.urls),

    path('articles/<int:year>/', articles.articles_by_year, name='articles_by_year'),
    path('articles/<int:year>/<int:month>', articles.articles_by_year_month, name='articles_by_year_month'),
    path('articles/2023/', articles.article_2023, name='article_2023'),
    path('app_1/', views_1.app_1, name='app_1'),
    path('app_2/', views_2.app_2, name='app_2'),
    path('', views_1.index, name='index'),
]
