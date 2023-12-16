from django.urls import path
from .views import ItemAPIView, ItemIDView, CategoryAPIView, CategoryIDView, CommentAPI, CommentIDView, ItemIdUser

app_name = 'item'

urlpatterns = [
    path('items/', ItemAPIView.as_view(), name='items'),
    path('items/<str:pk>/', ItemIDView.as_view(), name="item"),
    path('user-items/<str:pk>/', ItemIdUser.as_view(), name="user_item"),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<str:pk>/', CategoryIDView.as_view(), name='category_id'),
    path('items/<str:pk>/comments/', CommentAPI.as_view(), name="added_comments"),
    path('items/<str:item_pk>/comments/<str:comment_pk>/', CommentIDView.as_view(), name="view_comment"),
]