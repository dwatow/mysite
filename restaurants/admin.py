from django.contrib import admin

# Register your models here.
from restaurants.models import Restaurant, Food


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'comment', 'is_spicy', 'restaurant')
    list_filter = ('is_spicy',)
    fields = ('price','restaurant')
    
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
