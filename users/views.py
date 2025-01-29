import threading

from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from users.forms import RegisterForm, LoginForm, ForgetPasswordForm, ForgetPasswordEmailForm
from .utils import send_email_confirmation, send_email_update_password

UserModel = get_user_model()


class EmailVerificationView(TemplateView):
    template_name = "auth/email-verification-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Email verification"
        context["header"] = "Email verification link"
        context["message"] = "Please, check your email"
        return context


class ForgetPasswordEmailTemplateView(TemplateView):
    template_name = "auth/email_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Forget password email"
        context["header"] = "Email password"
        context["message"] = "Please, check your email, we sent a link to update your password"
        return context


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


class LoginFormView(FormView):
    template_name = "auth/user-login.html"
    form_class = LoginForm
    success_url = reverse_lazy("products:list")

    def form_valid(self, form):
        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request=self.request, user=user)
            messages.success(self.request, "You are successfully logged in")
            next_url = self.request.GET.get('next', reverse_lazy("products:list"))
            return redirect(next_url)
        else:
            self.form_invalid(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class MyLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request=self.request)
        return redirect(reverse_lazy('products:list'))

    def post(self, request, *args, **kwargs):
        logout(request=self.request)
        return redirect(reverse_lazy('products:list'))


class ForgetPasswordEmailView(FormView):
    template_name = "auth/forget-password-email.html"
    form_class = ForgetPasswordEmailForm
    success_url = reverse_lazy("users:forget-password-email")

    def form_valid(self, form):
        user = form.cleaned_data["user"]
        email_thread = threading.Thread(target=send_email_update_password, args=(user, self.request,))
        email_thread.start()
        return super().form_valid(form)


class UpdatePasswordFormView(FormView):
    template_name = 'auth/update-password.html'
    form_class = ForgetPasswordForm
    success_url = reverse_lazy("users:login")
