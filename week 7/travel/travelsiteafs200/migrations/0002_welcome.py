# Generated by Django 3.1.4 on 2021-01-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsiteafs200', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h2', models.CharField(max_length=50)),
                ('h1', models.CharField(max_length=50)),
                ('p', models.TextField()),
                ('a1', models.CharField(max_length=50)),
                ('a2', models.CharField(max_length=50)),
            ],
        ),
    ]
