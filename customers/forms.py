from django import forms

class RazorpayPaymentForm(forms.Form):
    amount = forms.DecimalField()