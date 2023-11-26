# Generated by Django 4.1.7 on 2023-11-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("city_population", models.IntegerField(default=0)),
            ],
        ),
    ]
