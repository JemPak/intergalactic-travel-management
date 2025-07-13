from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet, PlanetViewSet, ActivityViewSet, DestinationViewSet,
    AccommodationViewSet, TourViewSet, TourDestinationViewSet,
    BookingViewSet, ReviewViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'planets', PlanetViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'accommodations', AccommodationViewSet)
router.register(r'tours', TourViewSet)
router.register(r'tour-destinations', TourDestinationViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
