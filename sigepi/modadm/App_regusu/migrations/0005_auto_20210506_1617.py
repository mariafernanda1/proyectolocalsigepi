# Generated by Django 3.1.7 on 2021-05-06 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_regusu', '0004_auto_20210506_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rl_usu_inf_hab',
            old_name='ls_habs',
            new_name='id_hab',
        ),
    ]