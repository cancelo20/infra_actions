from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! И у сервера тоже!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
