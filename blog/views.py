from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from account.models import User
from .models import Book , Category


class BookListView(ListView):
    queryset = Book.objects.filter(status=True)
    template_name = 'blogs/home.html'
    context_object_name = 'book'
    paginate_by = 6


    
class DetailBookView(DetailView):
    template_name = 'blogs/detail.html'
    context_object_name = 'details'

    def get_object(self):
        get_id = self.kwargs.get('id')
        return get_object_or_404(Book.objects.filter(status=True) ,id=get_id)
    


class CategoryListView(ListView):
    paginate_by = 5
    template_name = 'blogs/category_list.html'

    def get_queryset(self):
        global category
        get_id = self.kwargs.get('id')
        category = get_object_or_404(Category.objects.filter(status=True) ,id=get_id)
        return category.cat_books.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category
        return context
    


class AuthorListBook(ListView):
    paginate_by = 5
    template_name = 'blogs/author_list.html'

    def get_queryset(self):
        global author
        get_id = self.kwargs.get('id')
        author = get_object_or_404(User.objects.filter(), id=get_id)
        return author.writer.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = author
        return context