from django.urls import path
from .views import index, load_subcategories, load_categories

urlpatterns = [
    path('', index, name='index'),
    path('load_categories/', load_categories, name='load_categories'),
    path('load_subcategories/', load_subcategories, name='load_subcategories'),
]