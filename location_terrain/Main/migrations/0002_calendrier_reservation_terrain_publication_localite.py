# Generated by Django 4.0.6 on 2022-10-05 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.calendrier')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.client')),
                ('gerant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.gerant')),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('surface', models.IntegerField()),
                ('description', models.TextField()),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('gerant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.gerant')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_publication', models.DateTimeField()),
                ('gerant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.gerant')),
            ],
        ),
        migrations.CreateModel(
            name='Localite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('terrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.terrain')),
            ],
        ),
    ]
