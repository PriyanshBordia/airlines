from django.contrib import admin

from .models import Airport, Flight, Passenger

class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

# class PassengerAdmin(admin.ModelAdmin):
#     flights =

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)
