# Generated by Django 5.1.3 on 2024-11-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fofumapi', '0004_alter_opportunity_liquidity'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalapi',
            name='access',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
