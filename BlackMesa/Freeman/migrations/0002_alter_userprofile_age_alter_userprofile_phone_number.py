# Generated by Django 5.1.3 on 2024-12-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Freeman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
