# Generated by Django 4.2.13 on 2024-05-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0002_alter_createpost_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createpost',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Suggestion Posts'},
        ),
        migrations.RenameField(
            model_name='createpost',
            old_name='Creator',
            new_name='creator',
        ),
    ]
