# Generated by Django 4.2.7 on 2023-11-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_designrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fio',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
    ]
