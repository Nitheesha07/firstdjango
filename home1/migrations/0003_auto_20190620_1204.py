# Generated by Django 2.2.2 on 2019-06-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_name',
            field=models.CharField(help_text='student name', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(help_text='Book Name ', max_length=100, null=True),
        ),
    ]