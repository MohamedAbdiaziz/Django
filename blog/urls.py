
from unicodedata import name
from django.urls import path
from .views import HomeVeiw, CategoryViewList, CategoryUpdateView, CategoryDeleteView,CategoryCreateView

urlpatterns = [
    path('', HomeVeiw, name='home'),
    path('category/', CategoryViewList, name="category"),
    path('category/<int:pk>/update/', CategoryUpdateView, name="category-update"),
    path('category/<int:pk>/delete/', CategoryDeleteView, name="category-delete"),
    path('category/add/', CategoryCreateView, name="category-add"),

]
