from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag("blogs/category_navbar.html")
def category_tags():
    return {
        "category" : Category.objects.filter(status=True)
    }