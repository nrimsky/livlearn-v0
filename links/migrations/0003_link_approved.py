# Generated by Django 3.1.7 on 2021-03-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20210313_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
