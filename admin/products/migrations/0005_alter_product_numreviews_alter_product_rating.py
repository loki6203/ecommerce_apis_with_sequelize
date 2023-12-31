# Generated by Django 4.2.3 on 2023-07-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_numreviews_alter_review_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='numReviews',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
