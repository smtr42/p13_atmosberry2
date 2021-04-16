from django import forms
from api.models import Device, Sensor


class SensorForm(forms.Form):
    device = forms.ModelMultipleChoiceField(queryset=None)
    sensor_type = forms.CharField(label='What is the type ?', widget=forms.Select(choices=Sensor.SENSOR_TYPE_CHOICE))
    def __init__(self, user, *args, **kwargs):
        super(SensorForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(user=user)

class AddressForm(forms.Form):
    pass


# good
class DeviceForm(forms.Form):
    device = forms.CharField(max_length=100, required=True,)
    lat = forms.DecimalField(max_digits=9, decimal_places=6)
    lon = forms.DecimalField(max_digits=9, decimal_places=6)