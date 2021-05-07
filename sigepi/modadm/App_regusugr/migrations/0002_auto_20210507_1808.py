# Generated by Django 3.1.7 on 2021-05-07 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_regusugr', '0001_initial'),
        ('App_modadm', '0002_auto_20210507_1808'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usugr',
            name='id_usu_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usu_nr',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol'),
        ),
        migrations.AddField(
            model_name='rl_usugr_inf_rol_actual',
            name='id_usugr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr'),
        ),
        migrations.AddField(
            model_name='rl_usugr_inf_rol_actual',
            name='rol_act',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.rol'),
        ),
        migrations.AddField(
            model_name='rl_usugr_form_acad_gr',
            name='id_usugr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr_inf_gr'),
        ),
        migrations.AddField(
            model_name='rl_usugr_form_acad_gr',
            name='ls_form_gr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.form_acad_gr'),
        ),
        migrations.AddField(
            model_name='rl_usugr_curs_ofer',
            name='id_usugr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr_inf_gr'),
        ),
        migrations.AddField(
            model_name='rl_usugr_curs_ofer',
            name='ls_cursofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.curs_ofer'),
        ),
        migrations.AddField(
            model_name='rel_usugr_ls_usu_nr',
            name='id_gr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr'),
        ),
        migrations.AddField(
            model_name='rel_usugr_ls_usu_nr',
            name='ls_int_nr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usu_nr'),
        ),
        migrations.AddField(
            model_name='rel_usugr_ls_usu',
            name='id_gr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr'),
        ),
        migrations.AddField(
            model_name='rel_usugr_ls_usu',
            name='ls_int_usu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rel_usugr_ls_etp',
            name='id_gr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr'),
        ),
        migrations.AddField(
            model_name='rel_usugr_ls_etp',
            name='ls_etp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.etapa_gr'),
        ),
        migrations.AddField(
            model_name='app_reg_gr',
            name='id_app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modadm.app_mod'),
        ),
    ]