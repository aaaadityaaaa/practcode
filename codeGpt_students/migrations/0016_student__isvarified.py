# Generated by Django 4.2 on 2023-06-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeGpt_students', '0015_remove_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='_isVarified',
            field=models.BooleanField(default=False),
        ),
    ]
