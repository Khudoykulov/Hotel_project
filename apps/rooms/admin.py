from django.contrib import admin
from .models import Room, RoomService, RoomContent, Image, Booking


class ContentAdminInline(admin.TabularInline):
    model = RoomContent
    extra = 0


class ImageAdminInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'create_date', 'size_a', 'size_b', 'bed', 'max_person')
    search_fields = ('name', 'price', 'max_person')
    list_filter = ('name', 'price', 'max_person',)
    date_hierarchy = 'create_date'
    readonly_fields = ('create_date', 'slug')
    list_display_links = ('name', 'price', 'create_date', 'size_a', 'size_b', 'bed', 'max_person')
    inlines = [ContentAdminInline, ImageAdminInline]


@admin.register(RoomService)
class RoomService(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    fields = ('room', 'check_in', 'check_out',)
    list_display = ('room', 'check_in', 'check_out',)
    search_fields = ('price_min', 'price_max',)
    list_display_links = ('room', 'check_in', 'check_out',)





