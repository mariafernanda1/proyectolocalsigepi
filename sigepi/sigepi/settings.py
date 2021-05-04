"""
Django settings for sigepi project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy
import os.path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lq0$99j+_d$_df570pcm1p^is3s1&f5p!7()8u(2dyi%r_ui4d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

#Aplicaciones del framework Django
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'django_select2',


]

# Aplicaciones de SIGEPI
SIGEPI_APPS = [
    'modadm.App_modadm', #Aplicación principal del módulo
    'modadm.App_regusu', #Aplicación de registro de usuario
    'modadm.App_regusui', #Aplicación de registro de usuario grupo
    'modadm.App_regusugr', #Aplicación de registro de usuario institucional
#    'modadm.App_regpat', #Aplicación de registro de Patrocinadores
#    'modadm.App_regben', #Aplicación de registro de Beneficiarios
    'modpry.App_modpry', #Aplicación principal del módulo
    'modpry.App_regpryi', #Aplicación de registro de proyecto de investigación
    'modpry.App_regprgi', #Aplicación de registro de programa de investigación
    'modpry.App_regppi', #Aplicación de registro de productos y procesos de investigación
#    'modpry.App_mlog', #Aplicación de marco lógico
    'modpry.App_gespry', #Aplicación de gestión de proyectos de investigación
    'modpry.App_evapry', #Aplicación de evaluación de proyectos de investigación
#    'modpry.App_disinv' #Aplicación de diseño de proyectos de investigación
    'modcons.App_cons' #Aplicación de consultas general sigepi
]

# Aplicaciones de terceros, exernas
EXT_APPS = [
]

INSTALLED_APPS= DJANGO_APPS + SIGEPI_APPS + EXT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware',
]

ROOT_URLCONF = 'sigepi.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/"plantillas",
            BASE_DIR/"plantillas/registro",
            "modadm/App_modadm/plantillas",
            "modadm/App_modadm/plantillas/reg_app",
            "modadm/App_modadm/plantillas/backend",
            "modadm/App_regusu/plantillas",
            "modadm/App_regusui/plantillas",
            "modadm/App_regusugr/plantillas",
            "modcons/App_cons/plantillas",
            BASE_DIR/"plantillas/consultas"

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sigepi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "static/"
#STATIC_ROOT = '/home/mariafz/Proyectos/sigepi/static/'
STATICFILES_DIRS = [BASE_DIR/"static"]

#variable para sustituir el usuario de django
#modelo y tabla
AUTH_USER_MODEL = 'App_modadm.User'

#LOGIN_REDIRECT_URL =  reverse_lazy('v_inicio')
LOGIN_REDIRECT_URL =  'inicioprb'

LOGOUT_REDIRECT_URL = 'registroprb'

LOGIN_URL = 'inicioprb'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
