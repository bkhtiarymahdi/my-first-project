from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import Book


class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = '__all__'
        elif request.user.is_staff:
            self.fields = 'title', 'content', 'writer_book', 'category', 'img', 'time_publish'
        else:
            return Http404('شما نیمتوانید به این بخش وارد شدید!')
        return super().dispatch(request, *args, **kwargs)
        
    


class NotationMixin():
    def formvalid(self, form):
        if self.request.user.is_superuser:
            form.seve()
        else:
            self.obj = form.seve(commit=False)
            self.obj.author = self.request.user
            return super().formvalid(form)



class WeiterMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        edit = get_object_or_404(Book, id=pk)
        if edit.author == request.user or request.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404
    