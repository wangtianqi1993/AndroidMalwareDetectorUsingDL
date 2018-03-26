#!/usr/bin/python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer

from detector.web import app

if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    app.debug = True
    http_server = WSGIServer(('', 9527), app)
    http_server.serve_forever()
