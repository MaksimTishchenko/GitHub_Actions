from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')

    @admin.action(description='Set price to 0')
    def make_free(self, request, queryset):
        queryset.update(price=0)

    actions = [make_free]