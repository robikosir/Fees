from django.contrib import admin

# Register your models here.
from fees.player_fees.models import PlayerFees

admin.site.register(PlayerFees)
