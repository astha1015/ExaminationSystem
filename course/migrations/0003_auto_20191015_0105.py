# Generated by Django 2.2.6 on 2019-10-15 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20191015_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='course_name',
        ),
    ]
