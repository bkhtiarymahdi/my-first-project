from django.db.models.query import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Book
from .models import User
from .mixins import FieldMixin, NotationMixin, WeiterMixin
from .froms import ProFileFields, RegisterForm



class HomeAdnim(LoginRequiredMixin, ListView):
    queryset = Book.objects.all()
    template_name = 'registration/home.html'
    context_object_name = 'list_books'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Book.objects.all()
        else:
            return Book.objects.filter(author=self.request.user)
        

class CreateBook(FieldMixin, LoginRequiredMixin, NotationMixin, CreateView):
    model = Book
    template_name = 'registration/created.html'
    
    
    
class UpdateBook(LoginRequiredMixin, FieldMixin, WeiterMixin, NotationMixin, UpdateView):
    model = Book
    template_name = 'registration/update.html'



class DeleteBook(WeiterMixin, DeleteView):
    model = Book
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('account:home')


class ProFileView(UpdateView):
    model = User
    form_class = ProFileFields
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(id=self.request.user.pk)
    


class SearchLlist(ListView):
    template_name = 'registration/search.html'
    
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Book.objects.filter(Q(content__icontains=search) | Q(title__icontains=search))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context


class SignUpView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("account:login")
    template_name = 'registration/signup.html'   


def logout_view(request):
    logout(request)
    return redirect('account:login')