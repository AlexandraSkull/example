from django.contrib import admin

from tree_menu.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'number_page')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'slug')

admin.site.register(Category, CategoryAdmin)
  