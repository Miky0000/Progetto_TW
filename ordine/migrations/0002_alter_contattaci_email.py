# Generated by Django 4.0 on 2023-05-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contattaci',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]