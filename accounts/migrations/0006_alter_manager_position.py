# Generated by Django 5.1.3 on 2024-12-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_manager_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='position',
            field=models.CharField(choices=[('grill_seller', 'grill_seller'), ('furniture_seller', 'furniture_seller'), ('camping_seller', 'camping_seller')], default='furniture_seller', max_length=60),
        ),
    ]