# Generated by Django 4.0 on 2021-12-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('health_status', models.CharField(max_length=300)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]