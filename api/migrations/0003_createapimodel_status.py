# Generated by Django 3.2.5 on 2021-08-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_createapimodel_trigger'),
    ]

    operations = [
        migrations.AddField(
            model_name='createapimodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
