# Generated by Django 4.2.2 on 2023-08-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('password', models.CharField(max_length=255, verbose_name='password')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('token', models.CharField(max_length=500, verbose_name='token')),
                ('token_expires_at', models.DateTimeField(verbose_name='token_expires_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
        ),
    ]
