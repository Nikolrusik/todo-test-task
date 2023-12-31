# Generated by Django 4.2.3 on 2023-07-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('completed', models.BooleanField(default=False, verbose_name='completed')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
        ),
    ]
