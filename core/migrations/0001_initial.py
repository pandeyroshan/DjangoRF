# Generated by Django 2.1.5 on 2019-09-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataID', models.IntegerField()),
                ('data', models.CharField(max_length=100)),
            ],
        ),
    ]
