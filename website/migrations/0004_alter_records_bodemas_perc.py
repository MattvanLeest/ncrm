# Generated by Django 5.0 on 2023-12-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_records_bodemas_perc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='bodemas_perc',
            field=models.IntegerField(),
        ),
    ]
