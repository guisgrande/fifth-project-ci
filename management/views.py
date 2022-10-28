from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsLetterList


def news_letter_sub(request):
    """
    A view to user subscribe to news letter list
    """
    if request.method == 'POST':
        name = request.POST.get('news_name', None)
        email = request.POST.get('news_email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            if request.user.is_authenticated:
                if email == request.user.email:
                    pass
            else:
                messages.error(request, f"Found registered user with associated {email} email. Login first.")
                return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = NewsLetterList.objects.filter(news_email=email).first()
        
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscribed.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = NewsLetterList()
        subscribe_model_instance.news_name = name
        subscribe_model_instance.news_email = email
        subscribe_model_instance.save()

        subject = str('Street Craft - News Letter Subscrition')
        body = render_to_string(
            'management/confirmation_emails/confirmation_news_letter_sub.txt',
            {'name': name, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )      

        messages.success(request, f'{email} email was successfully subscribed to our News Letter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
