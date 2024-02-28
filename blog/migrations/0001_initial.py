# Generated by Django 5.0.1 on 2024-01-28 20:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود؟')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('img', models.ImageField(upload_to='images', verbose_name='تصویر')),
                ('time_publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد شدن')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(to='blog.category', verbose_name='دسته بندی ')),
            ],
            options={
                'verbose_name': 'کتاب ',
                'verbose_name_plural': 'کتاب ها',
            },
        ),
    ]