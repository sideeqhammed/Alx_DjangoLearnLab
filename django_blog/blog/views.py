from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def register(request):
  if (request.method == 'POST'):
    form = CustomUserCreationForm(request.post)
    if (form.is_valid):
      form.save()
      return redirect('login')
  else:
    form = CustomUserCreationForm()
  return render(request, 'blog/register.html', {'form':form})

@login_required
def profileView(request):
  return render(request, 'blog/profile.html')

class BlogListView(ListView):
  model = Post
  template_name = 'blog/post_list.html'
  context_object_name = 'posts'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
  context_object_name = 'post'

class BlogCreateView(CreateView, LoginRequiredMixin):
  model = Post
  template_name = 'blog/post_create.html'
  fields = ['title', 'content', 'author']
  success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
  model = Post
  template_name = 'blog/post_create.html'
  fields = ['title', 'content', 'author']
  success_url = reverse_lazy('blog_list')

class BlogDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
  model = Post
  template_name = 'blog/post_delete.html'
  success_url = reverse_lazy('blog_list')


