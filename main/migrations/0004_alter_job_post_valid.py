# Generated by Django 4.2.1 on 2023-07-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_worker_cv_alter_worker_exp_proof_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='valid',
            field=models.BooleanField(null=True),
        ),
    ]
