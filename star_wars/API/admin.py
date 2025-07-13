from django.contrib import admin
from .models import (
    User, Planet, Activity, Destination, Accommodation,
    Tour, TourDestination, Booking, Review
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")
    ordering = ("id",)


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "population", "language", "currency")
    search_fields = ("name", "language", "currency")
    ordering = ("id",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    search_fields = ("name", "type")
    ordering = ("id",)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "planet", "activity")
    search_fields = ("name",)
    list_filter = ("planet", "activity")
    ordering = ("id",)


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "destination", "price", "rooms")
    search_fields = ("name",)
    list_filter = ("destination",)
    ordering = ("id",)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "duration", "price", "available_spots")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(TourDestination)
class TourDestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "tour", "destination", "visit_date")
    list_filter = ("tour", "destination")
    ordering = ("id",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tour", "accommodation", "date", "people", "status")
    list_filter = ("status", "date", "payment_method")
    search_fields = ("user__name",)
    ordering = ("id",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "booking", "rating", "date")
    list_filter = ("rating", "date")
    ordering = ("id",)
