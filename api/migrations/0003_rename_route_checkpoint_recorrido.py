# Generated by Django 3.2.3 on 2021-11-09 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211109_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkpoint',
            old_name='route',
            new_name='recorrido',
        ),
    ]