# Generated by Django 4.2.13 on 2024-05-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Suggested_Riding_Ability',
            field=models.IntegerField(choices=[(0, 'All Abilities'), (1, 'Beginner'), (2, 'Novice'), (3, 'Intermidiate'), (4, 'Advanced')], default=0),
        ),
    ]
