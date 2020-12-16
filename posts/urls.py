from django.urls import path, include
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
