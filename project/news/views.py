from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .forms import PostForm
from .filters import ProductFilter
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_queryset(self):
            queryset = super().get_queryset()
            self.filterset = ProductFilter(self.request.GET, queryset)
            return self.filterset.qs


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filterset'] = self.filterset
            return context


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — news_1.html
    template_name = 'news_1.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

class Search_List(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_queryset(self):
            queryset = super().get_queryset()
            self.filterset = ProductFilter(self.request.GET, queryset)
            return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name='news_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context

    def form_valid(self,form):
        post=form.save(commit=False)
        post.type='article'
        post.autor = self.request.user.author
        post.save()
        return super().form_valid(form)

class Post_Update(PermissionRequiredMixin,UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self,form):
        post=form.save(commit=False)
        post.type='article'
        post.autor = self.request.user.author
        post.save()
        return super().form_valid(form)
class Post_Delete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('product_list')
    