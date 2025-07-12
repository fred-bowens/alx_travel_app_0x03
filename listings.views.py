from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from listings.tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        
        # Extract necessary info for email
        user_email = booking.user.email
        booking_info = f"Trip: {booking.trip}\nDate: {booking.date}\nGuests: {booking.guests}"
        
        # Trigger the Celery task
        send_booking_confirmation_email.delay(user_email, booking_info)
