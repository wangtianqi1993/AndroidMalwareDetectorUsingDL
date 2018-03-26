#!/usr/bin/python
# -*- coding: utf-8 -*-

from detector.web import app

def main():
    app.run(host='0.0.0.0', port=1234, debug=True)


if __name__ == '__main__':
    main()
