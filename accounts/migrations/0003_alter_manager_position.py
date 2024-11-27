# Generated by Django 5.1.3 on 2024-11-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_manager_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='position',
            field=models.CharField(choices=[('furniture_seller', 'furniture_seller'), ('grill_seller', 'grill_seller'), ('camping_seller', 'camping_seller')], default='furniture_seller', max_length=60),
        ),
    ]
