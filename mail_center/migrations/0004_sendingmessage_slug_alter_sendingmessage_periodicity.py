# Generated by Django 5.0.6 on 2024-06-16 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_center', '0003_resultssendmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendingmessage',
            name='slug',
            field=models.SlugField(default=None, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sendingmessage',
            name='periodicity',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=60), 'Каждые 1 минуту'), (datetime.timedelta(seconds=900), 'Каждые 15 минут'), (datetime.timedelta(seconds=1800), 'Каждый 30 минут'), (datetime.timedelta(seconds=3600), 'Каждый 1 час'), (datetime.timedelta(seconds=7200), 'Каждые 2 часа'), (datetime.timedelta(seconds=10800), 'Каждые 3 часа'), (datetime.timedelta(seconds=14400), 'Каждые 4 часа'), (datetime.timedelta(seconds=18000), 'Каждые 5 часов'), (datetime.timedelta(seconds=21600), 'Каждые 6 часов'), (datetime.timedelta(seconds=43200), 'Каждые 12 часов'), (datetime.timedelta(days=1), 'Каждые 1 сутки'), (datetime.timedelta(days=2), 'Каждые 2 суток'), (datetime.timedelta(days=3), 'Каждые 3 суток'), (datetime.timedelta(days=4), 'Каждые 4 суток'), (datetime.timedelta(days=5), 'Каждые 5 суток'), (datetime.timedelta(days=6), 'Каждые 6 суток'), (datetime.timedelta(days=7), 'Каждую 1 неделю'), (datetime.timedelta(days=14), 'Каждые 2 недели'), (datetime.timedelta(days=21), 'Каждые 3 недели'), (datetime.timedelta(days=30), 'Каждый 1 месяц'), (datetime.timedelta(days=60), 'Каждые 2 месяца'), (datetime.timedelta(days=90), 'Каждые 3 месяца'), (datetime.timedelta(days=120), 'Каждые 4 месяца'), (datetime.timedelta(days=150), 'Каждые 5 месяцев'), (datetime.timedelta(days=180), 'Каждые 6 месяцев'), (datetime.timedelta(days=360), 'Каждый 12 месяцев')], default=(datetime.timedelta(seconds=43200), 'Каждые 12 часов'), verbose_name='периодичность отправки'),
        ),
    ]
