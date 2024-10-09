from django.contrib import admin
from .models import Room, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'check_in', 'check_out', 'guests', 'room_id')
    search_fields = ('full_name', 'email')  # Use 'full_name' instead of 'name'

admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)
