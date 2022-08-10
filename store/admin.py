from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


class ProductPicturesInline(admin.StackedInline):
    model = ProductPictures
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="70" height="auto">')

    get_image.short_description = 'Изображение'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'slug', 'draft', 'get_image')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ProductPicturesInline]
    list_display_links = ('title',)
    save_as = True
    save_on_top = True
    form = ProductAdminForm
    list_editable = ('draft',)
    readonly_fields = ('get_image',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'year')
        }),
        (None, {
            'fields': ('manufacture', 'category', ('poster', 'get_image'))
        }),
        (None, {
            'fields': (('operating_system', 'cpu', 'memory'),)
        }),
        (None, {
            'fields': ('premier', 'slug', 'draft')
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="70" height="auto">')

    get_image.short_description = 'Изображение'


@admin.register(Manufacture)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


@admin.register(ProductPictures)
class ProductPicturesAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="70" height="auto">')

    get_image.short_description = 'Изображение'


admin.site.site_title = 'Django Online Store'
admin.site.site_header = 'Django Online Store'
