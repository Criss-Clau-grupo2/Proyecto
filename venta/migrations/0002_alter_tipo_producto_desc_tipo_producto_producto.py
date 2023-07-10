# Generated by Django 4.1.2 on 2023-05-31 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_producto',
            name='desc_tipo_producto',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idTipoProducto', primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=40)),
                ('precio_producto', models.IntegerField()),
                ('stock_producto', models.IntegerField()),
                ('desc_producto', models.CharField(max_length=60)),
                ('id_tipo_producto', models.ForeignKey(db_column='id_tipo_producto', on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_producto')),
            ],
        ),
    ]