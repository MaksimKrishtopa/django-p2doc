# Generated by Django 4.2.7 on 2023-11-16 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_requestcategory_designrequest_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designrequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='RequestCategory',
        ),
        migrations.DeleteModel(
            name='DesignRequest',
        ),
    ]
