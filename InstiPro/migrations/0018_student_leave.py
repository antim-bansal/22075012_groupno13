# Generated by Django 4.2.6 on 2023-11-03 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InstiPro', '0017_staff_notification_message_staff_notification_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=100, null=True)),
                ('end_date', models.CharField(max_length=100, null=True)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstiPro.student')),
            ],
        ),
    ]
