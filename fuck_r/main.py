#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def replace_cmd(search, replacement, command):
    return command.replace(search, replacement)

def main():
    if len(sys.argv) < 4:
        print 'no fuck'
        return

    search = sys.argv[1]
    replacement = sys.argv[2]
    command = ' '.join(sys.argv[3:]).strip()

    new_command = replace_cmd(search, replacement, command)

    if new_command.startswith('fuck'):
        sys.stderr.write("Can't fuck twice")
        return

    sys.stderr.write(new_command + '\n')
    print new_command

if __name__ == '__main__':
    main()
