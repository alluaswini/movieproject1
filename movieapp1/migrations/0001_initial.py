# Generated by Django 3.0.4 on 2020-04-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('year_released', models.IntegerField()),
                ('desc', models.IntegerField()),
                ('image', models.CharField(max_length=50)),
            ],
        ),
    ]
