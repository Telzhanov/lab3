# Generated by Django 2.2 on 2019-04-30 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20190430_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
