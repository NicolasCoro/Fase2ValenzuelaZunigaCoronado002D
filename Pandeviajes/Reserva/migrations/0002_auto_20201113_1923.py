# Generated by Django 3.1.2 on 2020-11-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantP',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telef',
            field=models.IntegerField(default=0),
        ),
    ]