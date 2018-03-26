#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify


def _wrapper_result(result, message, code):
    return jsonify({
        'code': code,
        'message': message,
        'result': result,
    })


def wrapper_response_success(result, message='success', code=200):
    return _wrapper_result(result, message, code)


def wrapper_response_400(result,
                         message='there is an error in request params.',
                         code=400):
    return _wrapper_result(result, message, code)


def wrapper_response_500(result, message='there is an error occur at server.',
                         code=500):
    return _wrapper_result(result, message, code)
