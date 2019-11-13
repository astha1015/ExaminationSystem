# Generated by Django 2.2.5 on 2019-11-12 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('role', models.CharField(default='S', max_length=1)),
                ('country', models.CharField(blank=True, default='United States', max_length=40)),
                ('state', models.CharField(blank=True, default='Louisiana', max_length=40)),
                ('city', models.CharField(blank=True, default='New Orleans', max_length=40)),
                ('bio', models.CharField(blank=True, default='Enter a Bio', max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]