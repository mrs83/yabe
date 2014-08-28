from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import Post
from .forms import PostForm


class AuthorRequiredMixin(object):
    author_field = 'author'

    def get_object(self, *args, **kwargs):
        obj = super(AuthorRequiredMixin, self).get_object(*args, **kwargs)
        if self.request.user.is_superuser: # superusers can edit everything
            return obj
        if not getattr(obj, self.author_field) == self.request.user:
            raise Http404
        return obj


class PostAuthorMixin(object):
    def form_valid(self, form):
         user = self.request.user
         form.instance.author = user
         return super(PostAuthorMixin, self).form_valid(form)


class PostCreate(AuthorRequiredMixin, PostAuthorMixin, StaffuserRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blogs/post_create.html'
    form_class = PostForm


class PostUpdate(AuthorRequiredMixin, PostAuthorMixin, StaffuserRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blogs/post_update.html'
    form_class = PostForm


class PostDelete(AuthorRequiredMixin, StaffuserRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostList(ListView):
    model = Post
    paginate_by = 3
