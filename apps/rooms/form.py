from django import forms

from .models import Room, Booking


class RoomForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'adults', 'children', 'price_min', 'price_max']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['check_in'].widget.attrs.update({
            'class': 'input-small form-control',
            'placeholder': 'Check In',
            'name': 'checkInDate',
            'id': 'checkInDate',
        })
        self.fields['check_out'].widget.attrs.update({
            'class': 'input-small form-control',
            'placeholder': 'Check Out',
            'name': 'checkOutDate',
            'id': 'checkOutDate'
        })
        self.fields['adults'].widget.attrs.update({
            'class': 'form-control',
            'id': 'guests',
            'name': 'adults'
        })
        self.fields['children'].widget.attrs.update({
            'class': 'form-control',
            'id': 'children',
            'name': 'children'
        })
        self.fields['price_min'].widget.attrs.update({

        })
        self.fields['price_max'].widget.attrs.update({

        })