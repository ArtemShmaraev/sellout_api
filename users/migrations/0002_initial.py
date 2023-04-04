# Generated by Django 4.1.7 on 2023-03-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(related_name='users', to='wishlist.wishlist'),
        ),
    ]
