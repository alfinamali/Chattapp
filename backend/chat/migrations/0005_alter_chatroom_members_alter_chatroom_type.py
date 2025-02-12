# Generated by Django 5.0.1 on 2024-06-14 12:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0004_channeldetail"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="members",
            field=models.ManyToManyField(
                null=True, related_name="chatrooms", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="chatroom",
            name="type",
            field=models.CharField(
                choices=[("D", "Direct Room"), ("G", "Group")],
                default="G",
                max_length=5,
            ),
        ),
    ]
