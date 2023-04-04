# Generated by Django 4.1.7 on 2023-03-30 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('post_index', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UnitBundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_price', models.IntegerField()),
                ('final_price', models.IntegerField()),
                ('availability', models.BooleanField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.currency')),
                ('delivery_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_bundles', to='shipping.deliverytype')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_bundles', to='shipping.platform')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_bundles', to='products.size')),
            ],
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='products.product')),
                ('unit_bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_units', to='shipping.unitbundle')),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moscow_del_price', models.IntegerField()),
                ('extra_charge_percentage', models.FloatField()),
                ('rounding_step', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('delivery_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.deliverytype')),
            ],
        ),
    ]