# Generated by Django 5.0.1 on 2024-01-31 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='family',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='blog.category', verbose_name='سر شاخه'),
        ),
    ]
