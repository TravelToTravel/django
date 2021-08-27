from django.contrib import admin

# Register your models here.
from category.models import Party, Age, Location, Purpose

admin.site.register(Party)
admin.site.register(Age)
admin.site.register(Location)
admin.site.register(Purpose)

