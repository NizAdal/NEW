# Generated by Django 5.0.3 on 2024-03-28 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0035_rename_opt1_question_no_rename_opt2_question_yes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='No',
            new_name='no',
        ),
    ]