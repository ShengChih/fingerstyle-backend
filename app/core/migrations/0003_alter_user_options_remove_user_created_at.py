# Generated by Django 4.0.8 on 2022-10-06 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'get_latest_by': 'id', 'ordering': ['-id'], 'verbose_name': '用戶', 'verbose_name_plural': '用戶'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
    ]