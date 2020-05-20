from django.conf import settings
from tidylib import tidy_document
from django.core.exceptions import ImproperlyConfigured

class TidyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'Content-Type' in response and response['Content-Type'] == 'text/html; charset=utf-8':
            if 'Content-Length' in response:
                raise ImproperlyConfigured('Please load TidyMiddleware _after_ CommonMiddleware otherwise the "Content-Length" header will be incorrect!')
            options = {
                'wrap': 80,
                'indent-spaces': 2,
                'vertical-space': True,
                'doctype': 'html5',
                'drop-empty-elements': False,
            }

            if response.content:
                tidy_content, errors = tidy_document(response.content, options)
                print(errors)
                response.content = tidy_content

        return response
