from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.


class Customdoctor(AbstractUser):
    Doctor_license_no = models.PositiveBigIntegerField()


    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'
        db_table = 'custom_doctor'

    # Add custom related names for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='doctor_set',
        related_query_name='doctor',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='doctor_set',
        related_query_name='doctor',
        help_text=('Specific permissions for this doctor.'),
    )