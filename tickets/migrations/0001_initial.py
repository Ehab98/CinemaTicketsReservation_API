# Generated by Django 4.0.1 on 2022-01-10 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=50)),
                ('movie', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='tickets.guest')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='tickets.movie')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
