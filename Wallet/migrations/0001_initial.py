# Generated by Django 3.1.5 on 2023-04-14 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_available', models.DecimalField(decimal_places=2, default=0.0, max_digits=11)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalletProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(2, 'Super'), (1, 'Regular'), (0, 'Mini')], default=1)),
                ('limit', models.PositiveSmallIntegerField(choices=[(3, 9999999999.99), (2, 100000000), (0, 100000), (1, 1000000)], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_profile', to='Wallet.wallet')),
            ],
        ),
    ]
