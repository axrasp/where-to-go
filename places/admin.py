from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ['place', ]
    readonly_fields = ['place_preview']
    fields = ('image', 'place_preview', 'number')

    def place_preview(self, obj):
        return format_html(
            '<img src="{}" width="200px"/>',
            obj.image.url
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
