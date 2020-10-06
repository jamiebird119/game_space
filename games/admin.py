from django.contrib import admin
from .models import Game, Console, Genre


class GameAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'rating',
        'price',
        'publisher',
        'release_year'
    )
    ordering = ('name',)


class ConsoleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Game, GameAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Genre, GenreAdmin)
