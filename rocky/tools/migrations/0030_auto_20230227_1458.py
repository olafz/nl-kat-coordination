# Generated by Django 3.2.18 on 2023-02-27 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tools", "0029_set_user_full_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organizationmember",
            name="authorized",
        ),
        migrations.RemoveField(
            model_name="organizationmember",
            name="member_name",
        ),
        migrations.RemoveField(
            model_name="organizationmember",
            name="verified",
        ),
        migrations.AlterField(
            model_name="organizationmember",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="members", to="tools.organization"
            ),
        ),
        migrations.AlterField(
            model_name="organizationmember",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
