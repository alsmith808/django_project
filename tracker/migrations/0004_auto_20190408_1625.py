# Generated by Django 2.2 on 2019-04-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20190407_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('RQ', 'Requested'), ('TD', 'Todo'), ('FX', 'Fixed')], default='TD', max_length=2),
        ),
    ]
