# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Ticket(models.Model):

    #__Ticket_FIELDS__
    number = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")


class Box(models.Model):

    #__Box_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Box_FIELDS__END

    class Meta:
        verbose_name        = _("Box")
        verbose_name_plural = _("Box")


class Branch Office(models.Model):

    #__Branch Office_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    additional_info = models.CharField(max_length=255, null=True, blank=True)

    #__Branch Office_FIELDS__END

    class Meta:
        verbose_name        = _("Branch Office")
        verbose_name_plural = _("Branch Office")



#__MODELS__END
