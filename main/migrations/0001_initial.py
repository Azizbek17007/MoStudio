# Generated by Django 4.2.13 on 2024-06-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sarlavha', models.CharField(max_length=200)),
                ('mazmun', models.TextField()),
                ('rasm', models.ImageField(upload_to='blog/')),
                ('chop_etilgan_sana', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JamoaAzosi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ism', models.CharField(max_length=100)),
                ('lavozim', models.CharField(max_length=100)),
                ('rasm', models.ImageField(upload_to='jamoa/')),
                ('qisqa_tavsif', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loyiha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=200)),
                ('tavsif', models.TextField()),
                ('rasm', models.ImageField(upload_to='loyihalar/')),
                ('yaratildi_sana', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sharh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mijoz', models.CharField(max_length=100)),
                ('lavozim', models.CharField(blank=True, max_length=100, null=True)),
                ('izoh', models.TextField()),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='sharhlar/')),
                ('yaratildi_sana', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Xizmat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=100)),
                ('tavsif', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
