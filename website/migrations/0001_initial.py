# Generated by Django 5.0 on 2023-12-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('actueel', models.BooleanField(default=False)),
                ('project', models.CharField(max_length=100)),
                ('opdrachtgever', models.CharField(max_length=100)),
                ('tonnage', models.IntegerField()),
                ('bodemas_perc', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=1000)),
                ('slagingskans', models.CharField(max_length=3)),
                ('planning', models.CharField(max_length=20)),
                ('actiehouder', models.CharField(max_length=2)),
                ('actie', models.CharField(max_length=1000)),
            ],
        ),
    ]
