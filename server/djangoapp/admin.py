from django.contrib import admin
# from .models import related models\
from .models import CarMake
from .models import CarModel

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ["dealerID", "type", "year"]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ["name", "description"]
    inlines = [CarModelInline]

# Register your models here.
admin.site.register(CarMake, CarMakeAdmin)
