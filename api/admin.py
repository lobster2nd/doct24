from django.contrib import admin

from .models import Category, Subcategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image')
    list_display_links = ('name', 'slug', 'image')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image', 'category')
    list_display_links = ('name', 'slug', 'image')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'image', 'category')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'image', 'cat')
    list_display_links = ('name', 'image')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'price', 'image', 'cat')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_title = 'Админ-панель магазина'
admin.site.site_header = 'Админ-панель магазина'
