# Generated by Django 4.1.5 on 2023-04-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stripe_id',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]