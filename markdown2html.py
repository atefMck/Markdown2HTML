#!/usr/bin/python3
"""Markdown to HTML"""
from sys import argv, exit, stderr
import os
if len(argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=stderr)
    exit(1)
if not os.path.isfile(argv[1]):
    print("Missing {}".format(argv[1]), file=stderr)
    exit(1)
exit(0)

