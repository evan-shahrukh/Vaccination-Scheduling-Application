from django.contrib import admin
from .models import Campaign,Slot

# Register your models here.

class SlotInline(admin.TabularInline):
    model = Slot
    readonly_fields = ["reserved"]

class CustomCampaignAdmin(admin.ModelAdmin):
    inlines = [SlotInline]
    search_fields = ["center__name","vaccine__name"]
    list_display = ["center","vaccine","start_date"]
    ordering = ["-vaccine"]
    fields = (
        ("center"),
        ("vaccine"),
        ("start_date","end_date"),
        ("agents"),
    )

admin.site.register(Campaign,CustomCampaignAdmin)