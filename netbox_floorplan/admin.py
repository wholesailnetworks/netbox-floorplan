from django.contrib import admin
from .models import FloorplanObject, Floorplan


@admin.register(FloorplanObject)
class FloorplanObjectAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "rack",
        "location",
        "floorplan",
        "x_coordinate",
        "y_coordinate",
        "rotation"
    )


@admin.register(Floorplan)
class FloorplanAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
    )
