# Generated by Django 4.2.1 on 2023-06-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='is_approved',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='report',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
