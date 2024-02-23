from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['name', 'message',]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Your Name'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control mb-30',
            'placeholder': 'Start the discussion...'
        })

