# Generated by Django 5.0 on 2024-01-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("zipcode", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
