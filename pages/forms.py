from django import forms


class DeviceForm(forms.Form):
    device = forms.CharField(
        max_length=100,
        required=True,
    )
    lat = forms.DecimalField(max_digits=9, decimal_places=6)
    lon = forms.DecimalField(max_digits=9, decimal_places=6)
