from django.urls import path
from .views import ItemAPIView, ItemIDView, CategoryAPIView, CategoryIDView

app_name = 'item'

urlpatterns = [
    path('items/', ItemAPIView.as_view(), name='items'),
    path('items/<str:pk>/', ItemIDView.as_view(), name="item"),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<str:pk>/', CategoryIDView.as_view(), name='category_id'),
]