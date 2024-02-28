from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    img_face = models.ImageField(upload_to='image', null=True,verbose_name='تصویر')