# Generated by Django 4.1.4 on 2022-12-22 13:39

import about.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0003_messages_is_checked_messages_property_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllSocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('established_on', about.models.RangeIntegerField(validators=[django.core.validators.MinValueValidator(1990), django.core.validators.MaxValueValidator(2022)])),
                ('working_fielsd', models.CharField(max_length=250)),
                ('featured_photo', models.ImageField(upload_to='')),
                ('speech', models.TextField()),
                ('ceo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agent.agentprofile')),
            ],
        ),
    ]
