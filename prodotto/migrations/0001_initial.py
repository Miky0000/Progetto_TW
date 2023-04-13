# Generated by Django 4.1.6 on 2023-04-12 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('DR', 'DUE RUOTE'), ('TR', 'TRE RUOTE'), ('QR', 'QUATTRO RUOTE'), ('AL', 'ALTRO')], default='AL', max_length=2)),
                ('titolo', models.CharField(max_length=100)),
                ('id_prodotto', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
                ('img', models.ImageField(upload_to='images/')),
                ('descrizione', models.CharField(max_length=1000)),
                ('prezzo', models.FloatField()),
                ('modello', models.CharField(blank=True, max_length=150, null=True)),
                ('anno', models.IntegerField(blank=True, null=True)),
                ('n_acquisti', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=100)),
                ('publicato', models.DateTimeField(auto_now_add=True)),
                ('modificato', models.DateTimeField(auto_now=True)),
                ('venditore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modificato',),
            },
        ),
    ]