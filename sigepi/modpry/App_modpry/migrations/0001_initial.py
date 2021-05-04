# Generated by Django 3.1.7 on 2021-05-04 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mod_pry',
            fields=[
                ('id_mod_pry', models.AutoField(primary_key=True, serialize=False)),
                ('nomb_mod_pry', models.CharField(max_length=40, verbose_name='Nombre ')),
                ('desc_mod_pry', models.CharField(max_length=40, verbose_name='Decripcion ')),
                ('status_mod_pry', models.BooleanField(default=False, verbose_name='¿status de la aplicacion.?')),
            ],
            options={
                'verbose_name': 'mod_pry',
                'verbose_name_plural': 'mod_prys',
            },
        ),
    ]
