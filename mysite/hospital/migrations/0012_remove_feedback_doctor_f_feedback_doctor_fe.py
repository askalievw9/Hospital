# Generated by Django 5.1.5 on 2025-02-04 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_remove_feedback_doctor_feedback_doctor_f'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='doctor_f',
        ),
        migrations.AddField(
            model_name='feedback',
            name='doctor_fe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_fe', to='hospital.doctor'),
            preserve_default=False,
        ),
    ]
