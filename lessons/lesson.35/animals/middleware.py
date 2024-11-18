import time


def print_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Мы работаем с запросом

        print('GET REQUEST', request)
        # time.sleep(2)
        response = get_response(request)

        print('GET RESPONSE', response)

        # Мы работаем с ответом
        return response

    return middleware


# Посчитать время выполнения запроса

class TopTimeMiddleware:
    def __init__(self, get_response):
        self.name = 'Top middleware'
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Пришел запрос

        start_time = time.time()

        response = self.get_response(request)

        end_time = time.time()

        delta_time = end_time - start_time

        print('NAME', self.name)
        print('Время выполнения запроса:', delta_time)

        return response


class DownTimeMiddleware(TopTimeMiddleware):

    def __init__(self, get_response):
        self.name = 'Down middleware'
        self.get_response = get_response


def handsome_django_middleware(get_response):

    def middleware(request):
        # Мы работаем с запросом

        request.is_get = request.method == 'GET'
        request.is_post = request.method == 'POST'

        response = get_response(request)

        # Мы работаем с ответом
        return response

    return middleware


def save_requests_middleware(get_response):

    def middleware(request):
        # Мы работаем с запросом

        # ? каждый день

        # 18.11.2024 - 0

        # текущую дату
        # в базу к этой дате прибавляем 1 запрос (Не реляционная)
        # redis 18.11.2024 += 1
        # clickhouse, influx db

        response = get_response(request)

        # Мы работаем с ответом
        return response

    return middleware