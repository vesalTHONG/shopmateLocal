# Generated by Django 3.1 on 2022-11-15 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='craeted_date',
            new_name='created_date',
        ),
    ]
