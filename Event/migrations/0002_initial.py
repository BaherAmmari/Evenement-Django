# Generated by Django 4.1 on 2023-02-10 14:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation_event',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participation',
            field=models.ManyToManyField(related_name='participations', through='Event.participation_event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='participation_event',
            unique_together={('person', 'event')},
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gte', datetime.datetime(2023, 2, 10, 15, 52, 58, 571003))), name='Please check the event date!'),
        ),
    ]