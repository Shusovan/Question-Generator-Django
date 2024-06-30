# Generated by Django 5.0.6 on 2024-06-22 13:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='', verbose_name='docs/')),
                ('type', models.CharField(choices=[('pdf', 'pdf')], default='pdf', max_length=100)),
                ('row_created', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
    ]
