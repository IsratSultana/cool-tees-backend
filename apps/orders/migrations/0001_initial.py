# Generated by Django 4.2.2 on 2023-08-26 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(verbose_name='total_price')),
                ('customer_name', models.CharField(max_length=255, verbose_name='customer_name')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('building_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='building_type')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('state', models.CharField(max_length=255, verbose_name='state')),
                ('pin_code', models.CharField(max_length=255, verbose_name='pin_code')),
                ('total_qty', models.IntegerField(verbose_name='total_qty')),
                ('customer_phone', models.CharField(max_length=255, verbose_name='customer_phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
