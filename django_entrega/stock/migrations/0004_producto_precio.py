# Generated by Django 4.2.7 on 2023-11-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_producto_precio_alter_producto_color_luz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
