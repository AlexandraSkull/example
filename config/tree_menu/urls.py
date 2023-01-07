from django.urls import path

from .views import view_tree, CategoryView

urlpatterns = [
    path('', view_tree, name='menu'),
    path('<slug:slug>/', CategoryView.as_view(), name='category'),
]

