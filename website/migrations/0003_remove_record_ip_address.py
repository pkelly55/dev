# Generated by Django 5.0 on 2024-01-01 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_record_ip_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="record",
            name="ip_address",
        ),
    ]