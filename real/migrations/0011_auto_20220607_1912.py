# Generated by Django 2.2 on 2022-06-07 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0010_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL),
        ),
    ]