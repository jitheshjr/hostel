# Generated by Django 5.0.6 on 2024-06-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_alter_student_year_alter_trash_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
