# Generated by Django 2.2 on 2022-06-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0003_remove_agent_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]