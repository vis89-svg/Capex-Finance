# Generated by Django 5.1 on 2024-09-02 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='amount',
        ),
    ]
