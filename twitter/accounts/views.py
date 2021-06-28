from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm
from feed.models import Tweet
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created.')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


class UserTweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'accounts/profile.html'
    ordering = ['-datetime']


def profileupdate(request):
    if(request.method == 'POST'):
        pform = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if pform.is_valid():
            pform.save()
            return redirect('profile')

    else:
        pform = ProfileUpdateForm(instance = request.user.profile)

    return render(request, 'accounts/profileupdate.html', {'form': pform})
