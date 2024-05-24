# Generated by Django 4.2.13 on 2024-05-23 22:00

import cloudinary.models
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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('suggested_riding_ability', models.IntegerField(choices=[(0, 'All Abilities'), (1, 'Beginner'), (2, 'Novice'), (3, 'Intermediate'), (4, 'Advanced')], default=0)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('excerpt', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_poster', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]