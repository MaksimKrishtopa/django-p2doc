# Generated by Django 4.2.7 on 2023-11-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_designrequest_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designrequest',
            name='image',
            field=models.ImageField(null=True, upload_to='design_images/'),
        ),
    ]
