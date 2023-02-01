# Generated by Django 4.1.5 on 2023-02-01 13:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color1', models.CharField(max_length=50)),
                ('color2', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('creation_date', models.DateField(default=datetime.datetime.now)),
                ('photo', models.ImageField(upload_to='images/')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('initial_stock', models.IntegerField()),
                ('current_stock', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=100)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('talla', models.CharField(max_length=4)),
                ('tejido', models.CharField(max_length=50)),
                ('tallaje', models.CharField(max_length=50)),
                ('mangas', models.BooleanField(default=True, null=True)),
            ],
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='Gorra',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('color_logo', models.CharField(max_length=50)),
            ],
            bases=('products.product',),
        ),
    ]
