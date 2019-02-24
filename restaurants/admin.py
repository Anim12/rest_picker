# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from restaurants.models import Restaurant, Food, City

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields': ['name','desc','menu']}),
                 ('Address',{'fields':['address','post_code','city']}),
                 ('Contact',{'fields':['web','gmap_url','phone']}),
                 ('Food',{'fields':['food']}),
                 ('Pictures',{'fields':['picture','map']}),]
 

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food)
admin.site.register(City)
