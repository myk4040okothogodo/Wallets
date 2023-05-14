# Generated by Django 3.1.5 on 2023-04-14 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Wallet', '0002_wallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_wallet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='walletprofile',
            name='limit',
            field=models.PositiveSmallIntegerField(choices=[(1, 1000000), (2, 100000000), (0, 100000), (3, 9999999999.99)], default=1),
        ),
        migrations.AlterField(
            model_name='walletprofile',
            name='name',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Mini'), (2, 'Super'), (1, 'Regular')], default=1),
        ),
    ]