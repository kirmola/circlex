# Generated by Django 5.0.6 on 2024-05-09 01:34

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_post_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=10, max_length=10, prefix='', primary_key=True, serialize=False, verbose_name='Comment ID')),
                ('comment_detail', models.TextField(max_length=500, verbose_name='Comment')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Posted on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Posted on')),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post', verbose_name='Commented on')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]