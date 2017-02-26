# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='content_ru',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='description_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='description_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
    ]
