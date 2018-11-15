from rest_framework import status
from rest_framework.views import exception_handler, set_rollback
from django.http import HttpResponse
class Error(Exception):

    def __init__(self, err_code, err_message='Internal Server Error',
                 message=u'服务器异常', status_code=status.HTTP_400_BAD_REQUEST):
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.status_code = status_code

    def __unicode__(self):
            return u'[Error] %d: %s(%d)' % (self.err_code, self.err_message, self.status_code)

    def getResponse(self):
        return ErrorResponse(self.err_code, self.err_message, self.message, self.status_code)


def ErrorResponse(err_code=400, err_message='Internal Server Error',
                  message=u'服务器异常', status=status.HTTP_400_BAD_REQUEST, headers=None):
    err = {
        'error_code': err_code,
        'error': err_message,
        'message': message,
    }
    return HttpResponse(err, status, headers=headers)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    if isinstance(exc, Error):
        set_rollback()
        return ErrorResponse(exc.err_code, exc.err_message, exc.message, status=exc.status_code)
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response
