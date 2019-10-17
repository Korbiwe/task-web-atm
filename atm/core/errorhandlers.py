from werkzeug.exceptions import HTTPException

from atm.config import Config
from atm.core.utils import json_response
from atm.core.exceptions import AtmException

from atm.core import core


@core.app_errorhandler(AtmException)
def handle_api_errors(e: AtmException):
    return json_response(error=e.json_friendly), e.http_code


@core.app_errorhandler(HTTPException)
def handle_http_errors(e: HTTPException):
    if 300 <= e.code <= 399:
        return e
    if 400 <= e.code <= 499:
        return json_response(error={'message': str(e)}), e.code
    if 500 <= e.code <= 599:
        if Config.DEBUG:
            return json_response(error={'message': str(e)}), e.code
        else:
            return json_response(error={'message': 'Internal server error.'}), e.code


@core.app_errorhandler(Exception)
def handle_uncaught_errors(e: Exception):
    if Config.DEBUG:
        return json_response(error={'message': str(e)}), 500
    else:
        return json_response(
            error={'message': 'Something went terribly wrong. Please report this to the site owner.'}
        ), 500
