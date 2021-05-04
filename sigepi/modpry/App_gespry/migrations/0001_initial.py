# Generated by Django 3.1.7 on 2021-05-04 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_ges_pry',
            fields=[
                ('id_ges_pry', models.AutoField(primary_key=True, serialize=False)),
                ('nomb_ges_pry', models.CharField(max_length=40, verbose_name='Nombre de la App ')),
                ('desc_ges_pry', models.CharField(max_length=40, verbose_name=' descripcion de la App  ')),
                ('status_ges_pry', models.BooleanField(default=False, verbose_name='si logro el objetivo')),
            ],
            options={
                'verbose_name': 'app_ges_pry',
                'verbose_name_plural': 'app_ges_prys',
            },
        ),
        migrations.CreateModel(
            name='inf_ges_pry',
            fields=[
                ('inf_ges_pry', models.AutoField(primary_key=True, serialize=False)),
                ('Cpto_proy', models.CharField(max_length=40, verbose_name='Conceptualización del Proyecto:')),
                ('Form_proy', models.CharField(max_length=40, verbose_name='Formulación o diseño del Proyecto')),
                ('Eva_proy', models.CharField(max_length=40, verbose_name='evaluación del Proyecto:')),
                ('Eje_proy', models.CharField(max_length=40, verbose_name='Ejecución del Proyecto')),
                ('Proy', models.CharField(max_length=80, verbose_name='compilación de de tres momentos')),
            ],
            options={
                'verbose_name': 'inf_ges_pry',
                'verbose_name_plural': 'inf_ges_prys',
            },
        ),
    ]
