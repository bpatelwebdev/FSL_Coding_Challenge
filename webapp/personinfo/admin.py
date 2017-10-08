from django.contrib import admin

from .models import Household,Person,Vehicle

admin.site.register(Household)
admin.site.register(Person)
admin.site.register(Vehicle)
