from django.contrib import admin
from .models import Center,Storage

# Register your models here.

class StorageInline(admin.TabularInline):
    model = Storage
    readonly_fields = ["booked_quantity"]

class CustomCenterAdmin(admin.ModelAdmin):
    inlines = [StorageInline]
    search_fields = ["name"]
    list_display = ["name","address"]
    ordering = ["-name"]
    fields = (
        ("name"),
        ("address")
    )
    

admin.site.register(Center,CustomCenterAdmin)