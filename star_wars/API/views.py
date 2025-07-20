from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from Authentication.models import User

from .models import (
    Planet, Activity, Destination, Accommodation,
    Tour, TourDestination, Booking, Review
)
from .serializers import (
    PlanetSerializer, ActivitySerializer, DestinationSerializer,
    AccommodationSerializer, TourSerializer, TourDestinationSerializer,
    BookingSerializer, ReviewSerializer, UserSerializer
)

from .filters import TourFilter, AccomodationFilter, UserFilter

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    search_fields = ["name",]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    search_fields = ["name","description",]


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    search_fields = ["name","description", "planet__name"]


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    search_fields = ["name", "description", "destination__name",
                     "destination__description", "destination__planet__name"
                 ]
    filterset_class = AccomodationFilter

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    search_fields = ["name", "description", "tour_destinations__destination__name",
                 "tour_destinations__destination__description", "tour_destinations__destination__planet__name"
                 ]
    filterset_class = TourFilter
    
    @action(detail=True, methods=["get"])
    def destinations(self, request, pk=None):
        """
        Retorna los destinos asociados a un tour específico (por ID del tour).
        """
        tour_destinations = TourDestination.objects.filter(tour_id=pk).select_related("destination")
        serializer = TourDestinationSerializer(tour_destinations, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
