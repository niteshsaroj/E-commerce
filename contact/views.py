from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactSerializer
from .models import ContactMessage

class ContactAPIView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Email to admin
            send_mail(
                subject=f"[Contact] {contact.subject}",
                message=f"Message from {contact.name} ({contact.email}):\n\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            # Confirmation email to user
            send_mail(
                subject="Thank you for contacting us",
                message=f"Dear {contact.name},\n\nThank you for reaching out. We have received your message:\n\n{contact.message}\n\nWe'll get back to you shortly.\n\nRegards,\nE-Shop Team",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                fail_silently=False,
            )

            return Response({"message": "Contact message sent successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
