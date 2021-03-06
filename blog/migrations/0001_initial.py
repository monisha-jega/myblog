# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-15 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=50)),
                ('user_pass', models.CharField(max_length=20)),
                ('user_actname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
