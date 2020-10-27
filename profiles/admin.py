from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    readonly_fields = (
        'default_full_name', 'default_phone_number', 'default_postcode',
        'default_town_or_city', 'default_street_address1',
        'default_street_address2', 'default_county'
    )
    fields = [
        'default_full_name', 'default_phone_number', 'default_postcode',
        'default_town_or_city', 'default_street_address1',
        'default_street_address2', 'default_county'
    ]


admin.site.register(UserProfile, UserProfileAdmin)

