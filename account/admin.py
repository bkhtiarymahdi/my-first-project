from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('فیلد تصویر', {'fields':('img_face',)})
),


admin.site.register(User, UserAdmin)