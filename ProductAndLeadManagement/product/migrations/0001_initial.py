# Generated by Django 5.1.1 on 2024-09-09 13:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.CharField(max_length=20)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('Products', models.ManyToManyField(to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
