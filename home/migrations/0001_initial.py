# Generated by Django 3.0.5 on 2021-01-01 18:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('position', models.CharField(max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000, null=True)),
                ('supplier_name', models.CharField(max_length=10000, null=True)),
                ('cell_phone', models.CharField(max_length=10000, null=True)),
                ('contract_no', models.CharField(max_length=10000, null=True)),
                ('types_of_security', models.CharField(max_length=10000, null=True)),
                ('form_of_Security', models.CharField(max_length=10000, null=True)),
                ('issuing_bank', models.CharField(max_length=100000, null=True)),
                ('Reference_no', models.CharField(max_length=10000, null=True)),
                ('issuing_date', models.DateField()),
                ('extend_remindat', models.DateField()),
                ('last_remindat', models.DateField()),
                ('expiry_date', models.DateField()),
                ('amount', models.CharField(max_length=10000000, null=True)),
                ('extended', models.IntegerField(default=0)),
                ('daysleft', models.CharField(max_length=10000, null=True)),
                ('remark', models.CharField(max_length=1000, null=True)),
                ('user', models.ManyToManyField(blank=True, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
