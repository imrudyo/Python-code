#!/usr/bin/python

import sys
import base64

def main():

    args = sys.argv[1:]

    if not args:
        print 'usage: b64encdec.py b64string'
        sys.exit(1)

    string = args[0]

    print base64.b64decode(string)

if __name__ == '__main__':
    main()
