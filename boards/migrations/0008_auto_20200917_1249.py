# Generated by Django 3.1 on 2020-09-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
