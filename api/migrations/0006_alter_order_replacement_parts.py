# Generated by Django 4.2.10 on 2024-03-21 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_order_replacement_parts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='replacement_parts',
            field=models.ManyToManyField(blank=True, to='api.replacementpart'),
        ),
    ]
