# Generated by Django 4.1.1 on 2022-09-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("position", models.CharField(max_length=50)),
                ("image", models.ImageField(null=True, upload_to="team/image")),
            ],
        ),
    ]
