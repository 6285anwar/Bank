# Generated by Django 4.1.7 on 2023-03-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_data_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_form',
            name='dateofbirth',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
