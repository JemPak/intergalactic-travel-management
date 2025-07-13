from django.db import models
from django.contrib.auth import get_user_model


class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    image = models.ImageField(upload_to='planets/')

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='destinations')
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True, related_name='destinations')
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='accommodations')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField()
    image = models.ImageField(upload_to='accommodations/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tours/')
    available_spots = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class TourDestination(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_destinations')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tour_destinations')
    visit_date = models.DateField()

    def __str__(self):
        return f"{self.tour.name} - {self.destination.name} ({self.visit_date})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmado', 'Confirmado'),
        ('Pendiente', 'Pendiente'),
        ('Cancelado', 'Cancelado'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bookings')
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    accommodation = models.ForeignKey(Accommodation, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    date = models.DateField()
    people = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Reserva #{self.id} - {self.user.name}"


class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Review #{self.id} - {self.rating} estrellas"
