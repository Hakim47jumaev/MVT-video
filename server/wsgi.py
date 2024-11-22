"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Укажите путь к вашему проекту
path = '/home/hakimjumaev02/mysite'
if path not in sys.path:
    sys.path.append(path)

# Укажите имя вашей папки с приложением (где settings.py)
os.environ['DJANGO_SETTINGS_MODULE'] = 'MVT-video.settings'

# Активация виртуального окружения
from django.core.wsgi import get_wsgi_application
from pathlib import Path

activate_this = '/home/hakimjumaev02/.virtualenvs/myenv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

application = get_wsgi_application()

