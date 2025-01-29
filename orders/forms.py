from django import forms


class CheckoutForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=128)
    phone_number = forms.CharField(max_length=13)
    address = forms.CharField(max_length=255)


