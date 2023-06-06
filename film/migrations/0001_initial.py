# Generated by Django 4.1.6 on 2023-06-06 03:56

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
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('cover', models.ImageField(blank=True, default='no-image.png', upload_to='media/cover/')),
                ('durasi', models.CharField(max_length=50)),
                ('deskripsi', models.TextField(blank=True, null=True, verbose_name='deskripsi')),
            ],
            options={
                'ordering': ['judul'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(verbose_name='tanggal tayang')),
                ('jam', models.TimeField(verbose_name='jam tayang')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
            ],
        ),
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('jadwal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.jadwal')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('jumlah', models.IntegerField(verbose_name='jumlah tiket')),
                ('tiket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.tiket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.genre'),
        ),
    ]
