# Generated by Django 3.1 on 2020-09-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_board_use_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]