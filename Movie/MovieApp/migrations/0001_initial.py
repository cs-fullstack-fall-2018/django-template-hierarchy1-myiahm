# Generated by Django 2.0.6 on 2018-10-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('yearReleased', models.CharField(max_length=4)),
                ('ageAllowed', models.CharField(max_length=2)),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
    ]
