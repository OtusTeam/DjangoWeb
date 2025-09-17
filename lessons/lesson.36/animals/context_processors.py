import datetime

def some_message(request):
    return {"some_message": datetime.datetime.now()}
