# Generated by Django 5.0.3 on 2024-04-07 09:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0011_remove_patient_details_user_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_details',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='phone_number',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]