from django.contrib.auth import views
from django.urls import path

from .views import(
    HomeAdnim, CreateBook, UpdateBook,
    DeleteBook, ProFileView, SearchLlist, logout_view, SignUpView
      ) 

app_name = 'account'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
#     path(
#         "password_change/", views.PasswordChangeView.as_view(), name="password_change"
#     ),
#     path(
#         "password_change/done/",
#         views.PasswordChangeDoneView.as_view(),
#         name="password_change_done",
#     ),
#     path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     path(
#         "password_reset/done/",
#         views.PasswordResetDoneView.as_view(),
#         name="password_reset_done",
#     ),
#     path(
#         "reset/<uidb64>/<token>/",
#         views.PasswordResetConfirmView.as_view(),
#         name="password_reset_confirm",
#     ),
#     path(
#         "reset/done/",
#         views.PasswordResetCompleteView.as_view(),
#         name="password_reset_complete",
#     ),
]


urlpatterns += [
    path('', HomeAdnim.as_view(), name='home'),
    path('create/', CreateBook.as_view(), name='create'),
    path('update/<int:pk>', UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>', DeleteBook.as_view(), name='delete'),
    path('profile/', ProFileView.as_view(), name='profile'),
    path('search/', SearchLlist.as_view(), name='search'),
    path('register/',SignUpView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]