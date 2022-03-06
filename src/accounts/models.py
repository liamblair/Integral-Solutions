from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    """
    New User model with email as the primary qualifier
    """

    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=False)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=35)
    local_code = models.CharField(max_length=2)
    country_code = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    is_coord = models.BooleanField('grad coord status', default=False)
    is_comm = models.BooleanField('committee member status', default=False)
    is_advisor = models.BooleanField('major advisor status', default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['first_name', 'last_name', 'country_code', 'zip_code', 'local_code', 'street_address']

    objects = UserManager()

    

