from django.contrib import admin
from django.contrib.auth.models import User, Group

from online_shop.models import Category, Product, Comment

admin.site.register(Product)
admin.site.register(Comment)

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Category)
class CategoryModelaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
