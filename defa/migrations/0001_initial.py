# Generated by Django 3.0.8 on 2020-08-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('thum', models.FileField(default=None, upload_to='books/thum/')),
                ('pdf', models.FileField(default=None, upload_to='books/pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.FileField(default=None, upload_to='videos/pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='UploadedVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100)),
                ('video_path', models.CharField(max_length=500)),
                ('video_thum', models.FileField(default=None, upload_to='output/thumb/')),
            ],
        ),
    ]
