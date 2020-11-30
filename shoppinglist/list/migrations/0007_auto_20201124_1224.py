# Generated by Django 3.1.3 on 2020-11-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_auto_20201124_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('g', 'g'), ('lbs', 'lbs'), ('liters', 'liters'), ('ml', 'ml')], max_length=30, null=True),
        ),
    ]