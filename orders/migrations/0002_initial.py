# Generated by Django 4.1.7 on 2023-03-30 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='product_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.productunit'),
        ),
    ]
