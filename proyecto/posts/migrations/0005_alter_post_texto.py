# Generated by Django 5.1.1 on 2024-09-29 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.TextField(max_length=500),
        ),
    ]
