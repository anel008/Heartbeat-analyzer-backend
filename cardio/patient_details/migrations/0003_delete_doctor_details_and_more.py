# Generated by Django 5.0.3 on 2024-03-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0002_doctor_details_alter_patient_details_chest_pain_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor_details',
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='chest_pain',
            field=models.CharField(choices=[('1', 'yes'), ('0', 'no')], max_length=50),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='hyper_tension_bp',
            field=models.CharField(choices=[('1', 'yes'), ('0', 'no')], max_length=50),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='palpitation',
            field=models.CharField(choices=[('1', 'yes'), ('0', 'no')], max_length=50),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='surgery',
            field=models.CharField(choices=[('1', 'yes'), ('0', 'no')], max_length=50),
        ),
    ]