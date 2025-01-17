# Generated by Django 5.1.1 on 2024-09-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title_tr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
