#!/usr/bin/python3
"""Markdown to HTML"""
from sys import argv, exit, stderr
import os


def run():
    """Main func"""
    if len(argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    if not os.path.isfile(argv[1]):
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
    result = ""

    with open(argv[1], 'r') as file:
        ul_level_started = True
        for line in file:
            print()
            """Handling Headers"""
            if '#' in line:
                h_level = line.count("#")
                text = line.strip('#\n').lstrip().rstrip()
                html = "<h{}>{}</h{}>".format(h_level, text, h_level)
                result += html + '\n'
            """Handling Unordered listing"""
            if '-' in line:
                if ul_level_started:
                    result += "<ul>\n"
                    ul_level_started = False
                text = line.strip('-\n').lstrip().rstrip()
                html = "<li>{}</li>".format(text)
                result += html + '\n'




    with open(argv[2], 'w') as file:
        file.write(result)
    exit(0)


if __name__ == "__main__":
    run()
