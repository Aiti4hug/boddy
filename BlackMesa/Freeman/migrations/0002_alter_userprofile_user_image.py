# Generated by Django 5.1.3 on 2024-12-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]