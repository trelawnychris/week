# Generated by Django 3.0.4 on 2020-04-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0004_auto_20200429_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]