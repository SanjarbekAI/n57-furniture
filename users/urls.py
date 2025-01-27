from django.urls import path

from users.views import EmailVerificationView, RegisterView, VerificationView, LoginFormView, MyLogoutView, \
    ForgetPasswordEmailTemplateView, ForgetPasswordEmailView, UpdatePasswordFormView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginFormView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("forget/password/", ForgetPasswordEmailView.as_view(), name="forget-password"),
    path("forget/password/email/", ForgetPasswordEmailTemplateView.as_view(), name="forget-password-email"),
    path("update/password/<int:uid>/<str:token>/", UpdatePasswordFormView.as_view(), name="update-password"),
    # path("verification/resend/", VerificationResendView.as_view(), name="verification-resend"),
    path("verification/page/", EmailVerificationView.as_view(), name="verification-page"),
    path("verification/<int:uid>/<str:token>/", VerificationView.as_view(), name="verification"),
    # path("account/", AccountView.as_view(), name="account"),
    # path("account/delete/", AccountDeleteView.as_view(), name="account-delete"),
    # path("update/password/", UpdatePasswordView.as_view(), name="update-password"),
]
