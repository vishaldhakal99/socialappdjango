# Generated by Django 3.0.5 on 2020-05-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='profile',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='temporary_address',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
