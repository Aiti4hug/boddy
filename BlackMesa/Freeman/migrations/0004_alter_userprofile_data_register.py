# Generated by Django 5.1.3 on 2024-12-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeman', '0003_alter_userprofile_data_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='data_register',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
