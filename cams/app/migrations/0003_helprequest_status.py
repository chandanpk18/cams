# Generated by Django 5.0.2 on 2024-05-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Resolved', 'Resolved')], default='New', max_length=10),
        ),
    ]