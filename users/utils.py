from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse


def send_email_confirmation(user, request):
    token = default_token_generator.make_token(user)
    uid = user.pk

    confirmation_link = request.build_absolute_uri(
        reverse('users:verification', kwargs={'uid': uid, 'token': token})
    )

    subject = "Confirm Your Email Address"
    html_message = render_to_string('auth/email_confirmation.html', {
        'user': user,
        'confirmation_link': confirmation_link,
        "title": "Please, tap to link to verify your email"
    })

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.content_subtype = 'html'
    email.send()


def send_email_update_password(user, request):
    token = default_token_generator.make_token(user)
    uid = user.pk

    confirmation_link = request.build_absolute_uri(
        reverse('users:update-password', kwargs={'uid': uid, 'token': token})
    )

    subject = "Update your password"
    html_message = render_to_string('auth/email_confirmation.html', {
        'user': user,
        'confirmation_link': confirmation_link,
        "title": "Please, tap to link to update your password"
    })

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.content_subtype = 'html'
    email.send()
