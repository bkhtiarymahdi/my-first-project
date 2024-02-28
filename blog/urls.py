from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.BookListView.as_view(), name='home'),
    path('page/<int:page>', views.BookListView.as_view(), name='home'),
    path('detail/<int:id>/', views.DetailBookView.as_view() ,name='detail'),
    path('category/page/<int:id>', views.CategoryListView.as_view(), name='category'),
    # path('category/<int:id>', views.CategoryListView.as_view() , name='category'),
    path('author/<int:id>', views.AuthorListBook.as_view() , name='author'),
]
