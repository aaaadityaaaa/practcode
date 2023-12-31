# Generated by Django 3.2.4 on 2023-05-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeGpt_students', '0002_question_students_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='example',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='exp_inputs',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='exp_outputs',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='expected',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='testcases',
            field=models.CharField(max_length=100),
        ),
    ]
