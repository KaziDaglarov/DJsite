# Generated by Django 4.1.4 on 2022-12-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
    ]
