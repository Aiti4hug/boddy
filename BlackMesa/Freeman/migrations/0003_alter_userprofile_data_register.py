# Generated by Django 5.1.3 on 2024-12-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeman', '0002_alter_userprofile_age_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='data_register',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
