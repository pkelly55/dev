# Generated by Django 4.2.5 on 2024-02-26 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0013_cpu_load"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cpu_load",
            name="dataSaved",
        ),
        migrations.RemoveField(
            model_name="cpu_load",
            name="unique",
        ),
        migrations.RemoveField(
            model_name="record",
            name="file",
        ),
        migrations.RemoveField(
            model_name="record",
            name="title",
        ),
    ]
