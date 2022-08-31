from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase



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
