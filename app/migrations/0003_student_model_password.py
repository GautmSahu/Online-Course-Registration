# Generated by Django 3.0.5 on 2020-07-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_model',
            name='password',
            field=models.CharField(default=None, max_length=50),
        ),
    ]