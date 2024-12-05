# Generated by Django 5.1.3 on 2024-11-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manager",
            name="position",
            field=models.CharField(choices=[("grill_seller", "grill_seller"), ("camping_seller", "camping_seller"), ("furniture_seller", "furniture_seller")], default="furniture_seller", max_length=60),
        ),
    ]
