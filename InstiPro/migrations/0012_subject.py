# Generated by Django 4.2.6 on 2023-10-31 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InstiPro', '0011_rename_student_email_staff_staff_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstiPro.course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstiPro.staff')),
            ],
        ),
    ]
