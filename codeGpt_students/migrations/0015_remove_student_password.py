# Generated by Django 4.2 on 2023-06-13 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeGpt_students', '0014_student__tempotp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]