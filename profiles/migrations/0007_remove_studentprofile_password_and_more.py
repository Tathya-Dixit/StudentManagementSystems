# Generated by Django 4.2.1 on 2023-07-14 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_studentprofile_institute_studentprofile_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='password',
        ),
    ]