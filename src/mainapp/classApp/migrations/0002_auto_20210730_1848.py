# Generated by Django 2.1.5 on 2021-07-31 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classapp',
            name='duration',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
    ]
