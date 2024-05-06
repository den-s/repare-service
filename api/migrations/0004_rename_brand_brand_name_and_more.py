# Generated by Django 4.2.10 on 2024-03-10 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_order_client_delete_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='devicetype',
            old_name='device_type',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='orderstatus',
            old_name='status',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.brand'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.devicetype'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='device', to='api.device'),
        ),
        migrations.AlterField(
            model_name='order',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='replacement_parts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.replacementpart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.orderstatus', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker', to=settings.AUTH_USER_MODEL),
        ),
    ]
