from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # 1. Save message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        # 2. Email to admin
        context =  {
    "name": name,
    "email": email,
    "phone": phone,
    "subject": subject,
    "message": message,
}
        email_body = render_to_string("contact_email.html", context)

        email_msg = EmailMessage(
            subject=f"{subject}",
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
        )
        email_msg.content_subtype = "html"
        email_msg.send()

        # 3. Confirmation email to user
        send_mail(
            subject="We received your message",
            message="Thank you for contacting us. We'll get back to you shortly.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=True
        )

        messages.success(request, "Thank you! Your message has been sent.")
        return redirect("contact")
    

    return render(request, "contact.html")
