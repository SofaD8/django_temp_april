from django.urls import path
from .views import article_2023, articles_by_year, articles_by_year_month


urlpatterns = [
    path('2023/', article_2023, name='article_2023'),
    path('<int:year>/', articles_by_year, name='articles_by_year'),
    path('<int:year>/<int:month>/', articles_by_year_month, name='articles_by_month'),
]