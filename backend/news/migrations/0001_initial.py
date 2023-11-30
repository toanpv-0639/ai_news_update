# Generated by Django 4.0.1 on 2023-11-30 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=1000)),
                ('source', models.CharField(max_length=1000)),
                ('is_summary', models.BooleanField(default=False)),
                ('is_send', models.BooleanField(default=False)),
                ('is_valid', models.BooleanField(default=True)),
                ('crawled_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('sent_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('thresh_id', models.CharField(max_length=100)),
                ('channel_name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.thread')),
            ],
        ),
    ]