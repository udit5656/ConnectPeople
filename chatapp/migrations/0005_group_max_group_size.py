# Generated by Django 3.1 on 2020-08-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_group_group_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='max_group_size',
            field=models.IntegerField(default=20),
        ),
    ]
