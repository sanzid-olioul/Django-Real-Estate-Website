# Generated by Django 4.1.4 on 2022-12-19 07:04

import agent.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_photo', models.ImageField(default='logo/profile.png', upload_to=agent.models.user_directory_path)),
                ('about', models.TextField()),
                ('phone', models.CharField(max_length=14)),
                ('mobile', models.CharField(max_length=14)),
                ('facebook', models.URLField(max_length=150)),
                ('twitter', models.URLField(max_length=150)),
                ('instagram', models.URLField(max_length=150)),
                ('linkedin', models.URLField(max_length=150)),
            ],
        ),
    ]
