# Generated by Django 4.1.5 on 2023-04-19 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_about_alter_product_description_and_more'),
        ('wishes', '0004_wish_productwished_wish_wishowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='productWished',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='products.product'),
        ),
    ]
