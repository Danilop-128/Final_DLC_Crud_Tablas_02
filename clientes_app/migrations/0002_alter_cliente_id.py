# Generated by Django 5.1 on 2024-11-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.PositiveSmallIntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
