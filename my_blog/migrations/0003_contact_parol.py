# Generated by Django 4.2.3 on 2023-07-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='parol',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
