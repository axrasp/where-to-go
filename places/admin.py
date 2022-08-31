from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class PlaceImageInline(SortableTabularInline, admin.TabularInline):
    model = Image
    readonly_fields = ['place_preview']
    fields = ('image', 'place_preview', 'number')

    def place_preview(self, obj):
        return format_html(
            '<img src="{}" width="200px"/>',
            obj.image.url
        )


class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
