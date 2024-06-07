#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import ngrok

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    try:
        ngrok.set_auth_token("2QjcBSc1a8mdClgelHJaZXiXeh1_6S4DBgVfMRyHj8eQPCrS")
        listener = ngrok.forward(8000, hostname="singular-joey-normally.ngrok-free.app")
        print(f"Ingress established at {listener.url()}")
    except Exception as e:
        print(f"Error occurred: {e}")
        ngrok.disconnect()
        # ngrok.set_auth_token("2QjcBSc1a8mdClgelHJaZXiXeh1_6S4DBgVfMRyHj8eQPCrS")
        # listener = ngrok.forward(8000, hostname="singular-joey-normally.ngrok-free.app")
        # print(f"Ingress established at {listener.url()}")

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
