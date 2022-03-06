from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from . import models

class SignUpForm(UserCreationForm):
    #Establish error messages for the fields that can return errors detectable by regex
    phoneNumMsg = "Given phone number is not a valid phone number format."
    localCodeMsg = "Given State/Territory code is not a valid 2-3 length alphanumeric code."
    zipCodeMsg = "Given Zip/Postal code is not a valid 5 Postal Code."
    countryCodeMsg = "Given Country Code is not a valid 2 letter code."

    #Regex for the fields that are being validated
    internationalPhoneNumRegEx = '^[0-9/-/(/)]{10,20}$'
    localCodeRegex = '^[0-9A-Z]{2,3}$'
    zipCodeRegex = '^[0-9]{5}$'
    countryCode = '^[A-Z]{2}$'

    #Field instantation for all fields that don't already have estbalished user model form fields
    #All fields follow the same layout of "Widget" and "Label", some fields use custom regex validators
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'First Name*'))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'Last Name*'))
    phone = forms.CharField(widget=forms.TextInput(attrs={'required':False}),
                                    label=_(u'Phone Number'),
                                    validators=[RegexValidator(regex=internationalPhoneNumRegEx,
                                                                message=phoneNumMsg)])
    street_address = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'Street*'))
    city = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'City*'))
    local_code = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'State/Territory*'),
                                    validators=[RegexValidator(regex=localCodeRegex,
                                                                message=localCodeMsg)])
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'Zip/Postal Code*'),
                                    validators=[RegexValidator(regex=zipCodeRegex,
                                                                message=zipCodeMsg)])
    country_code = forms.CharField(widget=forms.TextInput(attrs={'required':True}),
                                    label=_(u'Country Code*'),
                                    validators=[RegexValidator(regex=countryCode,
                                                                message=countryCodeMsg)])

    class Meta:
        model = models.User
        fields = ("email","password1","password2","first_name","last_name","phone","street_address","city","local_code","zip_code","country_code")

class UserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ("email",)
