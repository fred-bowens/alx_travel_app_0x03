from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = 'Booking Confirmation'
    message = f"Dear customer,\n\nThank you for your booking.\n\nDetails:\n{booking_details}\n\nBest regards,\nALX Travel"
    send_mail(subject, message, 'noreply@alxtravel.com', [to_email])
