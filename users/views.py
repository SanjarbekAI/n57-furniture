import threading

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from users.forms import RegisterForm
from .utils import send_email_confirmation

UserModel = get_user_model()


class EmailVerificationView(TemplateView):
    template_name = "auth/email-verification-page.html"


class RegisterView(FormView):
    template_name = "auth/user-register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:verification-page")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        email_thread = threading.Thread(target=send_email_confirmation, args=(user, self.request,))
        email_thread.start()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class VerificationView(View):
    def get(self, request, *args, **kwargs):
        try:
            uid = kwargs.get('uid')
            token = kwargs.get('token')

            user = UserModel.objects.get(id=uid)
        except UserModel.DoesNotExist:
            return redirect('/')
        try:
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                messages.success(self.request, "Your email is verified!")
                return redirect('/')
            else:
                messages.success(self.request, "Link is not correct")
                return redirect('/')
        except Exception as e:
            print(e)
            return redirect('/')
