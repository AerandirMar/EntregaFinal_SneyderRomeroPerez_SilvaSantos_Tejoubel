# Generated by Django 4.0.3 on 2022-06-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fecha_estreno', models.DateField()),
                ('duracion', models.IntegerField()),
                ('sinopsis', models.CharField(max_length=1000)),
            ],
        ),
    ]
