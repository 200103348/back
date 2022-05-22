# Generated by Django 4.0.2 on 2022-04-28 19:31

from django.db import migrations, models
import myapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myvideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcountry', models.CharField(max_length=50)),
                ('mtext', models.TextField(max_length=5000)),
                ('msportsmen', models.CharField(max_length=50)),
                ('mcaption', models.CharField(max_length=100)),
                ('mvideo', models.FileField(upload_to='video/%y', validators=[myapp.validators.file_size])),
            ],
        ),
    ]
