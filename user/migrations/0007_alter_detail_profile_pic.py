# Generated by Django 4.1.2 on 2023-01-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_detail_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='profile_pic',
            field=models.FileField(default='user.png', null=True, upload_to=''),
        ),
    ]
