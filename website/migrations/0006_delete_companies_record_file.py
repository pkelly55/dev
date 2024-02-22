# Generated by Django 4.2.5 on 2024-01-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_rename_business_companies"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Companies",
        ),
        migrations.AddField(
            model_name="record",
            name="file",
            field=models.FileField(null=True, upload_to="files/", verbose_name=""),
        ),
    ]
