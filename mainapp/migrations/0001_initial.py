# Generated by Django 4.0.2 on 2022-06-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=30)),
                ('stock_price', models.FloatField()),
            ],
        ),
    ]
