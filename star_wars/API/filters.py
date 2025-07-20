
from .models import (
    Accommodation, Tour
)
from Authentication.models import User

import django_filters

class TourFilter(django_filters.FilterSet):
    activity = django_filters.NumberFilter(field_name='tour_destinations__destination__activity', lookup_expr='exact')
    planet = django_filters.NumberFilter(field_name='tour_destinations__destination__planet', lookup_expr='exact')
    duration = django_filters.CharFilter(field_name='duration', lookup_expr='iexact')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Tour
        fields = ['activity', 'planet', 'duration']
        
class AccomodationFilter(django_filters.FilterSet):
    activity = django_filters.NumberFilter(field_name='destination__activity', lookup_expr='exact')
    planet = django_filters.NumberFilter(field_name='destination__planet', lookup_expr='exact')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Accommodation
        fields = ['activity', 'planet']

class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name='email', lookup_expr='exact')

    class Meta:
        model = User
        fields = ['email']