# Generated by Django 4.2.5 on 2024-02-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0012_monitor"),
    ]

    operations = [
        migrations.CreateModel(
            name="CPU_load",
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
                ("cpu_usage", models.FloatField()),
                ("ram_usage", models.FloatField()),
                ("totalSiteVisits", models.IntegerField()),
                ("unique", models.IntegerField()),
                ("dataSaved", models.IntegerField()),
                ("now", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
