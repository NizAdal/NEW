# Generated by Django 5.0.3 on 2024-03-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0027_membership_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='file',
            field=models.ImageField(default='none', upload_to='members_images/'),
        ),
    ]