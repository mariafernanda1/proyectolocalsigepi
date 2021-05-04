from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.register(mod)
admin.site.register(app_mod)
admin.site.register(listado_aplicativo)
admin.site.register(ext_mod)
admin.site.register(ext_app)
admin.site.register(rol)
admin.site.register(param_config)
admin.site.register(Permiso)
admin.site.register(rol_permiso)
admin.site.register(func_app)
admin.site.register(rl_mod_app_mod)
admin.site.register(rl_mod_rol)
admin.site.register(rl_mod_param_cnf)
admin.site.register(rl_mod_func)
admin.site.register(rl_app_mod_rol)
admin.site.register(rl_app_mod_param_cnf)
admin.site.register(rl_app_mod_func)
admin.site.register(usu)
admin.site.register(mod_adm)
admin.site.register(adm_install)
admin.site.register(log_mod_rol)
admin.site.register(fuente_ins)
admin.site.register(log_acc_mod)
admin.site.register(usu_inf_apps)
admin.site.register(rl_usu_inf_apps_rol)
admin.site.register(discapacidad)
admin.site.register(usu_inf_pers)
admin.site.register(usu_inf_contac)
admin.site.register(red_soc)
admin.site.register(rl_usu_inf_red_social)
admin.site.register(form_acad)
admin.site.register(usu_inf_acad)
admin.site.register(rl_usu_inf_form_acad)
admin.site.register(curs_dict)
admin.site.register(rl_usu_inf_contac_curs_dict)
admin.site.register(usu_inf_prof)
admin.site.register(rl_usu_inf_prof_empleos)
admin.site.register(empleos)
admin.site.register(habilidades)
admin.site.register(usu_inf_hab)
admin.site.register(valid_hab)
admin.site.register(app_reg_usu)

admin.site.register(etapa_gr)
admin.site.register(usugr)
admin.site.register(usu_nr)
admin.site.register(rel_usugr_ls_etp)
admin.site.register(rel_usugr_ls_usu)
admin.site.register(rel_usugr_ls_usu_nr)
admin.site.register(usugr_inf_apps)
admin.site.register(rl_usugr_inf_rol_Actual)
admin.site.register(usugr_inf_gr)
admin.site.register(usugr_inf_contac)
admin.site.register(usugr_inf_red_social)
admin.site.register(form_acad_gr)
admin.site.register(usugr_inf_acad)
admin.site.register(curs_ofer)
admin.site.register(usugr_form_acad_gr)
admin.site.register(usugr_curs_ofer)
admin.site.register(app_reg_gr)

admin.site.register(usui)
admin.site.register(usui_inf_apps)
admin.site.register(usui_rol_actual)
admin.site.register(usui_inf_inst)
admin.site.register(usui_inf_contac)
admin.site.register(usui_red_social)
admin.site.register(usui_inf_acad)
admin.site.register(prog_ofer)
admin.site.register(usuo_prog_ofer)
admin.site.register(usui_inf_inv)
admin.site.register(conv_inv)
admin.site.register(rl_usui_usugr)
admin.site.register(rl_usui_usu)
admin.site.register(rl_usui_conv_inv)
admin.site.register(app_reg_ins)