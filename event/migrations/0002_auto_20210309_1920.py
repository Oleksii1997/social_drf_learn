# Generated by Django 3.1.7 on 2021-03-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Назва події'),
        ),
    ]