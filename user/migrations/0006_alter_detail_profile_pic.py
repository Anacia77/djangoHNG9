# Generated by Django 4.1.2 on 2023-01-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_detail_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='profile_pic',
            field=models.FileField(default='media/tem.png', null=True, upload_to=''),
        ),
    ]
