# Generated by Django 5.0.2 on 2024-03-23 17:53

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
            name='FirebaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('school', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GroupChats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=350)),
                ('image', models.ImageField(upload_to='')),
                ('isPrivate', models.BooleanField()),
                ('groupAdmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_of_groupchat', to=settings.AUTH_USER_MODEL)),
                ('groupMembers', models.ManyToManyField(related_name='groupchat_participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firebase_uid', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
