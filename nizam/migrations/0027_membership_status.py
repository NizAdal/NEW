# Generated by Django 5.0.3 on 2024-03-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0026_remove_question_opt1_remove_question_opt2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]