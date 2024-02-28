from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import Book
from .serializer import PostSerializer, UserSerializer
from account.models import User
from .Permissions import IsOwnerPermission, IsOwnerObjPermission



class ListBookAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerObjPermission,)


class DetailBookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = PostSerializer



class UserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerPermission,)


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerPermission,)


class BookViewSet(ModelViewSet):
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    filter_backends = ['status','category']
    search_fields = ['category', 'title', 'content']
    
    def get_permissions(self):
        if self.action == ['list', 'create']:
            permission_classes = (IsOwnerObjPermission,)
        else:
            permission_classes = (IsOwnerObjPermission,IsOwnerObjPermission)
        return [permission() for permission in permission_classes]
    permission_classes = (IsOwnerObjPermission,)
 
    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author=author)
        return queryset
        
    


# class RevokeTokenAPIView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)
    