# Generated by Django 3.2 on 2021-04-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloAdm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conv_inv',
            name='val_max',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='conv_inv',
            name='val_min',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='curs_dict',
            name='num_est',
            field=models.IntegerField(verbose_name='Cantidad de estudiantes'),
        ),
    ]
