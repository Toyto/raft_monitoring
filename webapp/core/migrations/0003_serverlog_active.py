# Generated by Django 2.0.6 on 2018-06-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180610_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverlog',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
