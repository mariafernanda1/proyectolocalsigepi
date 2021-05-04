# Generated by Django 3.1.7 on 2021-05-04 01:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_modpry', '0001_initial'),
        ('App_regusugr', '0001_initial'),
        ('App_evapry', '0001_initial'),
        ('App_regpryi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rel_evalucion_pry',
            name='id_investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rel_evalucion_pry',
            name='id_tipos_evalucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_evapry.tipos_evalucion'),
        ),
        migrations.AddField(
            model_name='evalucion_pry',
            name='id_grup_bd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regusugr.usugr'),
        ),
        migrations.AddField(
            model_name='criterios_pry',
            name='id_criterios_pry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_evapry.criterios'),
        ),
        migrations.AddField(
            model_name='criterios_pry',
            name='id_proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_regpryi.inf_pry'),
        ),
        migrations.AddField(
            model_name='app_ev_pry',
            name='id_mod_pry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_modpry.mod_pry'),
        ),
    ]