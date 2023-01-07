from django import template

from tree_menu.models import Category

register = template.Library()

@register.simple_tag()
def get_meta_categories(): #draw menu
    return Category.objects.filter(parent=None)
