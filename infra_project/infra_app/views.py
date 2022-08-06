from django.http import HttpResponse


def index(request):
    return HttpResponse('Это новая главная страница!!!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
