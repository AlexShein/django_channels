from django.http import HttpResponse
from django.template import loader
import django


def first(request):
    template = loader.get_template('echo_test.html')
    context = {
        'version': django.VERSION,
    }
    return HttpResponse(template.render(context, request))
