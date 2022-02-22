from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models

attrs_dict = { 'class': 'required' }

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class SignUpForm(UserCreationForm):
    #Remove attributes dictionary for required field, Django has native support for this

    username = forms.EmailField(widget=forms.TextInput(attrs={'required': True,'maxlength':75}),
                                label=_(u'Email Address'))
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")