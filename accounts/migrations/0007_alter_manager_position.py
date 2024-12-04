# Generated by Django 5.1.3 on 2024-12-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_manager_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='position',
            field=models.CharField(choices=[('camping_seller', 'camping_seller'), ('grill_seller', 'grill_seller'), ('furniture_seller', 'furniture_seller')], default='furniture_seller', max_length=60),
        ),
    ]
