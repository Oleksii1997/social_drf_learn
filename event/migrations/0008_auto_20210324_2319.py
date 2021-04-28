# Generated by Django 3.1.7 on 2021-03-24 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210313_2246'),
        ('event', '0007_event_format_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile', verbose_name='Організатор'),
        ),
    ]