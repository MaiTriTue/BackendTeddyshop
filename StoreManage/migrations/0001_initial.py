# Generated by Django 4.1.4 on 2022-12-06 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(default='Admin', max_length=100)),
                ('admin_email', models.EmailField(max_length=100, null=True)),
                ('admin_phone', models.CharField(max_length=20, null=True)),
                ('admin_discription', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('discription', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('customer_address', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('total_amount', models.FloatField(null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('customer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Id', models.CharField(max_length=100)),
                ('amount_product', models.IntegerField(default=1)),
                ('create_date_order', models.CharField(max_length=100)),
                ('customer_orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreManage.order')),
            ],
            options={
                'ordering': ['id', 'create_date_order'],
            },
        ),
    ]