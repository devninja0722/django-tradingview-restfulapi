# Generated by Django 3.2.9 on 2021-12-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_count_walletitem_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='walletitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
