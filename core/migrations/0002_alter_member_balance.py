# Generated by Django 4.2.1 on 2023-05-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
