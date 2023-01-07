from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Category

def view_tree(request):
    return render(request, 'tree_menu/view_menu.html')

class CategoryView(ListView):
    model = Category
    template_name = 'tree_menu/view_category.html'

    def get_context_data(self, **kwargs):
        category = Category.objects.get(slug=self.kwargs['slug'])
        categories = Category.objects.all()

        if Category.objects.filter(parent=category):
            child = True
        else:
            child = False

        context = {
            'category':category,
            'child':child,
            'categories': categories,
            
        }
        return context