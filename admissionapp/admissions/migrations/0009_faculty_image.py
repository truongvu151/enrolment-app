# Generated by Django 4.1.7 on 2023-05-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0008_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='faculties/%Y/%m/'),
        ),
    ]