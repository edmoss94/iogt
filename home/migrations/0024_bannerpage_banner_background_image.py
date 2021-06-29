# Generated by Django 3.1.12 on 2021-06-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0023_auto_20210629_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerpage',
            name='banner_background_image',
            field=models.ForeignKey(blank=True, help_text='Background image', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image'),
        ),
    ]
