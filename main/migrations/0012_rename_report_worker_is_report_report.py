# Generated by Django 4.2.1 on 2023-08-08 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_message_user_remove_message_worker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='report',
            new_name='is_report',
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('reported_by', models.CharField(max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.worker')),
            ],
        ),
    ]
