# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20171110_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('content', models.TextField()),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('editor', models.IntegerField()),
                ('is_main', models.BooleanField()),
                ('pos_eva_count', models.IntegerField(default=0)),
                ('neg_eva_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Follow_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('follow_id', models.IntegerField()),
                ('to_comment_id', models.IntegerField(null=True)),
                ('content', models.TextField()),
                ('post_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow_Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('follow_id', models.IntegerField()),
                ('grade', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('category', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('main_follow_id', models.IntegerField()),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('follow_count', models.IntegerField(default=0)),
                ('click_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='elective',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(max_length=100, null=True),
        ),

    ]