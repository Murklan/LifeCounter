from django.contrib import admin
from .models import Game, Player, CommanderDamage


class PlayerInline(admin.TabularInline):
    model = Player


class GameAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]


admin.site.register(Game, GameAdmin)
admin.site.register(CommanderDamage)
