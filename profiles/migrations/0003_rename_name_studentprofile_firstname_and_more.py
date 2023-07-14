# Generated by Django 4.2.1 on 2023-07-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_studentprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='lastName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
