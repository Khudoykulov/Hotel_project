from django.contrib import admin
from .models import Room, RoomService, RoomContent


class ContentAdminInline(admin.TabularInline):
    model = RoomContent
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'create_date', 'check_in', 'check_out')
    search_fields = ('name', 'price', 'check_in', 'check_out')
    list_filter = ('name', 'price', 'check_in', 'check_out')
    date_hierarchy = 'create_date'
    list_display_links = ('name', 'price', 'create_date', 'check_in', 'check_out')
    inlines = [ContentAdminInline]


@admin.register(RoomService)
class RoomService(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)



