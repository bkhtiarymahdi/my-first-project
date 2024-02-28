from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django.db.models.fields import GenericIPAddressField

from account.models import User
from tarikhshamsi.functionfarsi import converter



class Main_Manager(models.Manager):
    def main_status(self):
        return self.filter(status=True)



class Category(models.Model):
    family = models.ForeignKey('self',default=None , on_delete=models.SET_NULL ,related_name='kid' , null=True , blank=True ,verbose_name='سر شاخه')
    title = models.CharField(max_length = 100 ,verbose_name='عنوان دسته بندی')
    status = models.BooleanField(default=True, verbose_name='نمایش داده شود؟')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class Get_Ip_Address(models.Model):
    put_ip_user = models.GenericIPAddressField()



class Book(models.Model):
    title = models.CharField(max_length = 100 ,verbose_name='عنوان')
    category =models.ManyToManyField(Category ,verbose_name='دسته بندی ' ,related_name='cat_books')
    author = models.ForeignKey(User ,on_delete=models.CASCADE,null=True, blank=True, verbose_name='نویسنده', related_name='writer')
    writer_book = models.CharField(max_length = 100 , null=True, verbose_name='نویسنده ی کتاب')
    content = models.TextField(verbose_name='محتوا')
    status = models.BooleanField(default=True ,verbose_name='وضعیت')
    img = models.ImageField(upload_to='image' ,verbose_name='تصویر')
    time_publish = models.DateTimeField(default=timezone.now ,verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True ,verbose_name='زمان ایجاد شدن')
    ip_user = models.ManyToManyField(Get_Ip_Address, blank=True, related_name='ip_user')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('account:home')
    
    def publish(self):
        return converter(self.time_publish)
    
    def get_img(self):
        return format_html("<img src:'{}'>".format(self.img.url))
    
    class Meta:
        verbose_name = 'کتاب '
        verbose_name_plural = 'کتاب ها'


objects = Main_Manager