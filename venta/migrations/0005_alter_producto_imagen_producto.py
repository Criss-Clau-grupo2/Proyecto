# Generated by Django 4.1.2 on 2023-07-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_remove_detalle_boleta_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
