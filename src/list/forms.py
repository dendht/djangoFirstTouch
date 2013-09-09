from django import forms
from django.forms import ModelForm

from list.models import Attachment


class PriceForm(forms.ModelForm):

    class Meta:
        model = Attachment
        exclude = ('insp', 'contributor', 'date', 'title')

    def handle_uploaded_file(self, f):
        destination = open('src/list/name.txt', 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()