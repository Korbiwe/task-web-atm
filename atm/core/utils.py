from typing import Any

from uuid import uuid4

from flask import jsonify


def random_uuid4_as_hex():
    return uuid4().hex


def json_response(result: Any = None, error: dict = None, **kwargs):
    if error and result:
        raise ValueError('Using both error and result is not allowed!')

    if error and len(kwargs) != 0:
        # if we have both error and kwargs, add kwargs to params of the error object
        temp = error.get('params', {})
        error['params'] = {**temp, **kwargs}

    if error:
        # if there is are no i18n, message and/or params, we should add that to the error to comply with our rules
        if 'params' not in error:
            error['params'] = {}

        if 'i18n' not in error:
            error['i18n'] = 'tbd'

        if 'message' not in error:
            error['message'] = 'Unknown error.'

        return jsonify(success=True, error=error, result=None)

    if result is not None:
        # if we have a result, add kwargs to the parent object
        return jsonify(success=True, error=None, result=result, **kwargs)
    elif len(kwargs) != 0:
        # if we don't have a result, kwargs IS our result
        return jsonify(success=True, error=None, result=kwargs)
    else:
        # no kwargs, no result
        return jsonify(success=True, error=None, result=None)
