# Generated by Django 4.0.6 on 2022-07-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_addproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
