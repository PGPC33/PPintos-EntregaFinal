# Generated by Django 5.1.1 on 2024-09-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_alter_post_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemaPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
