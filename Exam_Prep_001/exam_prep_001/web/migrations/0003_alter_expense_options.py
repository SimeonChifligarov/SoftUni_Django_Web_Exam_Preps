# Generated by Django 4.0.2 on 2022-02-27 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_expense'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('title', 'price')},
        ),
    ]