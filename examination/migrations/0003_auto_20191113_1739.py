# Generated by Django 2.2.5 on 2019-11-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_auto_20191113_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoice',
            name='potential_answer',
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='potential_answer',
            field=models.ManyToManyField(blank=True, to='examination.PotentialAnswer'),
        ),
    ]