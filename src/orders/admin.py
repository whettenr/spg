from django.contrib import admin

# Register your models here.


from .models import UserCheckout, UserAddress, Order, Carrier, ShippingCost

class OrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', "status", "shipping_address", "shipping_price"]
	list_editable = ["status", "shipping_price"]
	list_filter = ["status", "shipping_address"]

	

	search_fields = ["title", "content"]
	class Meta:
		model = Order


admin.site.register(UserCheckout)
admin.site.register(UserAddress)
admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingCost)
admin.site.register(Carrier)