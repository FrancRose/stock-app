# Generated by Django 4.1.1 on 2022-09-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, verbose_name='Symbol')),
                ('qty', models.CharField(max_length=10000, verbose_name='Quantity')),
            ],
        ),
    ]
