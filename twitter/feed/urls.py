from django.urls import path
from . import views
from .views import (TweetListView, 
TweetCreateView, TweetUpdateView, TweetDeleteView, FollowersListView, FollowsListView, TweetDetailView, CommentDeleteView, UserPostListView)

urlpatterns = [
    path('', TweetListView.as_view(), name = 'home'),
    path('create/', TweetCreateView.as_view(), name = 'tweetcreate'),
    path('tweet/<int:pk>', TweetDetailView.as_view(), name = 'tweetdetail'),
    path('tweet/<int:pk>/update', TweetUpdateView.as_view(), name = 'tweetupdate'),
    path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name = 'tweetdelete'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name = 'commentdelete'),
    path('user/<str:username>', UserPostListView.as_view(), name='userdetail'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follow'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-follower'),
]