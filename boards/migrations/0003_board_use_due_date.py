# Generated by Django 3.1 on 2020-09-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='use_due_date',
            field=models.BooleanField(default=False),
        ),
    ]