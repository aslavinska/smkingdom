# Generated by Django 3.2.21 on 2023-09-22 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_customer_id',
        ),
    ]