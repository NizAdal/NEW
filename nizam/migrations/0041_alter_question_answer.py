# Generated by Django 5.0.3 on 2024-04-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0040_remove_question_no_remove_question_yes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(default='', max_length=50),
        ),
    ]
