# Generated by Django 5.1.1 on 2024-09-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_temapost_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.CharField(max_length=500)),
            ],
        ),
    ]
