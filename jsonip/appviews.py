
import json
from django.http import HttpResponse


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
            'is_ajax': request.is_ajax(),
            'method': request.method,
            'meta': {
                'http_referer': request.META.get('HTTP_REFERER'),
                'content_length': request.META.get('CONTENT_LENGTH'),
                'content_type': request.META.get('CONTENT_TYPE'),
                'http_accept_encoding': request.META.get('HTTP_ACCEPT_ENCODING'),
                'http_accept_language': request.META.get('HTTP_ACCEPT_LANGUAGE'),
            },
            'pages': {
                'home': '/',
                'about': '/about',
            }
    }

    return HttpResponse(json.dumps(data))

def about(request):
    data = {'description': 'A simple network and development tool to return information your HTTP request and the requesting client',
            'developer': 'Alan Illing',
            'developer-website': 'http://alanilling.com',
            'developer-github': 'https://github.com/ailling'
    }
    return HttpResponse(json.dumps(data))

def error404(request):
    return HttpResponse(json.dumps({'error': '404', 'description': 'Not found'}))

def error500(request):
    return HttpResponse(json.dumps({'error': '500', 'description': 'Server error'}))

def error403(request):
    return HttpResponse(json.dumps({'error': '403', 'description': 'Forbidden'}))

