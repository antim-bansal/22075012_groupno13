# Generated by Django 4.2.6 on 2023-11-05 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InstiPro', '0021_student_result_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_result',
            name='status',
        ),
    ]
