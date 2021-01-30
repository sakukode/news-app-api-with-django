from django.urls import path

# import semua class View untuk modul Category
from .views import CategoryListView, CategoryDetailView


urlpatterns = [
    # membuat route untuk API endpoint Category
    path('category/', CategoryListView.as_view(), name='api-category-list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='api-category-detail'),
]