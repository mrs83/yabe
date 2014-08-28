from django.shortcuts import render
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import Post
from .forms import PostForm


class PostCreate(StaffuserRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blogs/post_create.html'
    form_class = PostForm


class PostUpdate(StaffuserRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('articolo_list')
    template_name = 'blogs/post_update.html'
    form_class = PostForm


class PostDelete(StaffuserRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('articolo_list')


class PostList(ListView):
    model = Post
    paginate_by = 3
