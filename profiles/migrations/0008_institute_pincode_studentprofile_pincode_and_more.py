# Generated by Django 4.2.1 on 2023-07-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_studentprofile_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='Pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='Pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
    ]
