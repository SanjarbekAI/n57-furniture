from django.urls import path

from users.views import EmailVerificationView, RegisterView, VerificationView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # path("login/", LoginFormView.as_view(), name="login"),
    # path("logout/", MyLogoutView.as_view(), name="logout"),
    # path("forget/password/", ForgetPasswordFormView.as_view(), name="forget-password"),
    # path("verification/resend/", VerificationResendView.as_view(), name="verification-resend"),
    path("verification/page/", EmailVerificationView.as_view(), name="verification-page"),
    path("verification/<int:uid>/<str:token>/", VerificationView.as_view(), name="verification"),
    # path("account/", AccountView.as_view(), name="account"),
    # path("account/delete/", AccountDeleteView.as_view(), name="account-delete"),
    # path("update/password/", UpdatePasswordView.as_view(), name="update-password"),
]
