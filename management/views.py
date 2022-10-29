from django.shortcuts import redirect, reverse, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsLetterList, NewsLetterMail


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

        messages.success(request, f'{email} was successfully subscribed to our News Letter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def news_letter_view(request):
    """
    A view to display News Letter email form.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can view this page.')
        return redirect(reverse('home'))

    return render(request, 'management/admin_news_letter.html')


@login_required
def news_letter_send(request):
    """
    A view to site owner send News Letter email to subscribers
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, just site owner can send emails.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        subject = request.POST.get('subject', None)
        body = request.POST.get('body', None)
       
        if not subject or not body:
            messages.error(request, "You forgot to fill in one of the fields.")
            return redirect("/")
        
        email_list = []
        for subscriber in NewsLetterList.objects.all():
            email_list.append(subscriber.news_email)

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email_list]
        )

        news_letter_mails = NewsLetterMail()
        news_letter_mails.subject = subject
        news_letter_mails.body = body
        news_letter_mails.status = 1
        news_letter_mails.save()

        messages.success(request, 'News Letter successfully sent to mailing list!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
