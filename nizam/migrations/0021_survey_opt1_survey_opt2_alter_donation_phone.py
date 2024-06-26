# Generated by Django 5.0.3 on 2024-03-25 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0020_remove_survey_option1_remove_survey_option2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='opt1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='survey',
            name='opt2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999999999)]),
        ),
    ]
