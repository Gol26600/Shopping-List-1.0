# Generated by Django 3.1.3 on 2020-11-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20201123_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('g', 'g'), ('lbs', 'lbs')], max_length=30, null=True),
        ),
    ]