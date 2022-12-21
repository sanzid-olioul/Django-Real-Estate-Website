# Generated by Django 4.1.4 on 2022-12-21 16:12

import blog.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('agent', '0003_messages_is_checked_messages_property_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('comment_body', models.TextField()),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agentprofile')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.models.blog_directory_path)),
                ('title', models.CharField(max_length=500)),
                ('catagory', models.CharField(choices=[('travel', 'Travel'), ('food', 'Food'), ('it', 'IT')], max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.agentprofile')),
            ],
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['content_type', 'object_id'], name='blog_commen_content_b11109_idx'),
        ),
    ]
