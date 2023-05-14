# Generated by Django 3.1.5 on 2023-04-14 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transanction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransanctionProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transanction_category', models.PositiveSmallIntegerField(choices=[(0, '< 100,000'), (1, '> 100,000'), (3, '> 1,000,000'), (4, '> 1,000,000'), (2, '< 1,000,000')], default=0)),
                ('transanction_type', models.PositiveSmallIntegerField(choices=[(0, 'AFRICA'), (2, 'WORLD'), (1, 'KENYA')], default=1)),
                ('transanction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transanction_profile', to='Transanctions.transanction')),
            ],
        ),
    ]