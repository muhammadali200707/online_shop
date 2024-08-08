from django.contrib import admin
from django.contrib.auth.models import User, Group

from online_shop.models import Category, Product, Comment, Order

admin.site.unregister(User)
admin.site.unregister(Group)


class IsVeryExpensiveFilter(admin.SimpleListFilter):
    title = 'is_very_expensive_product'
    parameter_name = 'Is Very Expensive Products'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(price__gt=20_000_000)
        elif value == 'No':
            return queryset.filter(price__lte=20_000_000)
        return queryset


class IsProvide(admin.SimpleListFilter):
    title = 'is_provide_products'
    parameter_name = 'Is Provided Products'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(product__is_provide=True)
        elif value == 'No':
            return queryset.filter(product__is_provide=False)
        return queryset


class IsTopProduct(admin.SimpleListFilter):
    title = 'is_top_product'
    parameter_name = 'Is Top Products'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(order__gt=10)
        elif value == 'No':
            return queryset.filter(order__lte=10)
        return queryset


@admin.register(Category)
class CategoryModelaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'product_count')
    search_fields = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

    def product_count(self, obj):
        return obj.products.count()


@admin.register(Product)
class ProductModelaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'discount', 'is_very_expensive_product')
    search_fields = ('name',)
    list_filter = ['category', IsVeryExpensiveFilter]

    def is_very_expensive_product(self, obj):
        return obj.price > 20_000_000

    is_very_expensive_product.boolean = True


@admin.register(Comment)
class CommentModelaAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_provide_product')
    search_fields = ('name', 'email')
    list_filter = [IsProvide]

    def is_provide_product(self, obj):
        return obj.is_provide is True

    is_provide_product.boolean = True


@admin.register(Order)
class OrderModelaAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'quantity')
    search_fields = ('name', 'phone')
    list_filter = [IsTopProduct]

    def is_top_product(self, obj):
        return obj.quantity > 10

    is_top_product.boolean = True
