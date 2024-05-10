# Generated by Django 5.0.6 on 2024-05-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='profile_picture',
            field=models.ImageField(default='image.jpg', upload_to='uploads/', verbose_name='Profile Picture'),
            preserve_default=False,
        ),
    ]
