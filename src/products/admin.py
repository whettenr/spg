from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Product, Variation, ProductImage, Category, ProductFeatured

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10


class ProductAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'price']
	inlines = [
		ProductImageInline,
		VariationInline,
	]
	formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

# admin.site.register(Variation)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)