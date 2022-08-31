from django.contrib import admin
from .models import Place, Image


class PlaceImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ['place', ]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


admin.site.register(Image)