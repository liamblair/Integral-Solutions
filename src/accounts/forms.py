from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from . import models

class SignUpForm(UserCreationForm):

    username = forms.EmailField(widget=forms.TextInput(attrs={'required': True,'maxlength':75}),
                                label=_(u'Email Address'))

    zipCodeMessage = "Entered zip code is not a valid 5 digit US Postal Code."
    zipCode = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'Number Field'),
                                   validators=[RegexValidator(regex='[0-9]{5}',
                                                                message=zipCodeMessage)])
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2","zipCode")