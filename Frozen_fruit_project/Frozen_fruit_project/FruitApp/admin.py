from django.contrib import admin
from .models import  *

# Register your models here.
# admin.site.register(Fruit)
admin.site.register(Order)

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display =('name','price_per_kg','quantity_in_kg')