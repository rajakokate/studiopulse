# manage.py

#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studiopulse_api.settings')
    try:
        from django.core.management import execute_from_command_line
        import django
        django.setup()

        # Apply migrations
        from django.core.management import call_command
        call_command('migrate', interactive=False)


    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
