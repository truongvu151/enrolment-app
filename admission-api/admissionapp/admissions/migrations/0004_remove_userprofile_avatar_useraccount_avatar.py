# Generated by Django 4.1.7 on 2023-05-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_remove_banner_slug_remove_major_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(null=True, upload_to='users/%Y/%m'),
        ),
    ]
