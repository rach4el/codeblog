# Generated by Django 4.2.13 on 2024-05-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='admin_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
