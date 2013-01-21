
import json
from django.http import HttpResponse
import mimes

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def homepage(request):
    data = {'ip': get_client_ip(request),
            'host': request.get_host(),
            'request_meta': {
                'http_referer': request.META.get('HTTP_REFERER'),
                'content_length': request.META.get('CONTENT_LENGTH'),
                'content_type': request.META.get('CONTENT_TYPE'),
                'http_accept_encoding': request.META.get('HTTP_ACCEPT_ENCODING'),
                'http_accept_language': request.META.get('HTTP_ACCEPT_LANGUAGE'),
                'is_ajax': request.is_ajax(),
                'method': request.method,
            },
            'pages': {
                'home': '/',
                'about': '/about',
            }
    }
    if request.method == 'GET':
        data['params'] = request.GET
    if request.method == 'POST':
        data['params'] = request.POST

    return HttpResponse(json.dumps(data), mimetype=mimes.JSON)

def about(request):
    data = {'description': 'A simple network and development tool to inspect HTTP requests and initiating clients',
            'developer': 'Alan Illing',
            'developer-website': 'http://alanilling.com',
            'developer-github': 'https://github.com/ailling'
    }
    return HttpResponse(json.dumps(data), mimetype=mimes.JSON)

def error404(request):
    return HttpResponse(json.dumps({'error': '404', 'description': 'Not found'}), mimetype=mimes.JSON)

def error500(request):
    return HttpResponse(json.dumps({'error': '500', 'description': 'Server error'}), mimetype=mimes.JSON)

def error403(request):
    return HttpResponse(json.dumps({'error': '403', 'description': 'Forbidden'}), mimetype=mimes.JSON)

