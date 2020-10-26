from django.contrib import admin
from .models import Order, OrderLineItem, Discount
# Register your models here.


class OrderLineItemAdmininline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', 'total_after_discount')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdmininline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'grand_total',
                       'original_bag', 'stripe_pid', 'original_total')

    fields = ('order_number', 'user', 'date', 'full_name', 'email',
              'phone_number', 'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county',
              'delivery_cost', 'order_total', 'grand_total', 'original_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date',)


class DiscountAdmin(admin.ModelAdmin):
    model = Discount
    fields = [
        'name', 'code', 'expiry_date', 'offer_discount',
        'offer_details', 'games_or_consoles_valid'
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)
