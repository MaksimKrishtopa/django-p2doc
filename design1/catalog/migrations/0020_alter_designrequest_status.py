# Generated by Django 4.2.7 on 2023-11-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_designrequest_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designrequest',
            name='status',
            field=models.CharField(choices=[('Н', 'Новая'), ('П', 'Принято в работу'), ('В', 'Выполнено')], default='Н', max_length=20),
        ),
    ]
