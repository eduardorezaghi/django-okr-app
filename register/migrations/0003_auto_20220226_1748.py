# Generated by Django 2.2 on 2022-02-26 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20220223_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectivekeyresult',
            name='objetivo',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only text characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='objectivekeyresult',
            name='resultado_1',
            field=models.CharField(max_length=300, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only text characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='objectivekeyresult',
            name='resultado_2',
            field=models.CharField(blank=True, max_length=300, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only text characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='objectivekeyresult',
            name='resultado_3',
            field=models.CharField(blank=True, max_length=300, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only text characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='objectivekeyresult',
            name='resultado_4',
            field=models.CharField(blank=True, max_length=300, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only text characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='objectivekeyresult',
            name='resultado_5',
            field=models.CharField(blank=True, max_length=300, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only text characters are allowed.')]),
        ),
    ]