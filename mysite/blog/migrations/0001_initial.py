# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
