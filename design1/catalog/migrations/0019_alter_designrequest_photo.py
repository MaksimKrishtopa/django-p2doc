# Generated by Django 4.2.7 on 2023-11-20 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_remove_designrequest_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designrequest',
            name='photo',
            field=models.ImageField(null=True, upload_to='design_photos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])]),
        ),
    ]
