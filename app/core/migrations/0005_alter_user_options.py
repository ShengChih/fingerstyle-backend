# Generated by Django 4.0.8 on 2022-10-06 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'get_latest_by': 'id', 'ordering': ['-id'], 'verbose_name': '用戶', 'verbose_name_plural': '用戶'},
        ),
    ]