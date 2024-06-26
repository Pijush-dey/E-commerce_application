# Generated by Django 4.0.6 on 2024-05-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': "Customer's Info",
                'verbose_name_plural': "Customer's Info",
            },
        ),
    ]
