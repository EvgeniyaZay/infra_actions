from django.http import HttpResponse


def index(request):
    data = 'У меня получилось!'
    return HttpResponse(data, status_code=200)


def second_page(request):
    data = 'А это вторая страница!'
    return HttpResponse(data, status_code=200)
