import ckeditor.fields
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='信箱')),
                ('name', models.CharField(max_length=255, verbose_name='暱稱')),

                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=core.models.avatar_image_file_path, verbose_name='頭貼')),
                ('gender', models.CharField(choices=[('MALE', '男生'), ('FEMALE', '女生'), ('OTHER', '其他')], default='OTHER', max_length=6, verbose_name='性別')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='簡介')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('country', django_countries.fields.CountryField(default='TW', max_length=2, verbose_name='國家/地區')),
                ('guitar_brand', models.CharField(blank=True, max_length=20, null=True, verbose_name='吉他品牌')),
                ('guitar_model', models.CharField(blank=True, max_length=20, null=True, verbose_name='吉他型號')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),

            ],
        ),
    ]
