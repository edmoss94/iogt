# Generated by Django 3.1.13 on 2021-07-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210707_0702'),
        ('iogt_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='read_articles',
            field=models.ManyToManyField(to='home.Article'),
        ),
    ]
