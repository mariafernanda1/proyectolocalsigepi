# Generated by Django 3.2 on 2021-04-20 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moduloAdm', '0005_alter_usu_inf_pers_id_usu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usu_inf_contac',
            name='id_usu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]