# Generated by Django 2.2.3 on 2019-07-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=999999999999)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
