from django.shortcuts import get_object_or_404, render
from .forms import NewCommentForm
from .models import Tweet, Comment
from accounts.models import Follow
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import sys
# Create your views here.

class UserPostListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'feed/user_detail.html'
    context_object_name = 'posts'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        visible_user = self.visible_user()
        logged_user = self.request.user
        print(logged_user.username == '', file=sys.stderr)

        if logged_user.username == '' or logged_user is None:
            can_follow = False
        else:
            can_follow = (Follow.objects.filter(user=logged_user,
                                                follow_user=visible_user).count() == 0)
        data = super().get_context_data(**kwargs)

        tweet_user = Tweet.objects.all()
        data['user_tweet'] = tweet_user
        data['user_profile'] = visible_user
        data['can_follow'] = can_follow
        return data

    def get_queryset(self):
        user = self.visible_user()
        return Tweet.objects.filter(author=user).order_by('-datetime')

    def post(self, request, *args, **kwargs):
        if request.user.id is not None:
            follows_between = Follow.objects.filter(user=request.user,
                                                    follow_user=self.visible_user())

            if 'follow' in request.POST:
                    new_relation = Follow(user=request.user, follow_user=self.visible_user())
                    if follows_between.count() == 0:
                        new_relation.save()
            elif 'unfollow' in request.POST:
                    if follows_between.count() > 0:
                        follows_between.delete()

        return self.get(self, request, *args, **kwargs)


class TweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'feed/home.html'
    ordering = ['-datetime']
    
class TweetDetailView(LoginRequiredMixin, DetailView):
    model = Tweet
    template_name = 'feed/post_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(tweet_connected=self.get_object()).order_by('-date_posted')
        tweet_connected = Tweet.objects.all()
        data['comments'] = comments_connected
        data['posts'] = tweet_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(text=request.POST.get('text'),
                              author=self.request.user,
                              tweet_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    
    fields = ['text']
    success_url = '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin,UpdateView):
    model = Tweet
    
    fields = ['text']
    success_url = '/'

    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == Tweet.author):
            return True
        return False

class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model = Tweet
    success_url = '/'

    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == Tweet.author):
            return True
        return False


class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if(self.request.user == Comment.author):
            return True
        return False


class FollowersListView(ListView):
    model = Follow
    template_name = 'feed/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(follow_user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'followers'
        return data

class FollowsListView(ListView):
    model = Follow
    template_name = 'feed/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'follows'
        return data