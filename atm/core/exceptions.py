class AtmException(Exception):
    def __init__(self, i18n, message, **kwargs):
        self.i18n = i18n
        self.message = message
        self.params = kwargs

    @property
    def http_code(self):
        raise NotImplementedError()

    @property
    def json_friendly(self):
        return {
            'i18n': self.i18n,
            'message': self.message,
            'params': self.params
        }


class AtmUserError(AtmException):
    @property
    def http_code(self):
        return 400


class AtmNotFound(AtmException):
    @property
    def http_code(self):
        return 404


class AtmForbidden(AtmException):
    @property
    def http_code(self):
        return 403


class AtmUnprocessableError(AtmException):
    @property
    def http_code(self):
        return 409
