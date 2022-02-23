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

    firstName = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'First Name*'))
    
    lastName = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'Last Name*'))
    
    internationalPhoneNumRegEx = '^[0-9/-/(/)]{10,20}$'
    phoneNumMsg = "Given phone number is not a valid phone number format."
    phoneNum = forms.CharField(widget=forms.TextInput(attrs={'required':False}),
                                   label=_(u'Phone Number'),
                                   validators=[RegexValidator(regex=internationalPhoneNumRegEx,
                                                                message=phoneNumMsg)])
    
    street = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'Street*'))

    city = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'City*'))

    localCodeMsg = "Given State/Territory code is not a valid 2-3 length alphanumeric code."
    localCode = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'State/Territory*'),
                                   validators=[RegexValidator(regex='^[0-9A-Z]{2,3}$',
                                                                message=localCodeMsg)])

    zipCodeMsg = "Given Zip/Postal code is not a valid 5 Postal Code."
    zipCode = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'Zip/Postal Code*'),
                                   validators=[RegexValidator(regex='^[0-9]{5}$',
                                                                message=zipCodeMsg)])
    
    

    countryCodeMsg = "Given Country Code is not a valid 2 letter code."
    countryCode = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                   label=_(u'Country Code*'),
                                   validators=[RegexValidator(regex='^[A-Z]{2}$',
                                                                message=countryCodeMsg)])

    class Meta:
        model = User
        fields = ("username", "password1", "password2","firstName",
                    "lastName","phoneNum","street","city","localCode","zipCode","countryCode")