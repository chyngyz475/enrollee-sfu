from django import forms

from .models import FeedBack

class FeedBackForm(forms.Form):
  class Meta:
    model = FeedBack
    Fields = ['name','phone', 'description']