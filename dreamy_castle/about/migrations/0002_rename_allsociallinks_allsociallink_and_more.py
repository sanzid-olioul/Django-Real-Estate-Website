# Generated by Django 4.1.4 on 2022-12-22 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllSocialLinks',
            new_name='AllSocialLink',
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'about us'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'contact us'},
        ),
    ]