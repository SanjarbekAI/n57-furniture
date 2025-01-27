from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=128)

    def clean(self):
        username_or_email = self.cleaned_data["username_or_email"]
        password = self.cleaned_data["password"]

        try:
            user = UserModel.objects.get(
                Q(username=username_or_email) | Q(email=username_or_email)
            )
        except UserModel.DoesNotExist:
            raise forms.ValidationError("Username or password is invalid")

        credentials = {"username": user.username, "password": password}
        authenticated_user = authenticate(**credentials)
        if authenticated_user is not None:
            self.cleaned_data["user"] = authenticated_user
        else:
            raise forms.ValidationError("Username or password is invalid")
        return self.cleaned_data


class ForgetPasswordEmailForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        email = self.cleaned_data['email']
        try:
            user = UserModel.objects.get(email=email)
            self.cleaned_data["user"] = user
        except UserModel.DoesNotExist:
            raise forms.ValidationError("User is not found")

        return self.cleaned_data


class ForgetPasswordForm(forms.Form):
    new_password1 = forms.CharField(max_length=128)
    mew_password2 = forms.CharField(max_length=128)


class UpdatePasswordForm(ForgetPasswordForm):
    old_password = forms.CharField(max_length=128)


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'email']
