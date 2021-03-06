# Generated by Django 3.2.7 on 2021-09-19 09:44

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('private', models.BooleanField(default=False)),
                ('image', models.FileField(upload_to='')),
                ('times_shared', models.IntegerField(default=0)),
                ('size', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
