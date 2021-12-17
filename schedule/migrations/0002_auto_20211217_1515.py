# Generated by Django 3.1.7 on 2021-12-17 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('number_of_seats', models.IntegerField(blank=True, null=True)),
                ('price_per_place', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Opponents will be known soon', max_length=200)),
                ('date', models.DateTimeField()),
                ('viewers', models.IntegerField(blank=True, null=True)),
                ('result', models.CharField(blank=True, default="Game doesn't started yet", max_length=200, null=True)),
                ('players', models.ManyToManyField(blank=True, max_length=11, null=True, to='schedule.Player')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.stadium')),
            ],
        ),
    ]
