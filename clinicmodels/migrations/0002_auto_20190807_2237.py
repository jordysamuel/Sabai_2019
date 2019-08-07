# Generated by Django 2.2.4 on 2019-08-07 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicmodels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 22, 37, 17, 237579)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='picture_blob',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='postreferral',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 22, 37, 17, 237579)),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 22, 37, 17, 236555)),
        ),
    ]