# Generated by Django 4.0.2 on 2022-04-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_summer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=55)),
                ('gold', models.IntegerField()),
                ('silver', models.IntegerField()),
                ('bronze', models.IntegerField()),
                ('all', models.IntegerField()),
                ('place', models.IntegerField()),
            ],
        ),
    ]
