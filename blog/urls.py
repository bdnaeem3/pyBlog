from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPost.as_view(), name='blog-home'),
    path('post/<int:pk>', views.SinglePost.as_view(), name='single-post'),
    path('post/create', views.CreatePost.as_view(), name='create-post'),
    path('post/<int:pk>/update', views.UpdatePost.as_view(), name='update-post'),
    path('post/<int:pk>/delete', views.DeletePost.as_view(), name='delete-post'),
    path('user/<str:username>', views.UserPost.as_view(), name='user-post'),
    path('about', views.about, name='blog-about'),
]
