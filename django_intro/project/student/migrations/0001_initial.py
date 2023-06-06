# Generated by Django 4.2 on 2023-06-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentDetailModel",
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
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.IntegerField(unique=True)),
                ("year_of_joining", models.DateField()),
                ("branch", models.CharField(max_length=3)),
                ("dob", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
