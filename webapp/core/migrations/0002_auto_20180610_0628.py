# Generated by Django 2.0.6 on 2018-06-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlog',
            name='read_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='serverlog',
            name='write_amount',
            field=models.IntegerField(null=True),
        ),
    ]
