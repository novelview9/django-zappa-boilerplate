#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json


def main():
    if 'SERVERTYPE' in os.environ and os.environ['SERVERTYPE'] == 'AWS Lambda':
        json_data = open('zappa_settings.json')
        env_vars = json.load(json_data)['dev']['environment_variables']
        for key, val in env_vars.items():
            os.environ[key] = val

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
