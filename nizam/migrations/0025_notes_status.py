# Generated by Django 5.0.3 on 2024-03-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0024_remove_survey_opt1_remove_survey_opt2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]