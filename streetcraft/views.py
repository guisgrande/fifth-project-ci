from django.shortcuts import render


def handler400(request, exception):
    """ Bad Request 400 page view function """
    return render(request, '400.html')


def handler403(request, exception):
    """ Page Forbidden 403 page view function """
    return render(request, '403.html')


def handler404(request, exception):
    """ Page Not Found 404 page view function """
    return render(request, '404.html')


def handler500(request):
    """ Server Error 500 page view function """
    return render(request, '500.html')
