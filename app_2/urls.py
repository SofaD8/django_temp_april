from django.urls import path
from .views import index

app_name = 'app_2'

urlpatterns = [
    path('', index, name='index'),
]