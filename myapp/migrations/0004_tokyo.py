# Generated by Django 4.0.2 on 2022-04-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_menprize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tokyo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=55)),
                ('sport', models.CharField(max_length=55)),
                ('category', models.CharField(max_length=55)),
                ('medal', models.CharField(max_length=55)),
            ],
        ),
    ]