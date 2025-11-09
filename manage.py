#!/usr/bin/env python
import os
import sys

# main entry point for running Django commands

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings") #default settings for Django
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
