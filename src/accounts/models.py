from winreg import REG_EXPAND_SZ
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    name = models.CharField(max_length=150)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']
