from rest_framework import viewsets
from .models import (
    Planet, Activity, Destination, Accommodation,
    Tour, TourDestination, Booking, Review
)
from .serializers import (
    PlanetSerializer, ActivitySerializer, DestinationSerializer,
    AccommodationSerializer, TourSerializer, TourDestinationSerializer,
    BookingSerializer, ReviewSerializer
)


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class TourDestinationViewSet(viewsets.ModelViewSet):
    queryset = TourDestination.objects.all()
    serializer_class = TourDestinationSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
