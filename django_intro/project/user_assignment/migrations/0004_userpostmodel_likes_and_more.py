# Generated by Django 4.2 on 2023-06-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_assignment", "0003_remove_userprofilemodel_post_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userpostmodel",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                related_name="user_post_likes",
                to="user_assignment.usermodel",
            ),
        ),
        migrations.RemoveField(model_name="userprofilemodel", name="followers",),
        migrations.RemoveField(model_name="userprofilemodel", name="following",),
        migrations.AddField(
            model_name="userprofilemodel",
            name="followers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="user_profile_followers",
                to="user_assignment.usermodel",
            ),
        ),
        migrations.AddField(
            model_name="userprofilemodel",
            name="following",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="user_profile_following",
                to="user_assignment.usermodel",
            ),
        ),
    ]
