from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register('', views.BookViewSet)
# urlpatterns = router.urls


app_name = 'api'
urlpatterns = [
    path('', views.ListBookAPI.as_view()),
    path('detail/<int:pk>', views.DetailBookAPIView.as_view()),
    path('user/', views.UserAPIView.as_view()),
    path('user/detail/<int:pk>', views.UserDetailAPIView.as_view()),
    # path('revoke/', views.RevokeTokenAPIView.as_view())
]