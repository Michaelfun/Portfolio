# Generated by Django 4.2.6 on 2023-11-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_me_bio_alter_me_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.AddField(
            model_name='service',
            name='descript',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
