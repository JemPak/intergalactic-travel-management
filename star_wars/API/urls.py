from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PlanetViewSet, ActivityViewSet, DestinationViewSet,
    AccommodationViewSet, TourViewSet,
    BookingViewSet, ReviewViewSet, UserViewSet
)

router = DefaultRouter()
router.register(r'planets', PlanetViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'accommodations', AccommodationViewSet)
router.register(r'tours', TourViewSet)
# router.register(r'tours/<int:tour_id>/destinations', TourDestinationViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
