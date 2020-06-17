from django.contrib import admin
from .models import Manufacturer, ShoeType, ShoeColor, Shoe

admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)

# Register your models here.
