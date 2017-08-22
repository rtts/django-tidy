from django.conf import settings
from tidylib import tidy_document
from django.core.exceptions import ImproperlyConfigured

class TidyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response['Content-Type'] == 'text/html; charset=utf-8':
            if 'Content-Length' in response:
                raise ImproperlyConfigured('Please load TidyMiddleware _after_ CommonMiddleware otherwise the "Content-Length" header will be incorrect!')
            options = {
                'indent-spaces': 2,
                'doctype': 'html5',
                'input-encoding': 'utf8',
                'output-encoding': 'utf8',
                'drop-empty-elements': False,
            }
            response.content, errors = tidy_document(response.content, options)
            if errors and settings.DEBUG:
                raise ValueError('The generated HTML contains the following errors:\n\n' + errors)
        return response
