# Generated by Django 5.1.3 on 2024-12-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agora', '0004_remove_user_is_active_user_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]