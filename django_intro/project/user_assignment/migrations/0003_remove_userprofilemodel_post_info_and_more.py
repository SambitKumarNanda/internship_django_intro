# Generated by Django 4.2 on 2023-06-07 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_assignment", "0002_userpostmodel_alter_usermodel_contact_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofilemodel", name="post_info",),
        migrations.AddField(
            model_name="userpostmodel",
            name="user_detail_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_post_model_post_info",
                to="user_assignment.userprofilemodel",
            ),
        ),
    ]
