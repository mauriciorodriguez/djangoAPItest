# Generated by Django 3.2.3 on 2021-11-13 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_checkpoint_recorrido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpoint',
            name='nivel_cota',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='viento',
            field=models.CharField(max_length=50),
        ),
    ]