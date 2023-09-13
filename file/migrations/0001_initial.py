# Generated by Django 4.2.3 on 2023-09-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(upload_to='images')),
                ('specs', models.FileField(upload_to='documents')),
            ],
        ),
    ]
